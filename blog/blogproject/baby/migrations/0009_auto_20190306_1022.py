# Generated by Django 2.1.4 on 2019-03-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0008_auto_20190306_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='created_time',
            field=models.DateTimeField(default='2018-12-15 20:51:12.000000'),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_time',
            field=models.DateTimeField(default='2018-12-15 20:51:12.000000'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='tinypicurl',
            field=models.URLField(),
        ),
    ]