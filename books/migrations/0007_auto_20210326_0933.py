# Generated by Django 3.1.7 on 2021-03-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210325_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avarage_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
