from django.db import models

# Create your models here.
class En(models.Model):
    winer = (
      (0, 'Home Team Winer'),
      (1, 'Draw'),
      (2, 'Away Team Winer'),
    )
    div = models.CharField(max_length=200)
    date = models.DateTimeField('Game date')
    hometeam = models.CharField(max_length=200)
    avayteam = models.CharField(max_length=200)
    fthg = models.IntegerField(default=0)
    ftag = models.IntegerField(default=0)
    ftr = models.IntegerField(choices=winer)
    hthg = models.IntegerField(default=0)
    htag = models.IntegerField(default=0)
    htr = models.IntegerField(choices=winer)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.div+"=> "+self.hometeam+"-"+self.avayteam+" "+str(self.fthg)+":"+str(self.ftag)

