from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404, HttpResponse ,HttpResponseRedirect,redirect
from .form import Loform
from .models import Document

def register(request):
    if request.method == "POST":
        form  = Loform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dataFetch)
            #return HttpResponse("re")
        else:
            return HttpResponse("no er")
    else:
        form = Loform()
        return render(request,'editor.html',{'form1':form})

# def noteSave(request):
#     if request.method == "POST":
#         if request.POST.get('title') and request.POST.get('content'):
#             post = Document()
#             post.title  = request.POST.get('title')
#             post.content = request.POST.get('content')
#             post.save()
#             return  HttpResponse ("Data add")
#         else:
#             return  HttpResponse("data not add")
#     else :
#         return render(request, 'editor.html', {})

def dataFetch(request):
    obj = Document.objects.all()
    data = {'id':obj}
    return render(request , 'showData.html',data)


def Delete(request,id):
    d = Document.objects.get(id=id)
    d.delete()
    return redirect('/dataFetch')

def Edit(request,id):
    obj = Document.objects.get(id=id)
    return render(request , 'txt.html',{'obj':obj})

def update(request,id):
    obj = Document.objects.get(id=id)
    form = Loform(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/dataFetch')
    return render(request,'txt.html',{'obj':obj})

