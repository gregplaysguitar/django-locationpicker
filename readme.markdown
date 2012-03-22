# Usage

1. Copy/symlink location_picker.py onto your path
2. Copy/symlink the static/location_picker directory into your static directory
3. Use in your models.py as follows:

    from location_picker import LocationField
    class MyModel(models.Model):
        location = LocationField()
    
