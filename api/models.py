from django.db import models

# Create your models here.
class EntryValues(models.Model):
    script=models.CharField(max_length=1000)
    language = models.CharField(max_length=200)
    versionIndex = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s' % (self.script, self.language,self.versionIndex)

class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
