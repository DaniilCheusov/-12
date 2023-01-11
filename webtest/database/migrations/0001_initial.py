# Generated by Django 4.1.2 on 2022-11-21 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('Hall_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Hall_Name', models.CharField(blank=True, default=' ', max_length=10, null=True, unique=True, verbose_name='Назавние зала')),
                ('Price_Weekdays_8_17', models.PositiveSmallIntegerField(verbose_name='Стоимость 1 часа с 8 до 17')),
                ('Price_Weekdays_17_8', models.PositiveSmallIntegerField(verbose_name='Стоимость 1 часа с 17 до 8')),
                ('Price_Weekends_8_17', models.PositiveSmallIntegerField(verbose_name='Стоимость 1 часа с 8 до 17')),
                ('Price_Weekends_17_8', models.PositiveSmallIntegerField(verbose_name='Стоимость 1 часа с 17 до 8')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Client_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=20, verbose_name='Имя')),
                ('Mid_Name', models.CharField(max_length=20, verbose_name='Отчество')),
                ('Number', models.CharField(max_length=10, verbose_name='номер телефона')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Date', models.DateTimeField(null=True, verbose_name='Дата и время бронирования')),
                ('Time_range', models.CharField(max_length=2, null=True, verbose_name='Время аренды в часах')),
                ('Status', models.BooleanField(null=True, verbose_name='Status')),
                ('Type_of_Service', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.halls')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]