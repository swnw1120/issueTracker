# Generated by Django 4.0.3 on 2022-04-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Description',
            field=models.TextField(max_length=250),
        ),
    ]