# Generated by Django 4.2.7 on 2023-12-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='sarlavha kriting', max_length=250)),
                ('body', models.TextField(help_text=' text kiriting')),
            ],
        ),
    ]
