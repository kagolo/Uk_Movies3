# Generated by Django 3.2.8 on 2021-10-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0012_alter_episode_episode_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
    ]
