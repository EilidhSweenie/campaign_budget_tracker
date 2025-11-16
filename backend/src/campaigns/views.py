from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Campaign
from .forms import CampaignForm

def index(request):
    return HttpResponse("Add Campaign Index")

def add_new_campaign(request):
    if request.method == "POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view")
    else:
        form = CampaignForm()

    return render(request, "campaigns/add_campaign.html", {"form": form})

def view_all_campaigns(request):
    try:
        all_campaigns = Campaign.objects.all().values("id", "name", "budget", "spend", "status")
        return JsonResponse(list(all_campaigns), safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": "Could not fetch campaigns"},
            status=500,
        ) 
