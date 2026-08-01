from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from datetime import datetime, timedelta
from expenses.serializers import ExpenseSerializer
from expenses.models import Expense


class ExpenseSerializerTest(TestCase):
    """
    Test cases for the Expense serializer.
    """
    
    def setUp(self):
        self.valid_data = {
            'title': 'Test Expense',
            'amount': '100.50',
            'category': 'Food',
            'date': timezone.now().date().isoformat()
        }
    
    def test_valid_serializer(self):
        """
        Test serializer with valid data.
        """
        serializer = ExpenseSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
    
    def test_title_required(self):
        """
        Test that title is required.
        """
        data = self.valid_data.copy()
        data['title'] = ''
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
    
    def test_title_min_length(self):
        """
        Test that title has minimum length.
        """
        data = self.valid_data.copy()
        data['title'] = 'A'
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
    
    def test_amount_required(self):
        """
        Test that amount is required.
        """
        data = self.valid_data.copy()
        data['amount'] = None
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('amount', serializer.errors)
    
    def test_amount_positive(self):
        """
        Test that amount must be positive.
        """
        data = self.valid_data.copy()
        data['amount'] = '-10.00'
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('amount', serializer.errors)
    
    def test_amount_zero(self):
        """
        Test that amount cannot be zero.
        """
        data = self.valid_data.copy()
        data['amount'] = '0.00'
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('amount', serializer.errors)
    
    def test_category_required(self):
        """
        Test that category is required.
        """
        data = self.valid_data.copy()
        data['category'] = ''
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('category', serializer.errors)
    
    def test_date_required(self):
        """
        Test that date is required.
        """
        data = self.valid_data.copy()
        data['date'] = None
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
    
    def test_date_not_future(self):
        """
        Test that date cannot be in the future.
        """
        data = self.valid_data.copy()
        future_date = (datetime.now() + timedelta(days=1)).date().isoformat()
        data['date'] = future_date
        serializer = ExpenseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)