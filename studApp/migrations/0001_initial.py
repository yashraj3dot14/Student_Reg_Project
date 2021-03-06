# Generated by Django 4.0 on 2022-01-08 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('classdetail', models.CharField(max_length=10)),
                ('school', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('biology', models.IntegerField()),
                ('english', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentAcademic', to='studApp.studentinfo')),
            ],
        ),
    ]
