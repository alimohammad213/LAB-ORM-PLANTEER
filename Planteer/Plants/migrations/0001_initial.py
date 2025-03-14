# Generated by Django 5.1.7 on 2025-03-09 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Tree', 'Tree'), ('Fruit', 'Fruit'), ('Vegetable', 'Vegetable'), ('Flower', 'Flower'), ('Herb', 'Herb')], max_length=100)),
                ('about', models.TextField()),
                ('used_for', models.CharField(max_length=255)),
                ('is_edible', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='plants/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Plants.plant')),
            ],
        ),
    ]
