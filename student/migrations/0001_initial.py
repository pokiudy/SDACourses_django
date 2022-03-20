# Generated by Django 4.0.3 on 2022-03-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('is_olympic', models.BooleanField(default=False)),
                ('email_field', models.EmailField(max_length=40)),
                ('description', models.TextField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('average', models.FloatField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
