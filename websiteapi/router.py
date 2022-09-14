from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('WebsiteContects', WebsiteContectsView),
router.register('TourRegions', TourRegionsView),
router.register('TourDestination', TourDestnationView),
router.register('TourView', TourView),
router.register('TourData', TourDataView),
