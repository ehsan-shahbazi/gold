# Generated by Django 2.2.12 on 2020-06-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200601_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('publisher_name', models.CharField(default='Tasnim', max_length=100)),
                ('date_time', models.DateTimeField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsWrapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_url', models.URLField(default='https://www.tgju.org')),
                ('kind', models.IntegerField(default=0)),
            ],
        ),
    ]
