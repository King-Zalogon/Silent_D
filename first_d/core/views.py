from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from datetime import datetime
from .forms import CharacterResgister, RulesRegisterModelForm
from .models import Character, RulesSystem


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
        form = CharacterResgister(request.POST)

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
        form = CharacterResgister()

    context = {
        "char_form": form,
    }

    return render(request, "core/char_form.html", context)


class RulesSystemCreateView(CreateView):
    model = RulesSystem
    context_object_name = 'rules_systems_form'
    template_name = 'core/rules_systems_form.html'
    success_url = 'rules_systems_list'
    form_class = RulesRegisterModelForm
    # fields = '__all__'


class RulesSystemListView(ListView):
    model = RulesSystem
    context_object_name = "rules_systems_list"
    template_name = 'core/rules_systems_list.html'
    ordering = ['system_name']
    systems_count = ListView.__sizeof__

