# Generated by Django 5.0.3 on 2024-04-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaytacaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='gmap_business_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='landmark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='last_transaction_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='receiving_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='receiving_pubkey',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
