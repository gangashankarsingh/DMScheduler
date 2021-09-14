"""scheduler_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


from mail_credentials.models import RecepientContacts, Authentication
from rest_framework import routers, serializers, viewsets

class RecepientContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecepientContacts
        fields = ['email_id', 'description']


# ViewSets define the view behavior.
class RecepientContactsViewSet(viewsets.ModelViewSet):
    queryset = RecepientContacts.objects.all()
    serializer_class = RecepientContactsSerializer

# Serializers define the API representation.
class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):
    recepients = RecepientContactsSerializer(many=True)
    class Meta:
        model = Authentication
        fields = ['key_id', 'email_id', 'authenticator','recepients']

class AuthenticationViewSet(viewsets.ModelViewSet):
    queryset = Authentication.objects.all()
    serializer_class = AuthenticationSerializer



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'authenticate', AuthenticationViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls')),
]
