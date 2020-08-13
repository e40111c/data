# Generated by Django 3.1 on 2020-08-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CosmeticIngredient',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=255)),
                ('ingredient', models.TextField(blank=True, null=True)),
                ('acne', models.TextField(blank=True, null=True)),
                ('pchar', models.TextField(blank=True, null=True)),
                ('dalton', models.TextField(blank=True, null=True)),
                ('safeness', models.TextField(blank=True, null=True)),
                ('stimulation', models.TextField(blank=True, null=True)),
                ('score', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cosmetic_ingredient',
            },
        ),
        migrations.CreateModel(
            name='CosmeticProduct',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('pname', models.CharField(max_length=255)),
                ('char', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cosmetic_product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('continuous', models.CharField(blank=True, max_length=255, null=True)),
                ('cnt', models.CharField(blank=True, max_length=20, null=True)),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerProduct',
            fields=[
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('pname', models.CharField(blank=True, max_length=255, null=True)),
                ('pbrand', models.CharField(blank=True, max_length=255, null=True)),
                ('fit_prod', models.TextField(blank=True, db_column='fit_Prod', null=True)),
                ('unfit_prod', models.TextField(blank=True, db_column='unfit_Prod', null=True)),
                ('reg_date', models.DateTimeField()),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer_product',
            },
        ),
        migrations.CreateModel(
            name='CustomerStatus',
            fields=[
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('continuous', models.IntegerField(blank=True, null=True)),
                ('cnt', models.IntegerField(blank=True, null=True)),
                ('reg_date', models.DateTimeField()),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer_status',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('pname', models.CharField(blank=True, max_length=255, null=True)),
                ('pbrand', models.CharField(blank=True, max_length=255, null=True)),
                ('reg_date', models.DateTimeField()),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]