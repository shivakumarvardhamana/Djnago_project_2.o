# Generated by Django 4.1.2 on 2022-12-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_usercreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='login2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usename', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usercreate',
            name='password1',
        ),
    ]
