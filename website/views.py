from django.shortcuts import render, redirect
from .forms import FeedbackForm

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})
# Create your views here.
