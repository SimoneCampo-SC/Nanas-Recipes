from django.db import migrations


def seed_categories(apps, schema_editor):
    Category = apps.get_model("recipes", "Category")

    for name in ["Sides", "Main Course", "Desserts"]:
        Category.objects.get_or_create(name=name)


def remove_seeded_categories(apps, schema_editor):
    Category = apps.get_model("recipes", "Category")
    Category.objects.filter(
        name__in=["Sides", "Main Course", "Desserts"]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0007_alter_saved_recipe"),
    ]

    operations = [
        migrations.RunPython(
            seed_categories,
            remove_seeded_categories,
        ),
    ]
