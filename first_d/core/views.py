from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from datetime import datetime
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'core/index.html')

def npc_list(request):

    my_list = ['Gin', 'Ramirez', 'Crom', 'Ardevaas', 'Krunar']

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
            messages.info(request, message="Thank you for contacting us!")
            return redirect(reverse("npc_list"))

    else:
        form = ContactForm()

    context = {
        "contact_form": form,
    }

    return render(request, "core/contact.html", context)
