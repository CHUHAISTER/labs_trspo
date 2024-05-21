from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Applicant, Faculty, Subject, SubjectScore, Record
from .serializers import ApplicantSerializer, FacultySerializer, SubjectSerializer, SubjectScoreSerializer, \
    RecordSerializer


@api_view(['GET', 'POST'])
def applicant_list(request):
    if request.method == 'GET':
        applicants = Applicant.objects.all()
        serializer = ApplicantSerializer(applicants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def applicant_detail(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
    except Applicant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApplicantSerializer(applicant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        applicant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def faculty_list(request):
    faculties = Faculty.objects.all()
    serializer = FacultySerializer(faculties, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def faculty_list_post(request):

   serializer = FacultySerializer(data=request.data)
   if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def faculty_detail(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def subject_list_post(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


@api_view(['GET', 'PUT', 'DELETE'])
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