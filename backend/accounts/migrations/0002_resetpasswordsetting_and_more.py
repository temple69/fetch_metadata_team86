# Generated by Django 4.0.6 on 2022-08-04 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPasswordSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm_password_url', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'ResetPassword Settings',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_pics',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
