# Generated by Django 4.2 on 2024-10-16 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Conference', '0003_alter_conference_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='reservation',
            field=models.ManyToManyField(related_name='confReserv', through='Conference.Reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
