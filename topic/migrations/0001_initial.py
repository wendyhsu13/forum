# Generated by Django 4.0 on 2022-01-01 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='討論主題')),
                ('content', models.TextField(verbose_name='內文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('replied', models.DateTimeField(blank=True, null=True, verbose_name='回覆時間')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
