from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Count
from django.template import loader

from .models import Customer, Activities


def index(request):
    template = loader.get_template('customers/base.html')
    return HttpResponse(template.render({},request))


class CustomerList(ListView):
    model = Customer


class ActivityList(ListView):
    model = Activities


class CustomerByeSubscribeList(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = ' customer_bye_subscribe'

    def get_queryset(self):
        return Customer.objects.filter(subscribe_plan__subscribe_name=self.kwargs['subscribe'])


class CustomerByeActivityList(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = ' customer_bye_activity_and_date'

    def get_queryset(self):
        return Customer.objects.filter(activities__starting_time__date=self.kwargs['time'],
                                       activities__name=self.kwargs['activity'])


class CustomerByeActivityAmountList(ListView):
    mode = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customer_bye_activity_amount'

    # todo: write it better.
    def get_queryset(self):
        pk = 1
        most_participate = Customer.objects.get(pk=1)
        customers_amount = Customer.objects.all().count() + 1
        for i in range(1, customers_amount):
            check_if_bigger = Customer.objects.get(pk=i)
            if check_if_bigger.activities.count() > most_participate.activities.count():
                most_participate = check_if_bigger
                pk = i
        return [Customer.objects.get(pk=pk)]


class MostParticipatesActivity(ListView):
    mode = Activities
    template_name = 'customers/activities_list.html'
    context_object_name = 'most_participates_activity'

    # todo: write it better.
    def get_queryset(self):
        activities = Activities.objects.annotate(Count('customer')).values_list('name', 'customer__count')
        most_participate = activities.get(pk=1)
        activities_amount = activities.all().count()
        for i in range(1, activities_amount):
            check_if_bigger = activities.get(pk=i)
            if check_if_bigger[1] > most_participate[1]:
                most_participate = check_if_bigger
        return [most_participate]
