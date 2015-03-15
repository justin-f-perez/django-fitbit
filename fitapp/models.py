from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


UserFitbitUserModel = getattr(settings, 'USERFITBIT_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class UserFitbit(models.Model):
    """
    This model stores a user's Fitbit authentication.
    """

    user = models.OneToOneField(UserFitbitUserModel)
    fitbit_user = models.CharField(max_length=32, unique=True)
    auth_token = models.TextField()
    auth_secret = models.TextField()

    def __str__(self):
        return self.user.__str__()

    def get_user_data(self):
        return {
            'resource_owner_key': self.auth_token,
            'resource_owner_secret': self.auth_secret,
            'user_id': self.fitbit_user,
        }


class TimeSeriesDataType(models.Model):

    steps = 0
    body = 1
    TYPE_CHOICES = (
        (steps, 'steps'),
        (body, 'body'),
    )
    category = models.IntegerField(choices=TYPE_CHOICES)
    resource = models.CharField(max_length=128)

    def __str__(self):
        return self.path()

    class Meta:
        unique_together = ('category', 'resource')
        ordering = ['category', 'resource']

    def path(self):
        return '/'.join([self.get_category_display(), self.resource])


# Going to run with both this and the individual data models for a bit, to see
# how well this single type works for data collection
class TimeSeriesData(models.Model):
    """
    The purpose of this model is to store Fitbit user data obtained from their
    time series API (https://wiki.fitbit.com/display/API/API-Get-Time-Series).
    """

    user = models.ForeignKey(UserFitbitUserModel)
    resource_type = models.ForeignKey(TimeSeriesDataType)
    date = models.DateField()
    value = models.CharField(null=True, default=None, max_length=32)

    class Meta:
        unique_together = ('user', 'resource_type', 'date')

    def string_date(self):
        return self.date.strftime('%Y-%m-%d')


class DayStepData(models.Model):
    """
    This model is intended to store a Fitbit user's daily step data.
    """

    user = models.ForeignKey(UserFitbitUserModel)
    steps = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.user.__str__(), self.date, self.steps)

    class Meta:
        unique_together = ('user', 'date')


class MinuteStepData(models.Model):
    """
    This model is intended to store a Fitbit user's intra-hour step data.
    Requires Fitbit Partner API status.
    """

    user = models.ForeignKey(UserFitbitUserModel)
    steps = models.IntegerField()
    day = models.ForeignKey(DayStepData)
    time = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.user, self.day.date, self.steps)

    class Meta:
        unique_together = ('user', 'time')


class AriaData(models.Model):
    """
    This model is intended to store a Fitbit user's Aria scale data, which includes
    body weight and body fat measurements.
    """

    user = models.ForeignKey(UserFitbitUserModel)
    body_weight = models.DecimalField(decimal_places=1, max_digits=4)
    body_fat = models.DecimalField(decimal_places=1, max_digits=3)
    bmi = models.DecimalField(decimal_places=1, max_digits=3)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}, {3}".format(self.user, self.date, self.body_weight,
                                             self.body_fat)