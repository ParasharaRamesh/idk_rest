# Generated by Django 2.1.1 on 2018-11-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDK_rest', '0003_auto_20181122_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoretable',
            name='scoreVal',
            field=models.IntegerField(default=0),
        ),
    ]
