from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Registration
from django.core.exceptions import ValidationError
import csv
from rest_framework.decorators import api_view
from . import options
from django.views.decorators.csrf import csrf_exempt


def export(request):
	response = HttpResponse(content_type='text/csv')
	writer = csv.writer(response)
	writer.writerow([
            'Fullname',
            'Roll No',
            'Department',
            'Other department',
            'degree',
            'Other Degree',
            'Graduation Year',
            'Contact',
            'Email',
            'Option',
            'Designation',
            'Company Name',
            'University Name',
            'experience',
            'Preference 1',
            'Preference 2',
            'Preference 3',
            'Core',
            'Core Subdivision',
            'Preferred mentees',
            'Suggestions',
            'Recommendations',
        ])
	for registration in Registration.objects.all().values_list(
            'fullname',
            'rollno',
            'department',
            'department_other',
            'degree',
            'degree_other',
            'graduation_year',
            'contact',
            'email',
            'placementOrGrad',
            'designation',
            'company_name',
            'university_name',
            'experience',
            'field_pref1',
            'field_pref2',
            'field_pref3',
            'branch',
            'branch_subdivision',
            'preferred_mentees',
            'suggestions',
            'alumni_recommendations'
        ):
		writer.writerow(registration)

	response['Content-Disposition'] = 'attachment; filename="mentors_pmp23.csv"'
	return response


def index(request):
    return render(request, 'AsmpReg/home.html')


def phonehome(request):
    return render(request, 'AsmpReg/phonehome.html')


@csrf_exempt
def mentorReg(request):

    def __str__(self):
        return self.fullname

    if request.method == 'POST':

        fullname = request.POST.get('fullname')
        rollno = request.POST.get('rollno')
        department = request.POST.get('department')
        department_other = request.POST.get('other_department')
        degree = request.POST.get('degree')
        degree_other = request.POST.get('degree_other')
        graduation_year = request.POST.get('graduation_year')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        placementOrGrad = request.POST.get('placementOrGrad')

        field_pref3 = "NA"

        if (placementOrGrad == 'placement'):
            experience = request.POST.get('placementExperience')
            field_pref1 = request.POST.get('placementPref1')
            field_pref2 = request.POST.get('placementPref2')
            field_pref3 = request.POST.get('placementPref3')
        else:
            experience = request.POST.get('gradExperience')
            field_pref1 = request.POST.get('gradPref1')
            field_pref2 = request.POST.get('gradPref2')

        designation = request.POST.get('designation')
        company_name = request.POST.get('company_name')

        university = request.POST.get('university_name')

        suggestions = request.POST.get('suggestion')

        recommendations = request.POST.get('referral')

        core_branch = request.POST.get('core')
        branch_subdivision = request.POST.get('subdivisions')

        print(branch_subdivision)

        preferred_mentees = request.POST.get('no_of_mentees')

        registration = Registration(fullname=fullname or "NA", email=email or "NA", department=department or "NA", rollno=rollno or "NA", department_other=department_other or "NA",
                                    degree=degree or "NA", degree_other=degree_other or "NA", graduation_year=graduation_year or "NA", field_pref3=field_pref3 or "NA",
                                    contact=contact or "NA", placementOrGrad=placementOrGrad or "NA", designation=designation or "NA", company_name=company_name or "NA", experience=experience or "NA", field_pref1=field_pref1 or "NA", field_pref2=field_pref2 or "NA", branch=(core_branch or "NA"), branch_subdivision=(branch_subdivision or "NA"), preferred_mentees=preferred_mentees or "NA", university_name=(university or "NA"), suggestions=suggestions or "NA", alumni_recommendations=recommendations or "NA")

        registration.save()

        return render(request, 'AsmpReg/thank.html')


    context = {
        'options': options.__dict__,
    }

    return render(request, 'AsmpReg/form.html', context)


def thank(request):
    return render(request, 'AsmpReg/thank.html')


@api_view(['POST'])
def testapi(request):
    req_data = request.data
    alumni_id = req_data['id']
    duration = req_data['duration']
    context = {'alumni_id': alumni_id, 'duration': duration}
    return render(request, 'thank.html', context)
