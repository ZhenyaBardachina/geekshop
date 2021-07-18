# Generated by Django 3.2 on 2021-06-25 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_shopuserprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]