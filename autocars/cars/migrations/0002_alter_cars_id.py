# Generated by Django 3.2.22 on 2023-10-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
