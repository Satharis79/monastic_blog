# Generated by Django 4.0.5 on 2022-06-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_monk_userpic_alter_pictura_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monk',
            name='userpic',
            field=models.ImageField(default='media/img/undefined_monk.jpg', upload_to='media/img', verbose_name='Userpic'),
        ),
    ]
