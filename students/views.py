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
    if request.user.is_authenticated:
       student_skills = request.user.skills.all()
       internships = []
       for skill in student_skills:
         internships.extend(skill.internships.all())
       context = {
        'internships': set(internships),
    }
       print(internships)
       return render(request, 'students/student_dashboard.html', context)

    else:
        return redirect('signin')

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