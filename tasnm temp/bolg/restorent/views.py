from django.shortcuts import render,redirect
from restorent.models import BlogMOdel

# Create your views here.
def loadblog(request):
    try:
        return render(request,'add.html')
    except Exception as ex:
        print(ex)

def insertblog(request):
    try:
        blogMOdel=BlogMOdel()
        blogMOdel.name=request.POST["name"]
        blogMOdel.lastname=request.POST["lastname"]
        blogMOdel.contect=request.POST["contect"]

        blogMOdel.save()

        return redirect('/viewhere')
    except Exception as ex:
        pass

def viewdata(request):
    try:
        blogMOdel=BlogMOdel()
        blogList=blogMOdel.objects.all()
        print('::::::::::::::')
        return render(request,'viewBlog.html',{'blogList':blogList})
    except Exception as ex:
        pass