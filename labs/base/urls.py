from django.urls import path
from .views import (
    applicant_list, applicant_detail,
    faculty_list, faculty_detail,
    subject_list, subject_detail,
    subject_score_list, subject_score_detail,
    record_list, record_detail,
faculty_list_post, subject_list_post,
calculate_scores
)

urlpatterns = [
    path('', applicant_list, name='applicant_list'),
    path('applicants/', applicant_list, name='applicant_list'),
    path('applicants/<int:pk>/', applicant_detail, name='applicant_detail'),
    path('faculties/', faculty_list, name='faculty_list'),
    path('facultiesp/', faculty_list_post, name='faculty_list_post'),
    path('faculties/<int:pk>/', faculty_detail, name='faculty_detail'),
    path('subjects/', subject_list, name='subject_list'),
    path('subjectsp/', subject_list_post, name='subject_list'),
    path('subjects/<int:pk>/', subject_detail, name='subject_detail'),
    path('subject-scores/', subject_score_list, name='subject_score_list'),
    path('subject-scores/<int:pk>/', subject_score_detail, name='subject_score_detail'),
    path('records/', record_list, name='record_list'),
    path('records/<int:pk>/', record_detail, name='record_detail'),
    path('calculate-scores/<int:faculty_id>/', calculate_scores, name='calculate_scores'),  # доданий новий маршрут

]
