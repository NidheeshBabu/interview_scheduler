from datetime import datetime
from rest_framework import serializers
from interview_scheduler.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=['%d-%m-%Y'], format='%d-%m-%Y')
    start_time = serializers.TimeField(input_formats=['%I:%M %p'], format='%I:%M %p')
    end_time = serializers.TimeField(input_formats=['%I:%M %p'], format='%I:%M %p')
    
    class Meta:
        model = UserModel
        fields = "__all__"
    
    def validate(self, data):
        if len(data['full_name']) < 3:
            raise serializers.ValidationError("Name is too short")
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("Invalid time")
        if data['date'] < datetime.now().date():
            raise serializers.ValidationError("Invalid date")
        if data['role_name'] not in ['interviewer', 'candidate']:
            raise serializers.ValidationError("Invalid role, role must be either interviewer or candidate")
        return data
