# Generated by Django 3.2.3 on 2021-06-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20210606_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='recipe',
            field=models.ManyToManyField(blank=True, related_name='saved', to='recipes.Recipe'),
        ),
    ]
