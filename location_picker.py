from django import forms
from django.db import models
from django.conf import settings

class LocationPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.MEDIA_URL + 'c/lib/location_picker.css',
            )
        }
        js = (
            'http://www.google.com/jsapi?key=' + settings.GOOGLE_MAPS_API_KEY,
            settings.MEDIA_URL + 'j/lib/jquery.location_picker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)

class LocationField(models.CharField):

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)