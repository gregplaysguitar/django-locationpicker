# Django-locationpicker

Provides a field to store lat/lng pairs in a django model, and a google maps-powered 
location picker widget which is automatically enabled for the admin.

## Installation/usage

1. Run setup.py install, or place location_picker.py somewhere on your path.
2. If you're using staticfiles, add `location_picker` to your `INSTALLED_APPS` so
   that django can find the static files.
3. If you're not using staticfiles, you'll need to copy the static/location_picker 
   directory into your media directory, and set `LOCATION_PICKER_STATIC_URL`.
4. Use in your models.py as follows:

        from location_picker import LocationField
        class MyModel(models.Model):
            location = LocationField()

