from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def npc_list(request):
    context = {
        "user_name": "young Padawan",
        "today": datetime.now(),
        "sponsor": True,
        "npc_count": 20,
        "list_of_npc": ['Gin', 'Ramirez', 'Crom', 'Ardevaas', 'Krunar']
    }

    return render(request, 'npc_list.html', context)

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