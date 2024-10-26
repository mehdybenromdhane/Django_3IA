# Generated by Django 4.2 on 2024-10-08 14:51

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name': 'Participant'},
        ),
        migrations.AlterField(
            model_name='participant',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[User.models.cinValidator]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=50, validators=[User.models.emailValidator]),
        ),
    ]
