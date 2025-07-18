from clickhouse_driver import Client
from django.conf import settings


class ClickhouseClient:
    def __init__(self):
        cfg = settings.CLICKHOUSE
        self.client = Client(
            host=cfg['host'],
            port=cfg['port'],
            user=cfg['user'],
            password=cfg['password'],
            database=cfg['database'],
        )

    def execute(self, query, params=None):
        return self.client.execute(query, params or [])

clickhouse_client = ClickhouseClient().client
