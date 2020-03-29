# Generated by Django 2.2.11 on 2020-03-21 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0003_auto_20200320_1333'),
        ('Project', '0005_auto_20200321_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_User_Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dproject', to='Project.Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users_auth.Users')),
            ],
        ),
    ]