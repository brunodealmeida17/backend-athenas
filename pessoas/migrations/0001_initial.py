# Generated by Django 5.1.6 on 2025-02-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
            ],
        ),
    ]
