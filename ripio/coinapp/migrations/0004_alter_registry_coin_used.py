# Generated by Django 4.0.5 on 2022-06-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinapp', '0003_rename_receiver_id_registry_receiver_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='coin_used',
            field=models.CharField(max_length=200),
        ),
    ]
