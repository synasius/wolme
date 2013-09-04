from __future__ import unicode_literals

from rest_framework import routers

from .apiviews import WalletViewSet, MovementViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'movements', MovementViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
