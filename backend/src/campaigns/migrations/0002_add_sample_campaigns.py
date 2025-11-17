from django.db import migrations

def add_sample_campaigns(apps, schema_editor):
    Campaign = apps.get_model("campaigns", "Campaign")
    if Campaign.objects.exists():
        return
    Campaign.objects.create(name="Account A", budget=1000, spend=50, status="IN_BUDGET")
    Campaign.objects.create(name="Account B", budget=500, spend=300, status="WARNING")
    Campaign.objects.create(name="Account C", budget=100, spend=150, status="OUT_OF_BUDGET")

def remove_sample_campaigns(apps, schema_editor):
    Campaign = apps.get_model("campaigns", "Campaign")
    Campaign.objects.filter(name__in=["Account A", "Account B", "Account C"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_campaigns, remove_sample_campaigns),
    ]
