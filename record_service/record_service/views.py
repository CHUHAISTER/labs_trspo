from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecordSerializer
from .models import Record,Faculty,SubjectScore

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def record_list(request):
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def record_detail(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def calculate_scores(request, faculty_id):
    try:
        faculty = Faculty.objects.get(pk=faculty_id)
    except Faculty.DoesNotExist:
        return Response({"error": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

    records = Record.objects.filter(applicant__faculty=faculty, is_approved=True)
    results = []

    for record in records:
        applicant = record.applicant
        subject_scores = SubjectScore.objects.filter(applicant=applicant)
        total_score = sum(score.score for score in subject_scores) + applicant.certificate_score

        results.append({
            "applicant_id": applicant.id,
            "applicant_name": applicant.name,
            "total_score": total_score
        })

    results = sorted(results, key=lambda x: x['total_score'], reverse=True)
    enrolled_applicants = results[:faculty.intake_capacity]

    return Response({
        "faculty": faculty.name,
        "enrolled_applicants": enrolled_applicants
    }, status=status.HTTP_200_OK)