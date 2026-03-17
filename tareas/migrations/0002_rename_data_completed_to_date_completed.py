from django.db import migrations


def noop(apps, schema_editor):
    # This migration previously attempted to rename the completion field.
    # The database column is still called `data_completed`, but the model uses
    # `date_completed` with db_column='data_completed'.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(noop, reverse_code=noop),
    ]
