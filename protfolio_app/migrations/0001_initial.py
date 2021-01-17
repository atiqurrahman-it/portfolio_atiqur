# Generated by Django 3.0.8 on 2020-12-02 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('address', models.TextField(max_length=600)),
                ('Date_of_birth', models.DateField()),
                ('Zip_code', models.IntegerField()),
                ('cv', models.FileField(blank=True, upload_to='')),
                ('total_project', models.IntegerField(blank=True)),
                ('Happy_Customers', models.IntegerField(blank=True, default=20)),
                ('total_Awards', models.IntegerField(blank=True, default=100)),
                ('project_pending', models.IntegerField(blank=True, default=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('Meassage', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavel', models.CharField(max_length=150)),
                ('campus_name', models.CharField(max_length=220)),
                ('year', models.CharField(max_length=10)),
                ('details', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer_Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('address', models.TextField(max_length=600)),
                ('fb_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Protfolio_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('details', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_name', models.CharField(blank=True, max_length=25)),
                ('Skill_Per', models.IntegerField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Protfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('details', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio_app.Protfolio_Category')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('details', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio_app.Category')),
            ],
        ),
    ]
