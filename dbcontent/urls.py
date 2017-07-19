from django.conf.urls import  url
from . import views

urlpatterns = [

    url(r'^brief/$', views.brief, name='brief'),

	#/tree
    url(r'^Process_Items/list/$', views.ProcessItemView.as_view(), name='Process_Items/list'),
    url(r'^Agents/list/$', views.agent_list, name='agent_list'),
    url(r'^Processes/list/$', views.ProcessView.as_view(), name='Processes/list'),
    #url(r'^Item_Roles/list/$', views.ItemRolesView.as_view(), name='Item_Roles/list'),
    url(r'^Project_Parameters/list/$', views.ProjectParameterView.as_view(), name='Project_Parameters/list'),
    url(r'^Parameter_Values/list/$', views.ParameterValueView.as_view(), name='Parameter_Values/list'),
    url(r'^Project_Requirements/list/$', views.ProjectRequirementView.as_view(), name='Project_Requirements/list'),
    url(r'^Project_Requirement_Conditions/list/$', views.ProjectRequirementConditionView.as_view(), name='Project_Requirement_Conditions/list'),



    url(r'^Process_Items/add/$', views.ProcessItemCreate.as_view(), name='Process_Items/add'),
    url(r'^Agents/add/$', views.agent_new, name='agent_new'),
    url(r'^Processes/add/$', views.ProcessCreate.as_view(), name='Processes/add'),
    url(r'^Project_Parameters/add/$', views.ProjectParameterCreate.as_view(), name='Project_Parameters/add'),
    url(r'^Parameter_Values/add/$', views.ParameterValueCreate.as_view(), name='Parameter_Values/add'),
    url(r'^Project_Requirements/add/$', views.ProjectRequirementCreate.as_view(), name='Project_Requirements/add'),
    url(r'^Project_Requirement_Conditions/add/$', views.ProjectRequirementConditionCreate.as_view(), name='Project_Requirement_Conditions/add'),

    url(r'^Agents/(?P<pk>\d+)/edit/$', views.agent_edit, name='agent_edit'),

    url(r'^Agents/(?P<pk>\d+)/remove/$', views.agent_remove, name='agent_remove')

    ]
