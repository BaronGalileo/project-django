from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter

from .models import Post


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%Y-%m-%dT',
            attrs={'type': 'datetime-local'},
        ))


    class Meta:
        model = Post
        fields = {'title':['icontains'],
                 'categoryType': ['icontains'],

                 }
