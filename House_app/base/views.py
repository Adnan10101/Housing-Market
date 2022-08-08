from copyreg import pickle
from django.shortcuts import render,redirect
from django.urls import is_valid_path
from .forms import attributesForm
import pickle
import numpy as np
import json

# Create your views here.


def get_model():
    with open("./pkl_files/model.pkl",'rb') as file:
        model = pickle.load(file)
    
    with open("./pkl_files/scaler.pkl","rb") as file:
        scale = pickle.load(file)
    
    return model,scale



def get_columns():
    with open("./base/columns/columns.json","r") as file:
        columns = json.load(file)
    
    return columns






def home(request):
    form = attributesForm()
    #print(form)
    
        
    context = {
        "form":form,
        }
    return render(request,"base/home.html",context)

def about(request):
    columns = get_columns()
    model,scale = get_model()

    form = attributesForm(request.POST)
    location = request.POST.get("location")
    area = request.POST.get("area_size")
    bed = request.POST.get("bed")
    bath = request.POST.get("bath")
    status = request.POST.get("status")
    builder = request.POST.get("builder")

    #print("aaaa :",status)

    def price_predict(location,area,bed,bath,status,builder):
        if location in columns:
            location_index = columns.index(location)
        else:
            location_index = 0

        if builder in columns:
            builder_index = columns.index(builder)
        else:
            builder_index = 0

        y_pred = np.zeros(len(columns))
        y_pred[0] = area
        y_pred[1] = bed
        y_pred[2] = bath
        y_pred[3] = status
        if location_index > 0:
            y_pred[location_index] = 1
        if builder_index > 0:
            y_pred[builder_index] = 1
        
        
        return model.predict(scale.transform([y_pred]))[0]


    res = round(price_predict(location,area,bed,bath,status,builder),2)
    
    

    context = {
        "form":form,
        "location":location,
        "area":area,
        "bed":bed,
        "bath":bath,
        "status":status,
        "predicted":res}

    return render(request,"base/home.html",context)