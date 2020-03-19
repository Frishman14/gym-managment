from django.contrib import admin
from django.urls import path
from customers.views import CustomerList, CustomerByeSubscribeList, CustomerByeActivityList, \
    CustomerByeActivityAmountList, MostParticipatesActivity, index

urlpatterns = [
    path('', index, name='index'),
    path('all_customers/', CustomerList.as_view(), name='all_customers'),
    path('customer_bye_subscribe/<str:subscribe>/', CustomerByeSubscribeList.as_view(), name='customer_by_subscribe'),
    path('customer_bye_subscribe/student/', CustomerByeSubscribeList.as_view(), name='customer_by_sub_student'),
    path('customer_bye_activity/<str:time>/<str:activity>/', CustomerByeActivityList.as_view(),
         name='cust_bye_act_and_date'),
    path('customer_bye_activity/2020-03-22/Pilates/', CustomerByeActivityList.as_view(),
         name='cust_in_pilates_on_sunday'),
    path('the_most_participate_customer/', CustomerByeActivityAmountList.as_view(), name='most_participate_cust'),
    path('most_participate_activity/', MostParticipatesActivity.as_view(), name='most_participates_activity'),
    path('admin/', admin.site.urls),
]
