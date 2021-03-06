# Generated by Django 2.2.12 on 2020-06-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_paired'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='buy_price',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='material',
            name='persian_name',
            field=models.CharField(default='سکّه', max_length=100),
        ),
        migrations.AddField(
            model_name='material',
            name='sell_price',
            field=models.IntegerField(default=101),
        ),
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
