

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MetaD', '0002_uploadedfiles_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfiles',
            old_name='filesUpload',
            new_name='files_Upload',
        ),
    ]
