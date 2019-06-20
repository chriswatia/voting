from django.shortcuts import render, redirect
from .models import Candidate, County, Category
from .forms import CountyForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        form = CountyForm(request.POST)
        if form.is_valid():
            return redirect('votes-index')
    form = CountyForm
    return render(request, 'votes/home.html', {'form': form})


def index(request):
    context = {
        'candidates': Candidate.objects.all()
    }
    return render(request, 'votes/index.html', context)


@login_required
def about(request):
    return render(request, 'votes/about.html')
