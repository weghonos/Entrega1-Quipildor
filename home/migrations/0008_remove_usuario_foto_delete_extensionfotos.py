# Generated by Django 4.1.3 on 2022-11-08 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_usuario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto',
        ),
        migrations.DeleteModel(
            name='ExtensionFotos',
        ),
    ]
