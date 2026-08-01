from django.urls import path
from .views import ExpenseListCreateView, ExpenseDetailView, ExpenseTotalView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/total/', ExpenseTotalView.as_view(), name='expense-total'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
]