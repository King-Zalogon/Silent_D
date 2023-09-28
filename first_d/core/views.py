from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
    context = {

    }

    return render(request, "core/contact.html", context)
