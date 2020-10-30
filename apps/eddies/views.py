from django.shortcuts import render
from .forms import SearchAreaForm
from pydap.client import open_url
import numpy as np
from datetime import timedelta
from .cygnss.valid_point import ValidPoint


def eddies(request):
    if request.method == 'POST':
        form = SearchAreaForm(request.POST)
        if form.is_valid():
            # Collect and order datetime objects.
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            selected_dates = [start + timedelta(days=x) for x in range(0, (end.date() - start.date()).days)]
            selected_dates.append(end)

            #for date in selected_dates:
            #   for satellite_number in range(1, 9):
            #        url = generate_url(date, satellite_number)
            #        collect_data(url)

    else:
        form = SearchAreaForm()
    return render(request, "eddies/eddies.html", {'form': form})


# Function collecting relevant data for specific date.
def generate_url(date, satellite_number):
    base_url = "https://podaac-opendap.jpl.nasa.gov/opendap/hyrax/allData/"
    dataset = "cygnss/"
    level = "L1/"
    version = "v2.1/"
    date_string = str(date.year)+str(date.month)+str(date.day).zfill(2)
    specific_url = "/cyg0"+str(satellite_number)+".ddmi.s"+date_string+"-000000-e"+date_string+"-235959.l1.power-brcs.a21.d21.nc"
    url = base_url+dataset+level+version+str(date.year)+"/"+str(date.timetuple().tm_yday).zfill(3)+specific_url
    return url


# Collects the data from OPeNDAP nc files.
def collect_data(url):
    query = "?spacecraft_id"
    dataset = open_url(url+query)
    spacecraft_id = dataset['spacecraft_id'][:].data
    print(spacecraft_id)

