"""
Definition of views.
"""
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import login, authenticate
from datetime import datetime
from app.forms import ExecuteForm, UserForm
from app.dss import retrieve_governance_processes, governance_tree_builder
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import ProcessItem, Agent, Process, ItemRoles, ProjectParameter, ParameterValue, ProjectRequirement, ProjectRequirementCondition


def index(request):
    return render(request, 'app/initial.html')

def item(request):
    return render(request, 'app/structure.html')

def functionalities(request):
    return render(request, 'app/functionalities.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = ExecuteForm(request.POST)
        if form.is_valid():
            param_values = form.param_values()
            active_requirements = retrieve_governance_processes.get_active_requirements(param_values)
            req_items = retrieve_governance_processes.get_requirement_items(active_requirements)

            tb = governance_tree_builder.GovernanceTreeBuilder()
            tree_string = tb.pretty_print_items_support([i.id for i in req_items["condition_items"]])
            return render(request, 'app/index.html', {'title':'Result ', "tree_string": tree_string})

    else:
        form = ExecuteForm()

    return render(request, 'app/index.html', {'title':'Home ', "execute_form": form})


def test(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/test.html',
        {
            'title':'Test'
        }
    )


class UserFormView(View):
    form_class = UserForm
    template_name = 'app/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form':form})
