from rest_framework import serializers
from .models import DonorDetails, PatientDetail, Request, Stock, Feedback

class DonorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorDetails
        fields = '__all__'

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetail
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
