from django.db import models

class Cars(models.Model):

    class Meta:

        db_table = 'cars'

    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=40)
    info = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    img = models.CharField(max_length=100)
    id = models.AutoField(primary_key= True)



    def str(self):
        return self.model
