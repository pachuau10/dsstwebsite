from django.contrib import admin
from .models import Post, FeePayment, GalleryImage, GalleryCategory, Department, Teacher, Lab, Achievement, ContactMessage, AdmissionApplication


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_type', 'author', 'is_published', 'is_pinned', 'created_at']
    list_filter = ['post_type', 'is_published', 'is_pinned']
    search_fields = ['title', 'content']
    list_editable = ['is_published', 'is_pinned']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'student_id', 'class_name', 'fee_type', 'amount', 'status', 'payment_date']
    list_filter = ['fee_type', 'status', 'class_name']
    search_fields = ['student_name', 'student_id', 'transaction_id']
    readonly_fields = ['transaction_id', 'payment_date']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order', 'uploaded_at']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'department', 'experience_years', 'is_featured', 'order']
    list_filter = ['designation', 'department', 'is_featured']
    search_fields = ['name', 'subjects']
    list_editable = ['is_featured', 'order']


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ['name', 'lab_type', 'capacity', 'location', 'is_featured', 'order']
    list_filter = ['lab_type', 'is_featured']
    list_editable = ['is_featured', 'order']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'level', 'year', 'winner_name', 'is_featured']
    list_filter = ['category', 'level', 'year', 'is_featured']
    list_editable = ['is_featured']
    search_fields = ['title', 'winner_name']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    readonly_fields = ['submitted_at']


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'student_name', 'applying_for_class', 'father_name', 'father_phone', 'email', 'status', 'applied_at']
    list_filter = ['status', 'applying_for_class', 'gender', 'session']
    search_fields = ['application_number', 'student_name', 'father_name', 'email', 'father_phone']
    list_editable = ['status']
    readonly_fields = ['application_number', 'applied_at']
    fieldsets = (
        ('Student Information', {'fields': ('student_name', 'dob', 'gender', 'blood_group', 'applying_for_class', 'previous_school', 'previous_class', 'previous_percentage')}),
        ('Parent Information', {'fields': ('father_name', 'father_occupation', 'father_phone', 'mother_name', 'mother_occupation', 'mother_phone')}),
        ('Contact', {'fields': ('email', 'address', 'city', 'pincode', 'how_did_you_hear', 'remarks')}),
        ('Application Status', {'fields': ('application_number', 'status', 'session', 'applied_at')}),
    )
