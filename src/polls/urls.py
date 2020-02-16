from django.urls import path

from . import views
urlpatterns = [
    # z.B.: /polls/
    path('', views.index, name='index'),

    # z.B.: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # z.B.: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # z.B.: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
