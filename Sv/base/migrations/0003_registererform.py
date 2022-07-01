# Generated by Django 4.0.4 on 2022-05-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='registererForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('schedule', models.CharField(max_length=20)),
            ],
        ),
    ]