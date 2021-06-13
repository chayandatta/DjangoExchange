from django.db import models

SORT_CHOICES = (('activity', 'activity'), ('votes', 'votes'), ('creation', 'creation'), ('relevance', 'relevance'))
ORDER_CHOICES = (('asc', 'asc'), ('desc', 'desc'))


class ExchangeModel(models.Model):

    page_no = models.IntegerField(default=1)
    page_size = models.IntegerField(default=15)

    from_date = models.DateField()
    to_date = models.DateField()

    order_by = models.CharField(choices=ORDER_CHOICES, max_length=4)

    min_date = models.DateField()
    max_date = models.DateField()
    sort_by = models.CharField(choices=SORT_CHOICES, max_length=10)

    question = models.CharField(max_length=200)

    is_accepted = models.BooleanField(null=True)

    no_of_answers = models.IntegerField()

    body = models.CharField(max_length=200)

    is_closed = models.BooleanField(null=True)
    is_migrated = models.BooleanField(null=True)
    notice = models.BooleanField(null=True)

    not_tagged = models.CharField(max_length=200)
    tagged = models.CharField(max_length=200)

    title = models.CharField(max_length=200)
    user = models.IntegerField()
    url = models.CharField(max_length=999)
    views = models.IntegerField()
    wiki = models.BooleanField(null=True)

