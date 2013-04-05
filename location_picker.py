from django import forms
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# See readme.markdown
STATIC_URL = getattr(settings, 'LOCATION_PICKER_STATIC_URL', '%slocation_picker/' % settings.STATIC_URL)

class LocationPickerWidget(forms.TextInput):
    '''Widget which provides a google maps-powered widget for choosing
       a location in the format lat,lng.'''
       
    class Media:
        css = {
            'all': ('%slocation_picker.css' % STATIC_URL,)
        }
        js = ('http://maps.google.com/maps/api/js?sensor=false',
              '%sjquery.location_picker.js' % STATIC_URL,)

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)


class LocationField(models.CharField):
    '''A django model field which stores a lat/lng pair, validating the 
       format as lat,lng - ie.
       
       43.5343,172.6236'''
    
    DEFAULT_KWARGS = {'max_length': 255}
    
    def __init__(self, *args, **kwargs):
        kwargs = dict(list(self.DEFAULT_KWARGS.items()) + list(kwargs.items()))
        super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)

    def validate(self, value, obj):
        super(LocationField, self).validate(value, obj)
        try:
            x, y = value.split(',')
            float(x.strip()), float(y.strip())
        except:
            raise ValidationError('Bad coordinate format - should be lat,lng - eg. 43.5343,172.6236')
    
    def south_field_triple(self):
        ''''Returns a suitable description of this field for South.'''
        
        from south.modelsinspector import introspector
        args, kwargs = introspector(models.CharField)
        kwargs = dict(list(self.DEFAULT_KWARGS.items()) + list(kwargs.items()))
        return ('django.db.models.fields.CharField', args, kwargs)
        


