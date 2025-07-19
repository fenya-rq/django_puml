"""
Manually creating users, factories and factory_users for testing goals.
Should be removed before production using.
"""

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_factories_and_users(apps, schema_editor):
    Factory = apps.get_model('plan', 'Factory')
    FactoryUser = apps.get_model('plan', 'FactoryUser')
    User = apps.get_model('users', 'User')

    factories = [
        Factory(name='Завод А'),
        Factory(name='Завод Б'),
        Factory(name='Завод В'),
        Factory(name='Завод Г'),
    ]
    factories = Factory.objects.bulk_create(factories)

    users = [
        User(
            username=f'user{num}',
            email=f'user{num}@example.com',
            password=make_password(f'password{num}')
        ) for num in range(1,6)
    ]
    users = User.objects.bulk_create(users)

    factory_users = [
        FactoryUser(user=users[0], factory=factories[0]),
        FactoryUser(user=users[1], factory=factories[1]),
        FactoryUser(user=users[2], factory=factories[2]),
        FactoryUser(user=users[3], factory=factories[3]),
    ]
    FactoryUser.objects.bulk_create(factory_users)

class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_create_groups'),
    ]

    operations = [
        migrations.RunPython(create_factories_and_users),
    ]
