# Create your views here.

from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborrate_form.is_valid():
            collaborate_form.save()
            messages.add_messages(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days")

    about = About.objects.all().order_by('-updated_on').first() 
    collaborate_form = CollaborateForm(data=request.POST)

    return render(
        request,
        "about/about.html",
        {
            "about": about, "collaborate_form": collaborate_form
        },
    )