# Generated by Django 4.0.5 on 2022-06-14 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coinapp', '0002_rename_coin_name_user_coin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registry',
            old_name='receiver_id',
            new_name='receiver_name',
        ),
        migrations.RenameField(
            model_name='registry',
            old_name='sender_id',
            new_name='sender_name',
        ),
    ]
