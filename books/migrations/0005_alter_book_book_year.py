# Generated by Django 4.2.13 on 2024-07-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_finished_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_year',
            field=models.IntegerField(max_length=4),
        ),
    ]
