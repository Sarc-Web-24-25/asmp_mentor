# Generated by Django 4.2.2 on 2023-06-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asmp_reg", "0013_alter_registration_dept_mentees"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="registration",
            name="dept_mentees",
        ),
        migrations.AddField(
            model_name="registration",
            name="dept_mentees",
            field=models.ManyToManyField(
                blank=True,
                choices=[
                    ("No_preference_as_such", "No preference as such"),
                    ("Aerospace_Engineering", "Aerospace Engineering"),
                    ("Biosciences_&Bioengineering", "Biosciences & Bioengineering"),
                    (
                        "Centre_for_Policy_Studies-CPS",
                        "Centre for Policy Studies - CPS",
                    ),
                    (
                        "Centre_for_Urban_Science&Engineering-C-USE",
                        "Centre for Urban Science & Engineering - C-USE",
                    ),
                    (
                        "Centre_of_Studies_in_Resources_Engineering-CSRE",
                        "Centre of Studies in Resources Engineering - CSRE",
                    ),
                    ("Chemical_Engineering", "Chemical Engineering"),
                    ("Chemistry", "Chemistry"),
                    ("Civil_Engineering", "Civil Engineering"),
                    ("Climate_Studies", "Climate Studies"),
                    ("Computer_Science&Engineering", "Computer Science & Engineering"),
                    (
                        "Desai_Sethi_Centre_for_Entrepreneurship-DSCE",
                        "Desai Sethi Centre for Entrepreneurship - DSCE",
                    ),
                    ("Earth_Sciences", "Earth Sciences"),
                    ("Educational_Technology", "Educational Technology"),
                    ("Electrical_Engineering", "Electrical Engineering"),
                    ("Energy_Science&Engineering", "Energy Science & Engineering"),
                    ("Humanities&Social_Science", "Humanities & Social Science"),
                    ("IITB-Monash_Research_Academy", "IITB-Monash Research Academy"),
                    ("Industrial_Design_Centre", "Industrial Design Centre"),
                    ("Mathematics", "Mathematics"),
                    ("Mechanical_Engineering", "Mechanical Engineering"),
                    (
                        "Metallurgical_Engineering&_Materials_Science",
                        "Metallurgical Engineering & Materials Science",
                    ),
                    ("Physics", "Physics"),
                    (
                        "Shailesh_J.Mehta_School_of_Management",
                        "Shailesh J. Mehta School of Management",
                    ),
                    ("Systems&_Control_Engineering", "Systems & Control Engineering"),
                    ("CESE", "CESE"),
                    ("Other", "Other"),
                ],
                to="asmp_reg.department",
            ),
        ),
    ]
