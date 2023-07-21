from rest_framework import serializers
from dashboard.models import *

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'