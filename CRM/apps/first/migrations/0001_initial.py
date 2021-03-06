# Generated by Django 3.1 on 2020-08-16 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication', models.CharField(max_length=25, verbose_name='Канала обращения')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('e_mail', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Descriptin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100, verbose_name='Название компании')),
                ('name_manager', models.CharField(max_length=100, verbose_name='ФИО руководителя')),
                ('crt_date', models.DateField(auto_now_add=True, verbose_name='Дата создание')),
                ('date_record', models.DateField(auto_now=True, verbose_name='Дата изменения записи')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.companyaddress')),
                ('description_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.descriptin')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('start_date', models.DateField(verbose_name='Сроки начала')),
                ('deadline', models.DateField(verbose_name='Срок окончания')),
                ('cost', models.FloatField(verbose_name='Стоимость')),
                ('status', models.BooleanField(verbose_name='Статус')),
                ('description_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first.descriptin')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_manager', models.CharField(max_length=255, verbose_name='Имя менеджера')),
                ('appraisal', models.PositiveSmallIntegerField(default=0, verbose_name='Оценка')),
                ('communication_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first.communication')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.record')),
                ('description_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first.descriptin')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.project')),
            ],
            options={
                'verbose_name': 'Взаимодействия',
                'verbose_name_plural': 'Взаимодействия',
            },
        ),
    ]
