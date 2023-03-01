# Generated by Django 4.1.4 on 2022-12-18 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_bid_accepted_alter_seller_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='api.competition'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_seller', to='api.seller'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_buyer', to='api.buyer'),
        ),
    ]
