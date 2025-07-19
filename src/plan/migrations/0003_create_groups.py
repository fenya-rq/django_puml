"""Manually creating groups for testing goals. Should be removed before production using."""

from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='Менеджер по взаимодействию с ЗМК')
    Group.objects.get_or_create(name='Представитель ЗМК')

class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
