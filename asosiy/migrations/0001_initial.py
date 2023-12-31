# Generated by Django 4.2.5 on 2023-10-06 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('janr', models.CharField(max_length=30)),
                ('sahifa', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('ish_vaqti', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
                ('kitoblar_soni', models.PositiveSmallIntegerField()),
                ('tugilgan_yil', models.DateField(blank=True, null=True)),
                ('tirik', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('kurs', models.PositiveSmallIntegerField()),
                ('kitoblar_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField(auto_now_add=True)),
                ('qaytarish_sana', models.DateField(blank=True, null=True)),
                ('qaytardi', models.BooleanField(default=False)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kutubxonachi')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
        ),
    ]
