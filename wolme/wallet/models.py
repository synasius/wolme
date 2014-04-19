from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


@python_2_unicode_compatible
class Tag(models.Model):
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.slug


@python_2_unicode_compatible
class Wallet(models.Model):
    CURRENCIES = (
        ("EUR", "EUR"),
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wallets')
    label = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=3, null=False, blank=False, choices=CURRENCIES)

    def __str__(self):
        return "{} ({})".format(self.label, self.currency)


@python_2_unicode_compatible
class Movement(models.Model):
    wallet = models.ForeignKey(Wallet, related_name="movements")
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    tags = models.ManyToManyField(Tag, related_name="movements")

    def __str__(self):
        return "{} - {:.2f} for {} on {}".format(
            self.type, self.amount, self.wallet, self.date)
