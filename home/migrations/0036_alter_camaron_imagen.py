# Generated by Django 4.1.3 on 2022-11-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_camaron_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camaron',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/'),
        ),
    ]
