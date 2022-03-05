from datetime import datetime, timedelta
from interview_scheduler.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from interview_scheduler.models import UserModel

    
class UserRegisterView(APIView):
    
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleView(APIView):
    
    def get(self, request):
        if not request.query_params.get('candidate_id') or not request.query_params.get('interviewer_id'):
            return Response({"error": "Candidate ID and Interviewer ID are required"})
        candidate_id = request.query_params.get('candidate_id')
        interviewer_id = request.query_params.get('interviewer_id')
        candidate_user = UserModel.objects.filter(pk=candidate_id, role_name='candidate').first()
        if not candidate_user:
            return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)
        interviewer_user = UserModel.objects.filter(pk=interviewer_id, role_name='interviewer').first()
        if not interviewer_user:
            return Response({"error": "Interviewer not found"}, status=status.HTTP_404_NOT_FOUND)
        if candidate_user.date != interviewer_user.date:
            return Response({"message":"Time slots are in different dates"})
        if candidate_user.start_time > interviewer_user.end_time or candidate_user.end_time < interviewer_user.start_time:
            return Response({"message": "Schedule not available, Non overlaping time slots"})
        if candidate_user.start_time < interviewer_user.start_time:
            start = interviewer_user.start_time
        elif candidate_user.start_time >= interviewer_user.start_time:
            start = candidate_user.start_time
        
        if candidate_user.end_time < interviewer_user.end_time:
            end = candidate_user.end_time
        elif candidate_user.end_time >= interviewer_user.end_time:
            end = interviewer_user.end_time
        date = candidate_user.date
        start = (datetime.combine(date, start))
        end = (datetime.combine(date, end))
        schedule_list = []
        while ((start+timedelta(hours=1)) <= end):
            t = (start.time().strftime('%I:%M %p'), (start+timedelta(hours=1)).time().strftime('%I:%M %p'))
            schedule_list.append(t)
            start = start + timedelta(hours=1)
        return Response({"schedules": schedule_list, "message": "OK"})
        