from rest_framework import serializers
from student.models import student


class studentSerializer(serializers.ModelSerializer):


    name=serializers.CharField(
        max_length=20,
        label="Name :",
        style={'placeholder': 'Your Good Name', 'autofocus': True}
    )
    email = serializers.EmailField(
        max_length=20,
        label="Email :",
        style={'placeholder': 'Email', 'type':'email', 'pattern':'/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/'}
    )
    contact=serializers.CharField(
        max_length=20,
        label="Contact :",
        style={'placeholder': 'Contact','pattern':'[0-9]+','maxlength':'10','minlength':'10' }
    )

    class Meta:
        model=student
        fields='__all__'
