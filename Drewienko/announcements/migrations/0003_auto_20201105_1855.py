# Generated by Django 3.1.3 on 2020-11-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_auto_20201105_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(upload_to='announc_photos'),
        ),
    ]
