from django.db import models
from django.utils import timezone

SORT_CHOICES = (('activity', 'activity'), ('votes', 'votes'), ('creation', 'creation'), ('relevance', 'relevance'))
ORDER_CHOICES = (('asc', 'asc'), ('desc', 'desc'))


class ExchangeModel(models.Model):
    id = models.UUIDField(primary_key=True)
    page_no = models.IntegerField(default=1)
    page_size = models.IntegerField(default=15)

    from_date = models.CharField(max_length=20)
    to_date = models.CharField(max_length=20)

    order_by = models.CharField(choices=ORDER_CHOICES, max_length=4)

    min_date = models.CharField(max_length=20)
    max_date = models.CharField(max_length=20)
    sort_by = models.CharField(choices=SORT_CHOICES, max_length=10)

    question = models.CharField(max_length=200)

    is_accepted = models.BooleanField(null=True)

    no_of_answers = models.CharField(max_length=20)

    body = models.CharField(max_length=200)

    is_closed = models.BooleanField(null=True)
    is_migrated = models.BooleanField(null=True)
    notice = models.BooleanField(null=True)

    not_tagged = models.CharField(max_length=200)
    tagged = models.CharField(max_length=200)

    title = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    url = models.CharField(max_length=999)
    views = models.CharField(max_length=20)
    wiki = models.BooleanField(null=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
