# Generated by Django 2.1.4 on 2019-03-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0013_age_group_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_time',
            field=models.DateTimeField(),
        ),
    ]