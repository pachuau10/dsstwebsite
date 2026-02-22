from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notices/', views.notice_board, name='notice_board'),
    path('notices/<int:pk>/', views.post_detail, name='post_detail'),
    path('fee-payment/', views.fee_payment, name='fee_payment'),
    path('fee-payment/receipt/<int:pk>/', views.payment_receipt, name='payment_receipt'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('labs/', views.labs, name='labs'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievements/', views.achievements, name='achievements'),
    path('admission/', views.admission, name='admission'),
    path('admission/success/<int:pk>/', views.admission_success, name='admission_success'),
    path('contact/', views.contact, name='contact'),
]
