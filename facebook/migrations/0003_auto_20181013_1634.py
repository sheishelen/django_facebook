# Generated by Django 2.1.1 on 2018-10-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='page',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
