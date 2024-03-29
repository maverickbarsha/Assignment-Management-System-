# Generated by Django 2.2.7 on 2019-12-11 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upload', models.FileField(blank=True, default='No file uploaded', null=True, upload_to='assignments/')),
                ('due_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('course_code', models.CharField(max_length=8)),
                ('course_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('teacher', models.BooleanField(default=True)),
                ('student', models.BooleanField(default=False)),
                ('college_name', models.CharField(blank=True, max_length=225, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='No description', max_length=100, null=True)),
                ('upload', models.FileField(blank=True, upload_to='submissions/')),
                ('submitted_at', models.DateField(default=None)),
                ('last_updated', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='student.Assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='student.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='student.MyUser'),
        ),
    ]
