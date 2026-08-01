"""
API Views for managing expenses.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreateView(APIView):
    """
    Handles listing all expenses and creating new ones.
    
    GET: Returns all expenses, optionally filtered by category.
    POST: Creates a new expense with validation.
    """
    
    def get(self, request):
        """
        Retrieve all expenses with optional category filter.
        
        Query Parameters:
            category (str, optional): Filter expenses by category
        """
        # Start with all expenses
        queryset = Expense.objects.all()
        
        # Apply category filter if provided
        category = request.query_params.get('category')
        if category:
            # Case-insensitive filtering for better user experience
            queryset = queryset.filter(category__iexact=category)
        
        # Serialize and return the results
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create a new expense with the provided data.
        
        Expected JSON:
            {
                "title": "Lunch",
                "amount": 15.50,
                "category": "Food",
                "date": "2026-07-31"
            }
        """
        serializer = ExpenseSerializer(data=request.data)
        
        if serializer.is_valid():
            expense = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailView(APIView):
    """
    Handles individual expense operations.
    
    DELETE: Removes an expense by its ID.
    """
    
    def delete(self, request, pk):
        """
        Delete an expense by its primary key.
        
        Args:
            pk: The ID of the expense to delete
        
        Returns:
            204 No Content on success
            404 Not Found if expense doesn't exist
        """
        try:
            expense = get_object_or_404(Expense, pk=pk)
            expense.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Expense.DoesNotExist:
            return Response(
                {"error": "Expense not found."},
                status=status.HTTP_404_NOT_FOUND
            )


class ExpenseTotalView(APIView):
    """
    Calculates total expenses, optionally filtered by category.
    
    GET: Returns total sum of all expenses or filtered by category.
    """
    
    def get(self, request):
        """
        Calculate the total expenses.
        
        Query Parameters:
            category (str, optional): Calculate total for a specific category
        
        Returns:
            {"total": 1234.56} for overall total
            {"category": "Food", "total": 500.00} for category total
        """
        category = request.query_params.get('category')
        
        try:
            # Start with all expenses
            queryset = Expense.objects.all()
            
            # Apply category filter if provided
            if category:
                queryset = queryset.filter(category__iexact=category)
            
            # Calculate the sum
            total = queryset.aggregate(total=Sum('amount'))['total']
            
            # Handle empty result set
            if total is None:
                total = 0.0
            
            # Return appropriate response format
            if category:
                return Response({
                    'category': category,
                    'total': total
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'total': total
                }, status=status.HTTP_200_OK)
                
        except Exception as e:
            # Log the error in production
            return Response(
                {'error': 'Unable to calculate total expenses.'},
                status=status.HTTP_400_BAD_REQUEST
            )