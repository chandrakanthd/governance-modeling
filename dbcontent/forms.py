from django import forms

from app.models import Agent

class AgentForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ('name',)


#class ParameterValueForm(forms.ModelForm):

#    class Meta:
#        model = ParameterValue
#        fields = ('name', 'description', 'parameter',)
#
