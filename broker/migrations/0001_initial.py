# Generated by Django 2.1.7 on 2019-04-03 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('bath', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('area_sqft', models.FloatField()),
                ('area_type', models.CharField(max_length=100)),
                ('hk', models.IntegerField()),
                ('location', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('br', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='adv',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advs', to='broker.Broker'),
        ),
    ]