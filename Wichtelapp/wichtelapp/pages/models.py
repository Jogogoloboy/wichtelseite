from django.db import models

class Phase(models.Model):
     name = models.CharField(unique=True, max_length=200)
     wishtime = models.BooleanField(default=True)
     selectiontime = models.BooleanField(default=True)
     start_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
     end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
