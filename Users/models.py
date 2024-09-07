from dateutil.utils import today
from django_jalali.db import models as jmodels
from django.db import models
import jdatetime

class CustomUser(models.Model):
    GENDER_CHOICE = [
        ('M', 'male'),
        ("F", 'female')
    ]
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(default='Iran', max_length=4)
    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split(" ")
        return {'first_name': first_name, 'last_name': last_name}
    def get_age(self):
        today = jdatetime.date.today()
        age = today.year-self.birthday_date.year
        return age
    def is_birthday(self):
        today = jdatetime.date.today()
        return today.month == self.birthday_date.month and today.day == self.birthday_date.day
