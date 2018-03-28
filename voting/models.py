from django.db import models


class Votes(models.Model):
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total_votes)


class VoteDetail(models.Model):
    votes = models.ForeignKey(Votes)
    voted = models.IntegerField()
    not_voted = models.IntegerField()

    def __str__(self):
        return str(self.votes) + str(self.voted) + str(self.not_voted)





