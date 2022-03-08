# Generated by Django 3.2.9 on 2021-12-05 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluationAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('brach_manager', models.CharField(max_length=50)),
                ('branch_address', models.CharField(max_length=50)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_branch', to='EvaluationAPI.restaurant')),
            ],
        ),
    ]
