from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    description=models.TextField()
    starting_bid=models.CharField(max_length=50)
    category=models.CharField(max_length=50, blank= True)
    image_url=models.CharField(max_length=50, blank=True)

class Comment (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listing=models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    auction=models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    percentage=models.IntegerField(max_length=2)





