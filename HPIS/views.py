from django.shortcuts import render, reverse
from .forms import MyForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import os
from django.conf import settings

file_ = open(os.path.join(settings.BASE_DIR, 'hp_columns.csv'))
file_ = open(os.path.join(settings.BASE_DIR, 'model_eighty_joblib.pkl'))
file_ = open(os.path.join(settings.BASE_DIR, 'scaler_X.pkl'))
file_ = open(os.path.join(settings.BASE_DIR, 'scaler_Y.pkl'))
sc_X = joblib.load('scaler_X.pkl')
sc_Y = joblib.load('scaler_Y.pkl')
df3=pd.read_csv('hp_columns.csv')

def home(request): # the function will take request as input
    return render(request, 'index.html')

def parameters(request):
    print("request came to views")
    #submitbutton = request.POST.get("submit")
    if request.method == "POST":
        #form = MyForm(request.POST)
        #print(form.is_valid())
        #if form.is_valid():
        area_type =  request.POST.get("area_type")
        loc =        request.POST.get("location")
        bedrms =     request.POST.get("bedrooms")
        hallkitchen =request.POST.get("hallkitchen")
        areasqft =   request.POST.get("area_sqft")
        bathrms =    request.POST.get("bathrooms")
        balcns =     request.POST.get("balconies")            
        df3.loc[0]=np.zeros(1314)
        df3.loc[0]["bath"]=bathrms
        df3.loc[0]["balcony"]=balcns
        df3.loc[0]["location_ "+loc]=1
        df3.loc[0]["location_"+loc]=1
        df3.loc[0]["area_type_"+area_type]=1
        df3.loc[0]["new_size"]=bedrms
        df3.loc[0]["HK"]=hallkitchen
        df3.loc[0]["new_sqft"]=areasqft	
        clf=joblib.load('model_eighty_joblib.pkl')
        y_predict=sc_Y.inverse_transform(clf.predict(sc_X.transform(np.array(df3))))
        return HttpResponse(y_predict)


 # def parameters(request):
 #    context = {}
 #    if request.method == "POST":
 #        form = ParameterForm(request.POST)
 #        context['form'] = form
 #        if form.is_valid():
 #        	f = form.save()
 #        	return HttpResponseRedirect(reverse('home'))
 #        else:
 #        	return render(request, 'index.html', context)
 #    else:
 #        form = ParameterForm()
 #        context['form'] = form
 #        return render(request, 'index.html', context)        
 #       