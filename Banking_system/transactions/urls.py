from django.urls import path
from django.urls import path
from .views import DepositView, WithdrawView, HistoryView

urlpatterns = [
    path('deposit/', DepositView.as_view()),
    path('withdraw/', WithdrawView.as_view()),
    path('history/', HistoryView.as_view()),
]
