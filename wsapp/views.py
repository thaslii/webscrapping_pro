from django.shortcuts import render,HttpResponseRedirect
from .models import Link
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    if request.method=='POST':
        link_new=request.POST.get('page','')
        urls=requests.get("https://www.zomato.com/")
        b=BeautifulSoup(urls.text,'html.parser')

        for link in b.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Link.objects.create(address=li_address,string_name=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values=Link.objects.all()
    return render(request,'home.html',{'data_values':data_values})