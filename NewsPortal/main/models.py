from django.db import models


class New(models.Model):
    nameNew = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    textNew = models.TextField()
    my_image = models.ImageField(upload_to='images/',blank=True,null=True)
    date = models.DateField()

    def __str__(self):
        return self.nameNew
