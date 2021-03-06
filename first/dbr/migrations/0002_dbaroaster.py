# Generated by Django 3.2.5 on 2022-04-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbaRoaster',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('day', models.CharField(blank=True, max_length=25, null=True)),
                ('deepak', models.CharField(blank=True, max_length=25, null=True)),
                ('nainesh', models.CharField(blank=True, max_length=25, null=True)),
                ('akhilesh', models.CharField(blank=True, max_length=25, null=True)),
                ('gaurav', models.CharField(blank=True, max_length=25, null=True)),
                ('pranav', models.CharField(blank=True, max_length=25, null=True)),
                ('prashant', models.CharField(blank=True, max_length=25, null=True)),
                ('rohan', models.CharField(blank=True, max_length=25, null=True)),
                ('shreeyash', models.CharField(blank=True, max_length=25, null=True)),
                ('ankit', models.CharField(blank=True, max_length=25, null=True)),
                ('ashvini', models.CharField(blank=True, max_length=25, null=True)),
                ('kripa', models.CharField(blank=True, max_length=25, null=True)),
                ('siddesh', models.CharField(blank=True, max_length=25, null=True)),
                ('biki', models.CharField(blank=True, max_length=25, null=True)),
                ('sumit', models.CharField(blank=True, max_length=25, null=True)),
                ('mrunal', models.CharField(blank=True, max_length=25, null=True)),
                ('pritam', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'dba_roaster',
                'managed': False,
            },
        ),
    ]
