# Generated by Django 4.0.1 on 2022-03-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_alter_location_end_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='create_data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала рассадки'),
        ),
    ]
