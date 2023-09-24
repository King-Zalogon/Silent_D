from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Dhello Dworld!</h1>')

def sub_url(request):
    return HttpResponse("""
                        <ul>
                            <li> I'm </li>
                            <li> a sub </li>
                            <li> url </li>
                        </ul>
                        """)
