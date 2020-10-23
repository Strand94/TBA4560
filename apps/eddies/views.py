from django.shortcuts import render
from .forms import SearchAreaForm
#from apps.eddies.models import MODEL
from datetime import datetime


def eddies(request):
    print(str(datetime.now()))
    if request.method == 'POST':
        form = SearchAreaForm(request.POST)
        if form.is_valid():
            NW_corner = form.cleaned_data['north_west_lat']




            print(form.cleaned_data['north_west_lat'])

            pass  # does nothing, just trigger the validation
    else:
        form = SearchAreaForm()
    return render(request, "eddies/eddies.html", {'form': form})
