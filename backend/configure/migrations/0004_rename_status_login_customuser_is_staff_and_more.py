# Generated by Django 5.0.4 on 2024-05-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0003_remove_customuser_groups_remove_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='status_login',
            new_name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='session_timeout',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
