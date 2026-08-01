from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from expenses.models import Expense


class ExpenseAPITestCase(TestCase):
    """
    Test cases for the Expense API endpoints.
    """
    
    def setUp(self):
        self.client = APIClient()
        self.expense_data = {
            'title': 'Test Expense',
            'amount': '100.50',
            'category': 'Food',
            'date': timezone.now().date().isoformat()
        }
        
        # Create sample expenses
        self.expense1 = Expense.objects.create(
            title='Lunch',
            amount=Decimal('15.50'),
            category='Food',
            date=timezone.now().date()
        )
        self.expense2 = Expense.objects.create(
            title='Bus Ticket',
            amount=Decimal('2.50'),
            category='Transport',
            date=timezone.now().date()
        )
        self.expense3 = Expense.objects.create(
            title='Dinner',
            amount=Decimal('25.00'),
            category='Food',
            date=timezone.now().date()
        )
    
    def test_create_expense_success(self):
        """
        Test creating a new expense successfully.
        """
        url = reverse('expense-list-create')
        response = self.client.post(url, self.expense_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Expense')
        self.assertEqual(response.data['category'], 'Food')
    
    def test_create_expense_validation_error(self):
        """
        Test creating an expense with invalid data.
        """
        url = reverse('expense-list-create')
        invalid_data = self.expense_data.copy()
        invalid_data['amount'] = '-10.00'
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)
    
    def test_list_all_expenses(self):
        """
        Test listing all expenses.
        """
        url = reverse('expense-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
    def test_filter_expenses_by_category(self):
        """
        Test filtering expenses by category.
        """
        url = reverse('expense-list-create')
        response = self.client.get(f"{url}?category=Food")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for expense in response.data:
            self.assertEqual(expense['category'], 'Food')
    
    def test_filter_expenses_case_insensitive(self):
        """
        Test category filtering is case-insensitive.
        """
        url = reverse('expense-list-create')
        response = self.client.get(f"{url}?category=food")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_get_total_expenses(self):
        """
        Test getting total of all expenses.
        """
        url = reverse('expense-total')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 43.00)  # 15.50 + 2.50 + 25.00
    
    def test_get_total_by_category(self):
        """
        Test getting total by category.
        """
        url = reverse('expense-total')
        response = self.client.get(f"{url}?category=Food")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], 'Food')
        self.assertEqual(response.data['total'], 40.50)  # 15.50 + 25.00
    
    def test_get_total_empty_category(self):
        """
        Test getting total for empty category.
        """
        url = reverse('expense-total')
        response = self.client.get(f"{url}?category=Entertainment")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], 'Entertainment')
        self.assertEqual(response.data['total'], 0.0)
    
    def test_delete_expense_success(self):
        """
        Test deleting an expense successfully.
        """
        url = reverse('expense-detail', kwargs={'pk': self.expense1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify expense is deleted
        self.assertEqual(Expense.objects.count(), 2)
    
    def test_delete_expense_not_found(self):
        """
        Test deleting a non-existent expense.
        """
        url = reverse('expense-detail', kwargs={'pk': 999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_invalid_id_deletion(self):
        """
        Test deleting with invalid ID.
        """
        url = reverse('expense-detail', kwargs={'pk': 'invalid'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)