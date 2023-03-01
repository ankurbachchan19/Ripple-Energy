from django.db import models


class Buyer(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=20)


class Seller(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=30)
    verified = models.BooleanField(null=True)


class Competition(models.Model):

    id = models.CharField(primary_key=True, max_length=8)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE,
                              related_name="competition_buyer")
    name = models.CharField(max_length=100)
    open = models.DateTimeField()
    closed = models.DateTimeField()
    minimum_capacity = models.IntegerField()
    currency = models.CharField(max_length=3)


class Bid(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    created = models.DateTimeField()
    accepted = models.BooleanField(null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE,
                                    related_name="competition")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="competition_seller")
    value = models.FloatField()
    offered_capacity = models.IntegerField()
