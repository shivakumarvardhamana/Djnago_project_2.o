# Generated by Django 4.1.2 on 2022-12-12 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_login2_remove_usercreate_password1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login2',
            old_name='usename',
            new_name='username',
        ),
    ]
