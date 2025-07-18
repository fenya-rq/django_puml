import uuid

from django.db import models

from users.models import User


class Factory(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'ЗМК {self.name}'

class FactoryUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'factory'], name='unique_factory_user')
        ]

    def __str__(self):
        return f'{self.user} - пользователь {self.factory}'

class WorkVolumeRecord(models.Model):
    factory = models.UUIDField()
    start = models.DateField()
    finish = models.DateField()
    weight = models.PositiveIntegerField()
    author = models.PositiveBigIntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'work_volume_record'


class WorkVolume(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    start = models.DateField()
    finish = models.DateField()
    weight = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Объём работ {self.factory}'
