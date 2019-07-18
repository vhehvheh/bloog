# Generated by Django 2.2.3 on 2019-07-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('contents', models.TextField()),
                ('Lookup', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Code',
        ),
    ]
