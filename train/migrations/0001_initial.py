# Generated by Django 5.0.3 on 2024-03-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=2000)),
                ('release', models.CharField(max_length=4)),
                ('cover', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=30)),
            ],
        ),
    ]
