# Generated by Django 4.0.6 on 2024-08-05 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_remove_sipflatfile_custom_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='sip_flat_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.sipflatfile'),
        ),
    ]
