# Generated by Django 4.2.4 on 2023-08-31 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0004_remove_book_status_book_isbn_delete_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='reader',
            new_name='reader_name',
        ),
        migrations.AddField(
            model_name='reader',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
