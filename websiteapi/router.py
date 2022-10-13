from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register('AuthView', AuthView)
router.register('Package', PackageView),
router.register('PackageDetail', Package_Detail_View),
router.register('Destination', DestnationView),
# router.register('Destination Detail', Destination_Detail_View),
router.register('Gallery', GalleryView),
router.register(' Hero', HeroView),
router.register('booking', BookingView),
