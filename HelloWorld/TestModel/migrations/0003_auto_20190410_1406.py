# Generated by Django 2.1.7 on 2019-04-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20190401_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mMark', models.CharField(max_length=256)),
                ('mNote', models.CharField(max_length=1024)),
                ('mPrice', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='weathers',
            name='wDate',
            field=models.CharField(max_length=16),
        ),
    ]
