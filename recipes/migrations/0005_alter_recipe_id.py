# Generated by Django 3.2.3 on 2021-06-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]