from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from expenses.models import Expense


class ExpenseModelTest(TestCase):
    """
    Test cases for the Expense model.
    """
    
    def setUp(self):
        self.expense_data = {
            'title': 'Test Expense',
            'amount': Decimal('100.50'),
            'category': 'Food',
            'date': timezone.now().date()
        }
    
    def test_create_expense(self):
        """
        Test creating an expense instance.
        """
        expense = Expense.objects.create(**self.expense_data)
        self.assertEqual(expense.title, 'Test Expense')
        self.assertEqual(expense.amount, Decimal('100.50'))
        self.assertEqual(expense.category, 'Food')
        self.assertIsNotNone(expense.date)
        self.assertIsNotNone(expense.created_at)
        self.assertIsNotNone(expense.updated_at)
    
    def test_expense_str_method(self):
        """
        Test the string representation of expense.
        """
        expense = Expense.objects.create(**self.expense_data)
        expected_str = f"Test Expense - $100.50 (Food)"
        self.assertEqual(str(expense), expected_str)
    
    def test_expense_ordering(self):
        """
        Test that expenses are ordered by date (descending) by default.
        """
        expense1 = Expense.objects.create(
            title='Expense 1',
            amount=Decimal('100.00'),
            category='Test',
            date='2026-07-30'
        )
        expense2 = Expense.objects.create(
            title='Expense 2',
            amount=Decimal('200.00'),
            category='Test',
            date='2026-07-31'
        )
        
        expenses = Expense.objects.all()
        self.assertEqual(expenses[0].title, 'Expense 2')
        self.assertEqual(expenses[1].title, 'Expense 1')