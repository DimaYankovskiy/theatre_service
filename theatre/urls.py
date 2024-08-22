from rest_framework import routers

from theatre.views import (
    ActorViewSet,
    GenreViewSet,
    PerformanceViewSet,
    PlayViewSet,
    ReservationViewSet,
    TheatreHallViewSet,
    TicketsViewSet,
)

router = routers.DefaultRouter()
router.register("theatre_halls", TheatreHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketsViewSet)

urlpatterns = router.urls

app_name = "theatre"
