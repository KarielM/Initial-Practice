"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Request === work ===> Response

from django.contrib import admin
from django.urls import path
from app.views import hello_world_view, random_between_view, hello_nate, roll_die_view, add_view, test_pop, hey_you, how_old, can_i_take_your_order
from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path('age-in/<int:end>/<int:birthyear>', how_old),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>', can_i_take_your_order),
















    path('hello/', hello_world_view),
    path('hello_<str:name>/', hello_nate),
    path('roll_die/<int:sides>', roll_die_view),
    path('random_between/<int:lo>/<int:hi>/', random_between_view),
    path('add/<int:x>/<int:y>', add_view),
    path('test_list', test_pop),
    path('hey/<str:name>', hey_you),
    # path('age-in/<int:end>/<int:birthyear>', how_old),
    # path('order-total/<int:burgers>/<int:fries>/<int:drinks>', can_i_take_your_order),
    path('warmup-1/near-hundred/<int:n>', near_hundred),
    path('warmup-2/string-splosion/<str:str0>', string_splosion),
    path('string-2/cat-dog/<str:str0>', cat_dog),
    path('logic-2/lone-sum/<int:a>_<int:b>_<int:c>', lone_sum),
    path('admin/', admin.site.urls)
]
