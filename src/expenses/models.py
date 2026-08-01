"""
Expense model for tracking financial transactions.
"""
from django.db import models
from django.utils import timezone
from decimal import Decimal


class Expense(models.Model):
    """
    Represents a single expense entry in the tracker.
    
    Each expense has a title, amount, category, and date.
    The category field is indexed for faster filtering.
    """
    title = models.CharField(
        max_length=200,
        help_text="Brief description of the expense"
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Amount spent (must be greater than 0)"
    )
    category = models.CharField(
        max_length=100, 
        db_index=True,
        help_text="Category of the expense (e.g., Food, Transport)"
    )
    date = models.DateField(
        default=timezone.now,
        help_text="Date when the expense occurred"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when this record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when this record was last updated"
    )

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        """Human-readable representation of the expense."""
        return f"{self.title} - ${self.amount:.2f} ({self.category})"
    
    @property
    def formatted_amount(self):
        """Returns the amount formatted as currency."""
        return f"${self.amount:.2f}"