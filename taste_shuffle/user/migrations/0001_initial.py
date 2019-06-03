# Generated by Django 2.2.1 on 2019-05-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('team_number', models.IntegerField()),
                ('per_team', models.IntegerField()),
                ('leader_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_roomnum', models.IntegerField()),
                ('user_select', models.IntegerField()),
            ],
        ),
    ]
