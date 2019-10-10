from django.db import models
from datetime import datetime
class Diary(models.Model):
    Text=models.TextField()
    Date=models.DateTimeField(primary_key=True,default=datetime.now)
