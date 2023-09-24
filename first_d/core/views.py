from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def sub_url(request):
    return HttpResponse("""
                        <ul>
                            <li> I'm </li>
                            <li> a sub </li>
                            <li> url </li>
                        </ul>
                        """)

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
        <h1>The birth year was {year}</h1>
        """
    )