# Generated by Django 4.1.2 on 2022-12-23 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_employe_emp_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author')),
            ],
        ),
    ]