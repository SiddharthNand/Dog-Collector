# Generated by Django 4.1.1 on 2022-12-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_naps_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]