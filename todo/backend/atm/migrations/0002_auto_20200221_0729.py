# Generated by Django 2.2 on 2020-02-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('card_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
