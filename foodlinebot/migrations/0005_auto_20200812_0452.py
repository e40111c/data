# Generated by Django 3.1 on 2020-08-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlinebot', '0004_customerstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerStatus',
        ),
    ]