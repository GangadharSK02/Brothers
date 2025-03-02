# users/management/commands/populate_db.py
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from courses.models import Course, CourseLevel, CourseCategory, Module, Lesson, Enrollment, CourseReview
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **kwargs):
        # Create some Course Levels and Categories
        levels = ["Beginner", "Intermediate", "Advanced"]
        categories = ["Science", "Technology", "Arts"]

        level_objs = [CourseLevel.objects.get_or_create(name=level)[0] for level in levels]
        category_objs = [CourseCategory.objects.get_or_create(name=cat)[0] for cat in categories]

        # Create Users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="Password123"
            )
            users.append(user)

        # Create Courses
        for _ in range(5):
            course = Course.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                level=random.choice(level_objs),
                category=random.choice(category_objs),
                instructor=random.choice(users),
                is_published=True,
                agreement_required=True,
                mentor_verified=random.choice([True, False]),
                is_personalized=random.choice([True, False])
            )

            # Create Modules for the course
            for m in range(1, 4):
                module = Module.objects.create(
                    course=course,
                    title=f"Module {m}: {fake.word()}",
                    description=fake.sentence(),
                    order=m
                )
                # Create Lessons for each module
                for l in range(1, 4):
                    lesson = Lesson.objects.create(
                        module=module,
                        title=f"Lesson {l}: {fake.word()}",
                        description=fake.paragraph(nb_sentences=2),
                        order=l
                    )
            # Create enrollments for the course
            for user in random.sample(users, k=3):
                Enrollment.objects.create(
                    user=user,
                    course=course,
                    progress=random.uniform(0, 100),
                    agreement_signed=True,
                    mentor_verified=random.choice([True, False])
                )
            # Create course reviews
            for user in random.sample(users, k=2):
                CourseReview.objects.create(
                    course=course,
                    user=user,
                    rating=random.randint(1, 5),
                    comment=fake.sentence(),
                )
        self.stdout.write(self.style.SUCCESS("Database populated with sample data."))
