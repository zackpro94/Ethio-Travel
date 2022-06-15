# Generated by Django 3.2.8 on 2021-10-25 09:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ethiotravel', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='best_tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='null', upload_to='')),
            ],
        ),
    ]
