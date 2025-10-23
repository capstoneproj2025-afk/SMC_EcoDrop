# Generated migration to rename student_id field to school_id
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rewarditem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='student_id',
            new_name='school_id',
        ),
    ]
