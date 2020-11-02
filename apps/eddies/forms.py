from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from leaflet.forms.widgets import LeafletWidget
from django.contrib.gis import forms


class SearchAreaForm(forms.Form):
    grid = forms.PolygonField(widget=LeafletWidget(), required=False)
    start_time = forms.DateTimeField(widget=DateTimePickerInput().start_of('event days'))
    end_time = forms.DateTimeField(widget=DateTimePickerInput().end_of('event days'))

    def clean(self):
        cleaned_data = super(SearchAreaForm, self).clean()
