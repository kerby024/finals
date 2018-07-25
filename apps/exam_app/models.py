from __future__ import unicode_literals
from django.db import models
from ..logreg_app.models import User

class FriendManager(models.Manager):

    def addpokes(self, userid, pokedid):
        self.create(
            user_id = userid,
            poked_id = pokedid
        )
    
class Friend(models.Model):
    user = models.ForeignKey(User, related_name='pokee')
    poked = models.ForeignKey(User, related_name="pokers")
    objects = FriendManager()