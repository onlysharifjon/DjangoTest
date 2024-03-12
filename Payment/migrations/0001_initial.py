# Generated by Django 4.2.10 on 2024-03-12 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(unique=True)),
                ('expired_date', models.DateField()),
                ('card_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.foydalanuvchilar')),
            ],
        ),
    ]
