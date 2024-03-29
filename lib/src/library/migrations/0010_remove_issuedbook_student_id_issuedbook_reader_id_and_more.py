# Generated by Django 4.2.4 on 2023-09-03 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0009_issuedbook_reader_remove_book_is_taken_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='student_id',
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='reader_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reader name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='reader',
            name='full_name',
            field=models.CharField(max_length=256, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=models.CharField(blank=True, max_length=32, verbose_name='Phone Num'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
