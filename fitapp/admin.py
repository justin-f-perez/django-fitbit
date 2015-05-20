from . import models
from django.contrib import admin

admin.site.register(models.UserFitbit)
admin.site.register(models.TimeSeriesDataType)
admin.site.register(models.TimeSeriesData)
