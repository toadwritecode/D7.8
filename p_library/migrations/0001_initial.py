# Generated by Django 3.1.1 on 2020-09-23 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('birth_year', models.PositiveSmallIntegerField(verbose_name='Год рождения')),
                ('country', models.CharField(max_length=2, verbose_name='Страна')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('address', models.TextField(verbose_name='Физический адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('address', models.TextField(verbose_name='Физический адрес')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, verbose_name='Международный стандартный книжный номер')),
                ('title', models.CharField(max_length=128, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Аннотация')),
                ('year_release', models.PositiveSmallIntegerField(verbose_name='Год издания')),
                ('copy_count', models.PositiveSmallIntegerField(default=1, verbose_name='Число копий в библиотеке')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, upload_to='media/books_photo', verbose_name='Фото')),
                ('authors', models.ManyToManyField(blank=True, related_name='book_author', to='p_library.Author', verbose_name='Автор')),
                ('friend', models.ManyToManyField(blank=True, related_name='book_friend', to='p_library.Friend', verbose_name='Кто из друзей читает')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_publisher', to='p_library.publisher', verbose_name='Издательство')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
