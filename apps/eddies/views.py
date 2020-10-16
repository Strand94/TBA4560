from django.shortcuts import render
from .forms import SearchAreaForm
#from apps.eddies.models import MODEL


def eddies(request):
    if request.method == 'POST':
        form = SearchAreaForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SearchAreaForm()
    return render(request, "eddies/eddies.html", {'form': form})
