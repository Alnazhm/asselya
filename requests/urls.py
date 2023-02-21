from requests.views import CreateRequest, MyRequestsView
from django.urls import path
urlpatterns = [
    path('create/', CreateRequest.as_view(), name='create_request'),
    path('my_requests/', MyRequestsView.as_view(), name='my_requests')
]