from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="diseases/images/")),
            ],
        ),
        migrations.CreateModel(
            name="Drug",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="drugs/images/")),
            ],
        ),
        migrations.CreateModel(
            name="RiskFactor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="risk_factors/images/")),
            ],
        ),
        migrations.CreateModel(
            name="Symptom",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="symptoms/images/")),
            ],
        ),
        migrations.AddField(
            model_name="symptom",
            name="diseases",
            field=models.ManyToManyField(blank=True, related_name="symptoms", to="wiki.disease"),
        ),
        migrations.AddField(
            model_name="riskfactor",
            name="diseases",
            field=models.ManyToManyField(blank=True, related_name="risk_factors", to="wiki.disease"),
        ),
        migrations.AddField(
            model_name="drug",
            name="diseases",
            field=models.ManyToManyField(blank=True, related_name="drugs", to="wiki.disease"),
        ),
    ]
