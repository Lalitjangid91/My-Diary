from django.shortcuts import render,redirect
from .forms import *
from .models import *

def Home(request):
    d=Diary.objects.order_by('Date')
    if d:
        d=d.reverse()
    return render(request,'MyDiary/Home.html',{'list_data':d})
def delete(request):
    d=Diary.objects.all()
    for data in d:
        try:
            request.POST[str(data.DATE)]
            break
        except:
            pass
    data.delete()
    return redirect('home')
def Index(request):
    form=DiaryForm()
    if request.method=='POST':
        form=DiaryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request,'MyDiary/Index.html',{'form':form})
def Update(request,date):
    obj=Diary.objects.get(Date=date)
    t=obj.Text
    form=DiaryForm(initial={'Text':t})
    obj.delete()
    return render(request,'MyDiary/Index.html',{'form':form})

def DeleteAll(request):
    Diary.objects.all().delete()
    return redirect('home')
