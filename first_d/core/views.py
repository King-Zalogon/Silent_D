from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from datetime import datetime
from .forms import ContactForm
from .models import Character


# Create your views here.
def index(request):
    return render(request,'core/index.html')

def npc_list(request):

    my_list = Character.objects.all()

    context = {
        "user_name": "young padawan",
        "today": datetime.now(),
        "sponsor": True,
        "npc_count": len(my_list),
        "list_of_npc": my_list,
    }

    return render(request, 'core/npc_list.html', context)

def npc_name(request, npc_name):
    return HttpResponse(
        f"""
        <h1> Welcome to {npc_name}'s place</h1>
        <p> This character's web page</p>
        """
    )

def birth_year(request, year):
    return HttpResponse(
        f"""
        <h1>The birth year was {datetime.year}</h1>
        """
    )

def contact(request):

    # print(request.POST)

    if request.method == "POST":
        form = ContactForm(request.POST)

        # Then I can validate the data
        if form.is_valid():
            # then we register the data
            messages.info(request, message="Thank you for your contribution!")

            char = Character(
                    name = form.cleaned_data["char_name"],
                    concept = form.cleaned_data["concept"],
                    # rules_system = form.cleaned_data["rules_system"],
                    growth = form.cleaned_data["growth"],
                    age = form.cleaned_data["age"],
                    # creator = form.cleaned_data["owner_name"],
                    is_player = form.cleaned_data["is_player"],
                    alive = form.cleaned_data["alive"],
                    bio = form.cleaned_data["bio"],
                    portrait = form.cleaned_data["portrait"]
                    )
            char.save()

            messages.info(request, message='Character registration was successful')

            return redirect(reverse("npc_list"))

    else:
        form = ContactForm()

    context = {
        "contact_form": form,
    }

    return render(request, "core/contact.html", context)
