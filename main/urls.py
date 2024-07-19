from django.urls import path, include

urlpatterns =[
    path('', include(('main.lists.urls', 'main'), namespace='lists')),
    
]