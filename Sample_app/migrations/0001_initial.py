# Generated by Django 3.0.7 on 2020-09-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('contact', models.CharField(default='', max_length=70)),
                ('Query', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
