from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    age = filters.NumberFilter(field_name='age')
