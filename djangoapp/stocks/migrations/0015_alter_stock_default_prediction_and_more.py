# Generated by Django 4.1 on 2024-06-29 02:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0014_stock_default_prediction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="default_prediction",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Quant PD (%)",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="eps_estimate_y10_analysis",
            field=tinymce.models.HTMLField(
                blank=True, null=True, verbose_name="LLM EPS EST Y10"
            ),
        ),
    ]
