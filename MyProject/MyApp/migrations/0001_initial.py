# Generated by Django 4.1.2 on 2022-10-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_username', models.CharField(max_length=122)),
                ('student_email', models.EmailField(max_length=122)),
                ('Std', models.IntegerField()),
                ('Roll_number', models.IntegerField()),
                ('School_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=60)),
                ('Application_num', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Pending', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_Registraion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('password', models.CharField(max_length=40)),
                ('password1', models.CharField(max_length=40)),
                ('profile', models.CharField(max_length=40)),
            ],
        ),
    ]
