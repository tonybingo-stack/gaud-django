# Generated by Django 4.1.3 on 2022-11-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0002_dweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
