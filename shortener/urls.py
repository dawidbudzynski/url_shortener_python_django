from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.ShortenUrlView.as_view(), name='shortener'),
    path('<url_code>', views.RedirectToOriginalPageView.as_view(), name='redirect_to_original'),
    path('result/success/<url_code>', views.SuccessView.as_view(), name='success'),
    path('result/page_not_found', views.PageNotFoundView.as_view(), name='page_not_found'),
    path('result/error', views.ErrorView.as_view(), name='error')
]
