from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Post(models.Model):
    POST_TYPES = [
        ('exam', 'Exam Notice'), ('result', 'Result'), ('information', 'Information'),
        ('event', 'Event'), ('holiday', 'Holiday Notice'), ('admission', 'Admission'),
    ]
    title = models.CharField(max_length=200)
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='information')
    content = models.TextField()
    summary = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = CloudinaryField('image', folder='posts/', blank=True, null=True)
    is_pinned = models.BooleanField(default=False)
    document = models.FileField(
    upload_to='documents/',
    storage=RawMediaCloudinaryStorage(),
    blank=True,
    null=True
    )
    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title


class FeePayment(models.Model):
    PAYMENT_STATUS = [('pending','Pending'),('completed','Completed'),('failed','Failed')]
    FEE_TYPES = [
        ('tuition','Tuition Fee'),('exam','Exam Fee'),('library','Library Fee'),
        ('sports','Sports Fee'),('transport','Transport Fee'),('misc','Miscellaneous'),
    ]
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=5, blank=True)
    fee_type = models.CharField(max_length=20, choices=FEE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=20, default='online')
    transaction_id = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')
    payment_date = models.DateTimeField(default=timezone.now)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.fee_type} - {self.amount}"


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', folder='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-uploaded_at']

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=60, default='fas fa-chalkboard-teacher')
    color = models.CharField(max_length=20, default='#1a3a6e')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    DESIGNATIONS = [
        ('principal','Principal'),('vice_principal','Vice Principal'),
        ('hod','Head of Department'),('senior_teacher','Senior Teacher'),
        ('teacher','Teacher'),('assistant_teacher','Assistant Teacher'),
        ('prt','Primary Teacher'),('sports_coach','Sports Coach'),('counsellor','Counsellor'),
    ]
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=30, choices=DESIGNATIONS, default='teacher')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers')
    qualification = models.CharField(max_length=200, blank=True)
    experience_years = models.IntegerField(default=0)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    photo = CloudinaryField('photo', folder='teachers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    subjects = models.CharField(max_length=200, blank=True)
    achievements = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    joined_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.get_designation_display()}"

    def get_subjects_list(self):
        return [s.strip() for s in self.subjects.split(',') if s.strip()]


class Lab(models.Model):
    LAB_TYPES = [
        ('science','Science Lab'),('physics','Physics Lab'),('chemistry','Chemistry Lab'),
        ('biology','Biology Lab'),('computer','Computer Lab'),('library','Library'),('other','Other'),
    ]
    name = models.CharField(max_length=100)
    lab_type = models.CharField(max_length=20, choices=LAB_TYPES)
    description = models.TextField()
    capacity = models.IntegerField(default=0)
    equipment = models.TextField(blank=True, help_text='One per line')
    location = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image', folder='labs/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    incharge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='labs_incharge')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_equipment_list(self):
        return [e.strip() for e in self.equipment.split('\n') if e.strip()]


class Achievement(models.Model):
    CATEGORIES = [
        ('academic','Academic'),('sports','Sports'),('arts','Arts & Culture'),
        ('science','Science & Technology'),('social','Social Service'),('other','Other'),
    ]
    LEVELS = [
        ('school','School Level'),('district','District Level'),('state','State Level'),
        ('national','National Level'),('international','International Level'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    level = models.CharField(max_length=20, choices=LEVELS)
    description = models.TextField()
    winner_name = models.CharField(max_length=200, blank=True)
    winner_class = models.CharField(max_length=50, blank=True)
    year = models.IntegerField(default=2024)
    image = CloudinaryField('image', folder='achievements/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-year', 'category']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class AdmissionApplication(models.Model):
    CLASSES = [(str(i), f'Class {i}') for i in range(1, 13)]
    CLASSES = [('nursery','Nursery'),('lkg','LKG'),('ukg','UKG')] + [(str(i), f'Class {i}') for i in range(1, 13)]
    GENDERS = [('male','Male'),('female','Female'),('other','Other')]
    BLOOD_GROUPS = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]
    STATUS = [('pending','Pending'),('under_review','Under Review'),('shortlisted','Shortlisted'),('admitted','Admitted'),('rejected','Rejected')]

    # Student Info
    student_name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=10, choices=GENDERS)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS, blank=True)
    applying_for_class = models.CharField(max_length=10, choices=CLASSES)
    previous_school = models.CharField(max_length=200, blank=True)
    previous_class = models.CharField(max_length=20, blank=True)
    previous_percentage = models.CharField(max_length=10, blank=True)

    # Parent Info
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_phone = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_phone = models.CharField(max_length=15, blank=True)

    # Contact
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    # Extra
    how_did_you_hear = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(blank=True)

    # System
    application_number = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    session = models.CharField(max_length=20, default='2024-25')

    class Meta:
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.application_number} – {self.student_name} – Class {self.applying_for_class}"

    def save(self, *args, **kwargs):
        if not self.application_number:
            import uuid
            self.application_number = 'GPS' + str(uuid.uuid4()).upper()[:8]
        super().save(*args, **kwargs)


class MarqueeItem(models.Model):
    text = models.CharField(max_length=300)
    emoji = models.CharField(max_length=10, default='📢')
    link_post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True, help_text='Link to a notice post')
    custom_url = models.CharField(max_length=200, blank=True, help_text='Custom URL e.g. /gallery/ (used if no post linked)')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.emoji} {self.text}"

    def get_url(self):
        if self.link_post:
            return f'/notices/{self.link_post.pk}/'
        return self.custom_url or None