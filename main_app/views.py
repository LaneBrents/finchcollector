from django.shortcuts import render, redirect

# Import our model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# Create your views here
from django.http import HttpResponse

from .forms import FeedingForm
# Add the class of finch


# Define the home view
def home(request):
    return HttpResponse('HELLOOOOO')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    # Exclude the name from update
    fields = ['breed', 'description', 'age']
    success_url = '/finches/'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/' 

def add_feeding(request, finch_id):
    # we need to create a modelForm instance using the data from request.POST 
    form = FeedingForm(request.POST)
    # validate the form, so make sure the inputs are of the correct type and shape
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = finch_id
        new_feeding.save() 
    return redirect('detail', finch_id=finch_id)
