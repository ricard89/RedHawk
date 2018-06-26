from django.conf.urls import url
from main_app import views


# TEMPLATE TAGGING
app_name = 'main_app'

urlpatterns = [
    # MAIN APP URLS
    url(r'^taglist/$', views.taglist, name='taglist'),
    url(r'^update_tag_value/(?P<tag_id>\d+)/$', views.update_tag_value, name='update_tag_value'),
    url(r'^add_tag/$', views.add_tag, name='add_tag'),
    url(r'^delete_tag/(?P<tag_id>\d+)/$', views.delete_tag, name='delete_tag'),
]
