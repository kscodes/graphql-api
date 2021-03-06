# Generated by Django 3.2.3 on 2021-05-28 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('name', models.CharField(blank=True, max_length=49, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'banks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(blank=True, max_length=74, null=True)),
                ('address', models.CharField(blank=True, max_length=195, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=26, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bankinfo.banks')),
            ],
            options={
                'db_table': 'branches',
                'managed': True,
            },
        ),
    ]
