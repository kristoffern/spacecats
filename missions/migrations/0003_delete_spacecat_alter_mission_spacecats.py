# Generated by Django 4.2.13 on 2024-06-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacecats', '0001_initial'),
        ('missions', '0002_migrate_spacecat_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpaceCat',
        ),
        migrations.AlterField(
            model_name='mission',
            name='spacecats',
            field=models.ManyToManyField(related_name='missions', to='spacecats.spacecat'),
        ),
    ]
