# Generated by Django 5.0.6 on 2024-06-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='initial_recipient_secret',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='initial_sender_secret',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
