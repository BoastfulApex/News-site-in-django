from django.db import models



class News(models.Model):
    name = models.CharField(null=True, max_length=250)
    main = models.TextField(null=True, max_length=2500)
    tag = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True, blank=True)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
