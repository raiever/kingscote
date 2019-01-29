from django.db import models

class Page(models.Model):
    title = models.CharField('Page Title', max_length=60)
    permalink = models.CharField('Permanent Link', max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title
        
# Create your models here.


if __name__ == "__main__":
    pass
    