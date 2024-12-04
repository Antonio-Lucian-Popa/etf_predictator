# Generated by Django 5.1.4 on 2024-12-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ETFData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('sma_20', models.FloatField(blank=True, null=True)),
                ('sma_50', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsSentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etf_symbol', models.CharField(max_length=10)),
                ('title', models.TextField()),
                ('sentiment', models.CharField(max_length=10)),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]