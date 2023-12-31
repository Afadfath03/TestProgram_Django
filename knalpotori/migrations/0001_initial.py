# Generated by Django 4.2.2 on 2023-07-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Pengguna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('wa', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('imae', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(blank=True, default='pelanggan', max_length=10, null=True)),
                ('status', models.CharField(blank=True, default='active', max_length=10, null=True)),
            ],
        ),
    ]
