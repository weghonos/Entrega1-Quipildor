# Generated by Django 4.1.3 on 2022-11-08 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
