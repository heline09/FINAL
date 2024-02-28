from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from internconnect.models import Internship
from accounts.models import Student, Skill
from django.contrib.auth.decorators import login_required
import requests


@login_required
def student_dashboard(request):
    student_skills = request.user.skills.all()
    internships = []
    for skill in student_skills:
        for internship in skill.internships.all():
            if internship not in internships: # to avoid repetition
                internships.append(internship)

    context = {
        'internships': internships,
    }

    return render(request, 'students/student_dashboard.html', context)


def applyPage(request):
    return render(request, 'students/apply.html')


# if request.method == "POST":
#         selected_field_of_study_id = request.POST.get("select_field_of_study")
#         skills = request.POST.get("skills")
#         print(f"{skills=}")
#         if skills is an array/list:
#             for skill_id in skills:
#         request.user.skills.add(Skill.objects.get(id=skill_id))

#         if skills is a single item/string:
#             skill_id = skills
#         request.user.skills.add(Skill.objects.get(id=skill_id))

#         return redirect('student_dashboard')