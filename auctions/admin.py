from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(AuctionListing)
admin.site.register(Offer)

# Register your models here.
