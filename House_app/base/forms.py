from django import forms
import json
from .models import UserModel
from django.forms import ModelForm


def get_locIndex():
    with open("./base/columns/location.json","r") as file:
        location_list = json.load(file)
    
    return location_list

def get_builderIndex():
    with open("./base/columns/builder.json","r") as file:
        builder_list = json.load(file)
    
    return builder_list

loc_index = get_locIndex()
build_index = get_builderIndex()
display_choice = ((0,"Ready To move in"),(1,"Under Construction"))

class attributesForm(forms.Form):
    location = forms.ChoiceField(choices = [(i,i) for i in loc_index])
    area_size = forms.FloatField()
    bed = forms.IntegerField()
    bath = forms.IntegerField()
    status = forms.ChoiceField(widget = forms.RadioSelect,choices = display_choice)
    builder = forms.ChoiceField(choices = [(i,i) for i in build_index])


class userForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"