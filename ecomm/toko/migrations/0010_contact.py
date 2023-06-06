# Generated by Django 4.2 on 2023-06-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0009_produkitem_addonsgambardua_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subjek', models.CharField(max_length=100)),
                ('pesan', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]