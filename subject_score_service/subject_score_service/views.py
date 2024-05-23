from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import SubjectScore
from .serializers import SubjectScoreSerializer

@api_view(['GET', 'POST'])
def subject_score_list(request):
    if request.method == 'GET':
        subject_scores = SubjectScore.objects.all()
        serializer = SubjectScoreSerializer(subject_scores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def subject_score_detail(request, pk):
    try:
        subject_score = SubjectScore.objects.get(pk=pk)
    except SubjectScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectScoreSerializer(subject_score)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectScoreSerializer(subject_score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject_score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAdminUser])
def subject_score_detail_delete(request, pk):
    try:
        subject_score = SubjectScore.objects.get(pk=pk)
    except SubjectScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectScoreSerializer(subject_score)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        subject_score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)