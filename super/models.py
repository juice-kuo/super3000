from django.db import models

# Create your models here.
class company(models.Model):
    cComid = models.CharField(max_length=20,null=False)
    cPosition = models.CharField(max_length=20,null=False)
    cName = models.CharField(max_length=20,null=False)
    cSharemoney = models.CharField(max_length=30,null=False)
    
    def _str_(self):
        return self.cName
    