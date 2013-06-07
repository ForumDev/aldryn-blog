# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_blog.views import ArchiveView, PostDetailView, TaggedListView
from aldryn_blog.feeds import LatestEntriesFeed, TagFeed

urlpatterns = patterns('',
    url(r'^$', ArchiveView.as_view(), name='latest-posts'),
    url(r'^feed/$', LatestEntriesFeed(), name='latest-posts-feed'),
    url(r'^(?P<year>\d{4})/$', ArchiveView.as_view(), name='archive-year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', ArchiveView.as_view(), name='archive-month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^tagged/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='tagged-posts'),
    url(r'^tagged/(?P<tag>[-\w]+)/feed/$', TagFeed(), name='tagged-posts-feed'),
)