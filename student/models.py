from django.db import models

from api.models import User

class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    college = models.CharField(
        max_length=150,
        blank=True
    )

    qualification = models.CharField(
        max_length=100,
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now_add=True
    )



from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,**kwargs):

    if created and not instance.is_superuser:

        StudentProfile.objects.create(user = instance)

post_save.connect(create_student_profile,User)


