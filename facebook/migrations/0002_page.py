# Generated by Django 2.1.1 on 2018-10-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(max_length=20)),
                ('page_name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]