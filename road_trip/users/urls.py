from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import UserList, UserDetail

urlpatterns = [ 
    path('', UserList.as_view()),
    path('<int:user_id>', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)