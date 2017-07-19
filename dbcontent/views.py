from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext, loader
from datetime import datetime
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from app.models import ProcessItem, Agent, Process, ItemRoles, ProjectParameter, ParameterValue, ProjectRequirement, ProjectRequirementCondition
from .forms import AgentForm


def brief(request):
    return render(request, 'dbcontent/brief.html')


#List of classes for Database Contents View Forms

class ProcessItemView(generic.ListView):
    template_name = 'dbcontent/ProcessItemList.html'

    def get_queryset(self):
        return ProcessItem.objects.all()


#class AgentView(generic.ListView):
#    template_name = 'dbcontent/AgentList.html'
#
#    def get_queryset(self):
#        return Agent.objects.all()

def agent_list(request):
    posts = Agent.objects.all()
    return render(request, 'dbcontent/AgentList.html', {'posts':posts})



class ProcessView(generic.ListView):
    template_name = 'dbcontent/ProcessList.html'

    def get_queryset(self):
        return Process.objects.all()


class ItemRolesView(generic.ListView):
    template_name = 'dbcontent/ItemRolesList.html'

    def get_queryset(self):
        return ItemRoles.objects.all()

class ProjectParameterView(generic.ListView):
    template_name = 'dbcontent/ProjectParameterList.html'

    def get_queryset(self):
        return ProjectParameter.objects.all()


class ParameterValueView(generic.ListView):
    template_name = 'dbcontent/ParameterValueList.html'

    def get_queryset(self):
        return ParameterValue.objects.all()


class ProjectRequirementView(generic.ListView):
    template_name = 'dbcontent/ProjectRequirementList.html'

    def get_queryset(self):
        return ProjectRequirement.objects.all()


class ProjectRequirementConditionView(generic.ListView):
    template_name = 'dbcontent/ProjectRequirementConditionList.html'

    def get_queryset(self):
        return ProjectRequirementCondition.objects.all()


#Create new data and add it to the database

class ProcessItemCreate(CreateView):
    model = ProcessItem
    fields = ['name', 'description']
    template_name = 'dbcontent/processitem_form.html'


#class AgentCreate(CreateView):
#    model = Agent
#    fields = ['name']
#    template_name = 'dbcontent/agent_form.html'

def agent_new(request):
    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('agent_list')
    else:
        form = AgentForm()
    return render(request, 'dbcontent/agent_form.html', {'form':form})

def agent_edit(request, pk):
    post = get_object_or_404(Agent, pk=pk)
    if request.method == "POST":
        form = AgentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('agent_list')
    else:
        form = AgentForm(instance=post)
    return render(request, 'dbcontent/agent_form.html', {'form':form})

def agent_remove(request, pk):
    post = get_object_or_404(Agent, pk=pk)
    post.delete()
    return redirect('agent_list')



class ProcessCreate(CreateView):
    model = Process
    fields = ['name', 'description', 'agent', 'condition_items', 'prevent_items', 'result_items']
    template_name = 'dbcontent/process_form.html'

class ProjectParameterCreate(CreateView):
    model = ProjectParameter
    fields = ['name', 'description', 'type']
    template_name = 'dbcontent/projectparameter_form.html'

class ParameterValueCreate(CreateView):
    model = ParameterValue
    fields = ['name', 'description', 'parameter']
    template_name = 'dbcontent/parametervalue_form.html'

class ProjectRequirementCreate(CreateView):
    model = ProjectRequirement
    fields = ['name', 'description', 'condition_items', 'prevent_items', 'introduced_items']
    template_name = 'dbcontent/projectrequirement_form.html'

class ProjectRequirementConditionCreate(CreateView):
    model = ProjectRequirementCondition
    fields = ['name', 'requirement', 'condition_parameter', 'allowed_values', 'custom_value']
    template_name = 'dbcontent/projectrequirementcondition_form.html'
