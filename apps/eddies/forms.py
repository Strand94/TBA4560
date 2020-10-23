from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class SearchAreaForm(forms.Form):
    north_west_lat = forms.FloatField(min_value=-90, max_value=90)
    north_west_lon = forms.FloatField(min_value=-90, max_value=90)

    south_east_lat = forms.FloatField(min_value=-90, max_value=90)
    south_east_lon = forms.FloatField(min_value=-90, max_value=90)

    start_time = forms.DateTimeField(widget=DateTimePickerInput().start_of('event days'))
    end_time = forms.DateTimeField(widget=DateTimePickerInput().end_of('event days'))


    def clean(self):
        cleaned_data = super(SearchAreaForm, self).clean()
        north_west = cleaned_data.get('north_west')
        south_east = cleaned_data.get('south_east')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if not north_west and not south_east and not end_time and not start_time:
            raise forms.ValidationError('You have to fill out all the fields!')
