from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import JobForm
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs':jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    
    return render(request, 'create.html', {'form': form})
