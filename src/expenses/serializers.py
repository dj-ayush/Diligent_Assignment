"""
Serializers for the Expense model with comprehensive validation.
"""
from rest_framework import serializers
from .models import Expense
from datetime import date


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Handles serialization and deserialization of Expense objects.
    
    Includes custom validation for:
    - Required fields
    - Amount must be positive
    - Date cannot be in the future
    - String fields must have minimum length
    """
    
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'date']
        read_only_fields = ['id']
    
    def validate_title(self, value):
        """
        Ensure title is not empty and has reasonable length.
        """
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Please provide a title for the expense."
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                "Title must be at least 2 characters long."
            )
        if len(value) > 200:
            raise serializers.ValidationError(
                "Title cannot exceed 200 characters."
            )
        return value
    
    def validate_amount(self, value):
        """
        Ensure amount is valid and greater than zero.
        """
        if value is None:
            raise serializers.ValidationError(
                "Amount is required."
            )
        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )
        # Check decimal places
        if value.as_tuple().exponent < -2:
            raise serializers.ValidationError(
                "Amount can have at most 2 decimal places."
            )
        return value
    
    def validate_category(self, value):
        """
        Ensure category is not empty and has reasonable length.
        """
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Please specify a category for the expense."
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                "Category must be at least 2 characters long."
            )
        if len(value) > 100:
            raise serializers.ValidationError(
                "Category cannot exceed 100 characters."
            )
        return value
    
    def validate_date(self, value):
        """
        Ensure date is valid and not in the future.
        """
        if not value:
            raise serializers.ValidationError(
                "Date is required."
            )
        if value > date.today():
            raise serializers.ValidationError(
                "Date cannot be in the future."
            )
        return value
    
    def validate(self, data):
        """
        Cross-field validation to ensure all required fields are present.
        """
        required_fields = ['title', 'amount', 'category']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({
                    field: f"{field.capitalize()} is required."
                })
        return data