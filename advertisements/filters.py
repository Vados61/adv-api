from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementCreatedFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    creator = filters.ModelChoiceFilter(queryset=User.objects.all())
    created_at = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at']
