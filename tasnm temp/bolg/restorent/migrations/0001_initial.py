# Generated by Django 3.1.2 on 2020-12-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMOdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('contect', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'blogmaster',
            },
        ),
    ]
