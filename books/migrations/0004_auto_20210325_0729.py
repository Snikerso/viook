# Generated by Django 3.1.7 on 2021-03-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210325_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings_count',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]