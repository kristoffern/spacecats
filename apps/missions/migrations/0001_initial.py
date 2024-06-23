# Generated by Django 4.2.13 on 2024-06-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spacecats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('launch_date', models.DateField()),
                ('spacecats', models.ManyToManyField(related_name='missions', to='spacecats.spacecat')),
            ],
        ),
    ]