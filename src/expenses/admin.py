"""
Admin configuration for the Expense model.
"""
from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Custom admin interface for managing expenses.
    """
    # Display these fields in the list view
    list_display = ('id', 'title', 'amount', 'category', 'date', 'created_at')
    
    # Add filters for easy navigation
    list_filter = ('category', 'date', 'created_at')
    
    # Enable search across these fields
    search_fields = ('title', 'category', 'description')
    
    # Default ordering
    ordering = ('-date', '-created_at')
    
    # Make these fields read-only
    readonly_fields = ('created_at', 'updated_at')
    
    # Group fields in the detail view
    fieldsets = (
        ('Expense Information', {
            'fields': ('title', 'amount', 'category', 'date')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Add bulk actions
    actions = ['delete_selected']