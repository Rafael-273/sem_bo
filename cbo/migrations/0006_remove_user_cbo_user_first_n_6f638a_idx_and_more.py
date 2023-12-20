# Generated by Django 4.2.6 on 2023-12-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbo', '0005_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='user',
            name='cbo_user_first_n_6f638a_idx',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='CRM',
            new_name='occupational_registration',
        ),
        migrations.RemoveField(
            model_name='user',
            name='specialty',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name', 'occupational_registration'], name='cbo_user_first_n_b90126_idx'),
        ),
    ]