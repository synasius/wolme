__author__ = 'Federico Frenguelli <synasius@gmail.com>'

from django.contrib import admin

from models import Movement, Tag, Wallet

admin.site.register(Movement)
admin.site.register(Tag)
admin.site.register(Wallet)
