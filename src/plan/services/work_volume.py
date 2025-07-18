from plan.models import Factory, FactoryUser, WorkVolume
from users.models import User
from utils import clickhouse_client


class WorkVolumeService:

    def __init__(self, user: User, data: dict):
        self.user = user
        self.data = data
        self.factory = None
        self.clickhouse_client = clickhouse_client

    def get_factory(self) -> Factory | None:
        if self.factory is None:
            self.factory = Factory.objects.filter(id=self.data['factory']).first()
        return self.factory

    def check_factory_exists(self) -> bool:
        return self.get_factory() is not None

    def check_user_permissions(self) -> bool:
        if self.user.groups.filter(name='Менеджер по взаимодействию с ЗМК').exists():
            return True
        if self.user.groups.filter(name='Представитель ЗМК').exists():
            return FactoryUser.objects.filter(user=self.user, factory=self.factory).exists()
        return False

    def create_or_update_work_volume(self):
        print(self.data)
        return WorkVolume.objects.update_or_create(
            factory=self.factory,
            start=self.data['start'],
            finish=self.data['finish'],
            defaults={
                'weight': self.data['weight'],
            }
        )

    def insert_work_volume_record_clickhouse(self, work_volume) -> None:
        insert_query = """
            INSERT INTO work_volume_record
            (factory, start, finish, weight, author, created)
            VALUES
        """

        self.clickhouse_client.execute(insert_query, [(
            str(self.factory.external_id),
            work_volume.start,
            work_volume.finish,
            work_volume.weight,
            self.user.id,
            work_volume.created
        )])

    def process(self) -> dict[str, str | int]:
        if not self.check_factory_exists():
            return {'error': 'Factory not found', 'errorCode': 174, 'status': 404}

        if not self.check_user_permissions():
            return {'error': 'Permission denied', 'errorCode': 174, 'status': 404}

        work_volume, created = self.create_or_update_work_volume()

        try:
            self.insert_work_volume_record_clickhouse(work_volume)
        except Exception as e:
            return {'error': f'ClickHouse insert failed: {e}', 'status': 500}

        return {'result': 'success', 'status': 201}
