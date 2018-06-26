from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from api.views import TagCreateView, TagDetailsView, UserView, UserDetailsView

schema_view = get_schema_view(title = "redhawk API")

urlpatterns = {
    url(r'^schema/$', schema_view),
    url(r'^taglists/$', TagCreateView.as_view(), name="tags"),
    url(r'^taglists/(?P<pk>[0-9]+)/$', TagDetailsView.as_view(), name="tag_detail"),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
