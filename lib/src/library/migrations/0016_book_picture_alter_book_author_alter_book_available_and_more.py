# Generated by Django 4.2.4 on 2023-09-04 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_rename_last_name_reader_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(default=1, upload_to='uploads/%Y/%m/%d/', verbose_name='Картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reader',
            name='full_name',
            field=models.CharField(max_length=256, verbose_name='Full name'),
        ),
    ]
