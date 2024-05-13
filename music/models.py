from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=120)
    born = models.DateField()

    def __str__(self) -> str:
        return self.name


class Genres(models.Model):
    title = models.CharField(max_length=100)

class Music(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField(Genres, null=True,blank=True)
    lyric = models.TextField()


    def __str__(self):
        return f'{self.title} /// {self.singer}'
    


    
