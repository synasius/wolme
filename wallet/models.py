from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.slug


class Wallet(models.Model):
    CURRENCIES = (
        ("EUR", "EUR"),
    )
    user = models.ForeignKey('auth.User', related_name='wallets')
    label = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=3, null=False, blank=False, choices=CURRENCIES)

    def __unicode__(self):
        return u"{} ({})".format(self.label, self.currency)


class Movement(models.Model):
    MOVEMENT_IN = "in"
    MOVEMENT_OUT = "out"
    MOVEMENT_TYPES = (
        (MOVEMENT_IN, _("In")),
        (MOVEMENT_OUT, _("Out")),
    )

    wallet = models.ForeignKey(Wallet, related_name="movements")
    type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    tags = models.ManyToManyField(Tag, related_name="movements")

    def __unicode__(self):
        return u"{} - {:.2f} for {} on {}".format(
            self.type, self.amount, self.wallet, self.date)
