# Generated by Django 4.0.3 on 2022-08-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
