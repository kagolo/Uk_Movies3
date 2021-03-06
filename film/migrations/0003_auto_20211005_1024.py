# Generated by Django 3.2.7 on 2021-10-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_title', models.CharField(max_length=200)),
                ('serie_actor', models.CharField(max_length=200)),
                ('serie_general', models.CharField(max_length=300)),
                ('serie_VJ', models.CharField(max_length=200)),
                ('serie_cost', models.CharField(max_length=200)),
                ('serie_season', models.CharField(max_length=200)),
                ('serie_episode', models.CharField(max_length=200)),
                ('serie_status1', models.CharField(choices=[('New', 'New'), ('Featured', 'Featured')], max_length=300)),
                ('serie_status2', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=200)),
                ('serie_release_date', models.DateField(auto_now_add=True)),
                ('serie_image', models.ImageField(upload_to='')),
                ('serie_video', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='movie_translator',
            new_name='movie_VJ',
        ),
        migrations.AddField(
            model_name='register_users',
            name='contact',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
