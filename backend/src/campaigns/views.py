import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Campaign
from .forms import CampaignForm

def index(request):
    return HttpResponse("Add Campaign Index")

@csrf_exempt
def add_new_campaign(request):
    form = CampaignForm()
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        form = CampaignForm(data)
        if form.is_valid():
            campaign = form.save()
            return JsonResponse({
                "id": campaign.id,
                "name": campaign.name,
                "budget": campaign.budget,
                "spend": campaign.spend,
                "status": campaign.status
            })
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def view_all_campaigns(request):
    try:
        all_campaigns = Campaign.objects.all().values("id", "name", "budget", "spend", "status")
        return JsonResponse(list(all_campaigns), safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": "Could not fetch campaigns"},
            status=500,
        ) 
