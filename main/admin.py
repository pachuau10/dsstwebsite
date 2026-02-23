from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline
from .models import AdmissionClass, AdmissionDocument, AdmissionSession, MarqueeItem, Post, FeePayment, GalleryImage, GalleryCategory, Department, SiteSettings, Teacher, Lab, Achievement, ContactMessage, AdmissionApplication
from unfold.admin import ModelAdmin


@admin.register(Post)
class PostAdmin(UnfoldModelAdmin):
    list_display = ['title', 'post_type', 'author', 'is_published', 'is_pinned', 'created_at']
    list_filter = ['post_type', 'is_published', 'is_pinned']
    search_fields = ['title', 'content']
    list_editable = ['is_published', 'is_pinned']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(FeePayment)
class FeePaymentAdmin(UnfoldModelAdmin):
    list_display = ['student_name', 'student_id', 'class_name', 'fee_type', 'amount', 'status', 'payment_date']
    list_filter = ['fee_type', 'status', 'class_name']
    search_fields = ['student_name', 'student_id', 'transaction_id']
    readonly_fields = ['transaction_id', 'payment_date']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(UnfoldModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(GalleryImage)
class GalleryImageAdmin(UnfoldModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order', 'uploaded_at']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']


@admin.register(Department)
class DepartmentAdmin(UnfoldModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']


@admin.register(Teacher)
class TeacherAdmin(UnfoldModelAdmin):
    list_display = ['name', 'designation', 'department', 'experience_years', 'is_featured', 'order']
    list_filter = ['designation', 'department', 'is_featured']
    search_fields = ['name', 'subjects']
    list_editable = ['is_featured', 'order']


@admin.register(Lab)
class LabAdmin(UnfoldModelAdmin):
    list_display = ['name', 'lab_type', 'capacity', 'location', 'is_featured', 'order']
    list_filter = ['lab_type', 'is_featured']
    list_editable = ['is_featured', 'order']


@admin.register(Achievement)
class AchievementAdmin(UnfoldModelAdmin):
    list_display = ['title', 'category', 'level', 'year', 'winner_name', 'is_featured']
    list_filter = ['category', 'level', 'year', 'is_featured']
    list_editable = ['is_featured']
    search_fields = ['title', 'winner_name']


@admin.register(ContactMessage)
class ContactMessageAdmin(UnfoldModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    readonly_fields = ['submitted_at']


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(UnfoldModelAdmin):
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


@admin.register(MarqueeItem)
class MarqueeItemAdmin(UnfoldModelAdmin):
    list_display = ['emoji', 'text', 'link_post', 'custom_url', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ['admission_open', 'admission_open_date']
    
    # Unfold specific
    compressed_fields = True
    warn_unsaved_form = True

    fieldsets = (
        ("Admission Settings", {
            "fields": ("admission_open", "admission_open_date", "admission_closed_message"),
            "description": "Toggle admission form on/off from here.",
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
    

class AdmissionClassInline(TabularInline):
    model = AdmissionClass
    extra = 1

class AdmissionDocumentInline(TabularInline):
    model = AdmissionDocument
    extra = 1

@admin.register(AdmissionSession)
class AdmissionSessionAdmin(ModelAdmin):
    list_display = ['session_name', 'is_active', 'forms_open_date', 'forms_close_date']
    inlines = [AdmissionClassInline, AdmissionDocumentInline]
    compressed_fields = True
    warn_unsaved_form = True
    fieldsets = (
        ("Session", {
            "fields": ("session_name", "is_active", "closed_message", "next_open_date"),
        }),
        ("Important Dates", {
            "fields": ("forms_open_date", "forms_close_date", "admission_test_date", "result_date"),
        }),
        ("Fee Structure", {
            "fields": ("monthly_fee", "registration_fee", "admission_fee"),
        }),
    )