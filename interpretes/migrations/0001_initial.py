# Generated by Django 4.1 on 2023-05-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('genero', models.TextField(max_length=50)),
                ('clasificacion', models.TextField(max_length=30)),
                ('aparicion', models.DateField()),
            ],
        ),
    ]
