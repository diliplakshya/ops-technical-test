# Generated by Django 2.1.7 on 2019-03-28 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technicaltest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplicationMetaData',
            new_name='MetaDataEndPoint',
        ),
        migrations.RenameModel(
            old_name='TechnicalTest',
            new_name='RootEndPoint',
        ),
    ]
