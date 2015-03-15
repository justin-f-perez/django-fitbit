from . import models
from django.contrib import admin

admin.site.register(models.UserFitbit)
admin.site.register(models.AriaData)
admin.site.register(models.DayStepData)
admin.site.register(models.MinuteStepData)
admin.site.register(models.TimeSeriesDataType)