# Generated by Django 2.1.4 on 2019-03-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0004_auto_20190302_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='tinypicurl',
            field=models.URLField(blank=True),
        ),
    ]