from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html', context=None)

class TestPage(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'test.html',context=None)

class AboutPageView(TemplateView):
    template_name = "test.html"