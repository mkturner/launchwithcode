from django.db import models


# Create your models here.
class Join(models.Model):
    email = models.EmailField()
    ref_id = models.CharField(max_length=120, default="empty", unique=True)
    ip_address = models.CharField(max_length=120, default='0.0.0.0')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % (self.email)

    class Meta():
        """docstring for Meta"""
        unique_together = ('email', 'ref_id',)
