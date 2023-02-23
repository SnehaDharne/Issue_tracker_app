from django.urls import path

from tracker import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path('', views.IssueListView.as_view(), name="issue.list"),
    path('issue/<int:pk>', views.IssueDetailView.as_view(), name="issue.detail"),
    path('issue/create', views.CreateIssueView.as_view(), name="issue.create"),
    path('issue/update/<int:pk>', views.UpdateIssueView.as_view(), name="issue.close"),
    path('issue/delete/<int:pk>', views.DeleteIssueView.as_view(), name="issue.delete")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)