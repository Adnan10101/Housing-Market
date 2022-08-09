from copyreg import pickle
from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import attributesForm,userForm
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




def loginPage(request):
    user_form = userForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone_ = request.POST.get("phone_no")

        #print("email : ",phone_)

        try:
            user = userForm.objects.get(username = username)
        except:
            messages.error(request,"User does not exist")

        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect('/')
        

    context = {
        "user_form":user_form
    
    }
    return render(request,"base/user_page.html",context)

def logoutPage(request):
    logout(request)
    
    return redirect("/")

def register(request):
    context = {}
    return render(request,"base/register_page.html",context)


def home(request):
    form = attributesForm()
    #print(form)
    #user = User.objects.get(username = )
    
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