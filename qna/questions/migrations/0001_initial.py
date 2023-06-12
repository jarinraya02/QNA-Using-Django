# Generated by Django 4.1.2 on 2022-10-16 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('Q_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=50)),
                ('U_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ouruser')),
            ],
        ),
    ]
