# Generated by Django 4.2.4 on 2023-09-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_author_reader_rename_student_id_issuedbook_reader_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='full_name',
        ),
        migrations.AddField(
            model_name='reader',
            name='first_name',
            field=models.CharField(default=1, max_length=256, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='last_name',
            field=models.CharField(default=1, max_length=256, verbose_name='Last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='patronymic',
            field=models.CharField(default=1, max_length=256, verbose_name='Patronymic'),
            preserve_default=False,
        ),
    ]
