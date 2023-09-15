from django.shortcuts import render,redirect
from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task2'
class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'
class taskupdateview(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url= reverse_lazy('cbvhome')



def index(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority,date=date)
        task1.save()
    return render(request, 'home.html',{'task2':task2})
#def detail(request):


    #return render(request,'detail.html',{'task':task1})
def delete(request,taskid):
    task3=task.objects.get(id=taskid)
    if request.method=='POST':
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,taskid):
    task4=task.objects.get(id=taskid)
    f=todoform(request.POST or None,instance=task4)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
