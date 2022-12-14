# Generated by Django 4.1.1 on 2022-11-11 15:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0034_rename_user_post_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camaron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=30)),
                ('variedad', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=30)),
                ('ph', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateField(auto_now_add=True, null=True)),
                ('contenido', ckeditor.fields.RichTextField(null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
