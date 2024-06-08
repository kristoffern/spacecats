from django.db import migrations

def copy_spacecat_data(apps, schema_editor):
    OldSpaceCat = apps.get_model('missions', 'SpaceCat')
    NewSpaceCat = apps.get_model('spacecats', 'SpaceCat')

    for old_spacecat in OldSpaceCat.objects.all():
        NewSpaceCat.objects.create(
            id=old_spacecat.id,
            name=old_spacecat.name,
            age=old_spacecat.age,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('spacecats', '0001_initial'),
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_spacecat_data),
    ]
