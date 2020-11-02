from django.shortcuts import render
from .forms import SearchAreaForm
from pydap.client import open_url
import numpy as np
from datetime import timedelta
from .cygnss.opendap import generate_url


def eddies(request):
    if request.method == 'POST':
        form = SearchAreaForm(request.POST)
        if form.is_valid():
            # Collect and order datetime objects.
            coordinate_a = form.cleaned_data['coordinate_a']
            coordinate_b = form.cleaned_data['coordinate_b']
            latitudes = [coordinate_a.split(",")[0],coordinate_b.split(",")[0]]
            longitudes = [coordinate_a.split(",")[1],coordinate_b.split(",")[1]]
            print(latitudes)
            print(longitudes)

            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            grid = form.cleaned_data['grid']
            selected_dates = [start + timedelta(days=x) for x in range(0, (end.date() - start.date()).days)]
            selected_dates.append(end)

            for date in selected_dates:
                for satellite_number in range(1, 9):
                    url = generate_url(date, satellite_number)

    else:
        form = SearchAreaForm()
    return render(request, "eddies/eddies.html", {'form': form})



