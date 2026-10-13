from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

class Problem(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    LANGUAGE_CHOICES = [
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("java", "Java"),
    ("c", "C"),
    ("cpp", "C++"),
    ("csharp", "C#"),
    ("php", "PHP"),
    ("ruby", "Ruby"),
    ("go", "Go"),
    ("rust", "Rust"),
    ("kotlin", "Kotlin"),
    ("swift", "Swift"),
    ("typescript", "TypeScript"),
    ("sql", "SQL"),
  ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES
    )

    points = models.PositiveIntegerField(
        default=10
    )

    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="problems"
    )

    sample_input = models.TextField(
        blank=True
    )

    sample_output = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    