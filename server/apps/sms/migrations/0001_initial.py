# Generated by Django 3.2.5 on 2021-08-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=160)),
                ('receiver', models.CharField(max_length=50)),
            ],
        ),
    ]
