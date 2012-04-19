# Usage

1. Copy/symlink location_picker.py onto your path
2. Copy/symlink the static/location_picker directory into your static directory. If you're
   not using staticfiles, you'll need to set LOCATION_PICKER_STATIC_URL to wherever you put
   the location_picker files.
3. Use in your models.py as follows:

    from location_picker import LocationField
    class MyModel(models.Model):
        location = LocationField()

