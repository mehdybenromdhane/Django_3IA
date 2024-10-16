# Generated by Django 4.2 on 2024-10-15 23:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Conference', '0002_alter_reservation_conference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='reservation',
            field=models.ManyToManyField(related_name='conf_reserv', through='Conference.Reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]