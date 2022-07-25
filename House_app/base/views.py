from django.shortcuts import render
import pickle

#with open(r"Housing Market\\model\\model.pkl","rb") as file:
#    model = pickle.load(file)

with open("./House_app/templates/main.html") as file:

    a = file.read()
    print(a)


def home(request):
    return render(request,"base/home.html")