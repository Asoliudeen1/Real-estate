# Generated by Django 4.1.2 on 2022-10-12 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtor.realtor'),
        ),
        migrations.DeleteModel(
            name='Realtor',
        ),
    ]