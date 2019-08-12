from rest_framework import serializers
from app1.models import Books
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = 'id', 'title', 'pages'