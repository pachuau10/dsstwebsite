from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, FeePayment, Teacher, Department, Lab, GalleryImage, GalleryCategory, Achievement, ContactMessage
import uuid


def home(request):
    pinned_posts = Post.objects.filter(is_published=True, is_pinned=True)[:3]
    latest_posts = Post.objects.filter(is_published=True, is_pinned=False)[:6]
    exam_notices = Post.objects.filter(is_published=True, post_type='exam')[:3]
    featured_teachers = Teacher.objects.filter(is_featured=True)[:4]
    featured_achievements = Achievement.objects.filter(is_featured=True)[:6]
    featured_gallery = GalleryImage.objects.filter(is_featured=True)[:8]
    context = {
        'pinned_posts': pinned_posts,
        'latest_posts': latest_posts,
        'exam_notices': exam_notices,
        'featured_teachers': featured_teachers,
        'featured_achievements': featured_achievements,
        'featured_gallery': featured_gallery,
    }
    return render(request, 'main/home.html', context)


def notice_board(request):
    post_type = request.GET.get('type', '')
    search = request.GET.get('search', '')
    posts = Post.objects.filter(is_published=True)
    if post_type:
        posts = posts.filter(post_type=post_type)
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'main/notice_board.html', {
        'page_obj': page_obj, 'post_types': Post.POST_TYPES,
        'selected_type': post_type, 'search': search,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    related_posts = Post.objects.filter(is_published=True, post_type=post.post_type).exclude(pk=pk)[:4]
    return render(request, 'main/post_detail.html', {'post': post, 'related_posts': related_posts})


def fee_payment(request):
    if request.method == 'POST':
        transaction_id = 'TXN' + str(uuid.uuid4()).upper()[:12]
        payment = FeePayment.objects.create(
            student_name=request.POST.get('student_name'),
            student_id=request.POST.get('student_id'),
            class_name=request.POST.get('class_name'),
            section=request.POST.get('section', ''),
            fee_type=request.POST.get('fee_type'),
            amount=request.POST.get('amount'),
            month=request.POST.get('month', ''),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            payment_method=request.POST.get('payment_method'),
            transaction_id=transaction_id,
            remarks=request.POST.get('remarks', ''),
            status='completed',
        )
        messages.success(request, f'Payment successful! Transaction ID: {transaction_id}')
        return redirect('payment_receipt', pk=payment.pk)
    return render(request, 'main/fee_payment.html', {'fee_types': FeePayment.FEE_TYPES})


def payment_receipt(request, pk):
    payment = get_object_or_404(FeePayment, pk=pk)
    return render(request, 'main/payment_receipt.html', {'payment': payment})


def about(request):
    departments = Department.objects.all()
    leadership = Teacher.objects.filter(designation__in=['principal', 'vice_principal', 'hod']).order_by('order')
    return render(request, 'main/about.html', {'departments': departments, 'leadership': leadership})


def teachers(request):
    department_id = request.GET.get('dept', '')
    search = request.GET.get('search', '')
    departments = Department.objects.all()
    teacher_list = Teacher.objects.select_related('department').all()
    if department_id:
        teacher_list = teacher_list.filter(department_id=department_id)
    if search:
        teacher_list = teacher_list.filter(Q(name__icontains=search) | Q(subjects__icontains=search))
    # Group by designation order
    principal = teacher_list.filter(designation='principal').first()
    vp = teacher_list.filter(designation='vice_principal')
    hods = teacher_list.filter(designation='hod')
    staff = teacher_list.exclude(designation__in=['principal', 'vice_principal', 'hod'])
    paginator = Paginator(staff, 12)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'main/teachers.html', {
        'departments': departments, 'principal': principal, 'vps': vp,
        'hods': hods, 'page_obj': page_obj,
        'selected_dept': department_id, 'search': search,
    })


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'main/teacher_detail.html', {'teacher': teacher})


def labs(request):
    lab_list = Lab.objects.filter(is_featured=True).select_related('incharge')
    lab_type = request.GET.get('type', '')
    if lab_type:
        lab_list = lab_list.filter(lab_type=lab_type)
    return render(request, 'main/labs.html', {
        'labs': lab_list, 'lab_types': Lab.LAB_TYPES, 'selected_type': lab_type,
    })


def gallery(request):
    categories = GalleryCategory.objects.all()
    cat_slug = request.GET.get('cat', '')
    images = GalleryImage.objects.select_related('category').all()
    selected_cat = None
    if cat_slug:
        selected_cat = GalleryCategory.objects.filter(slug=cat_slug).first()
        if selected_cat:
            images = images.filter(category=selected_cat)
    paginator = Paginator(images, 20)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'main/gallery.html', {
        'categories': categories, 'page_obj': page_obj,
        'selected_cat': selected_cat, 'cat_slug': cat_slug,
    })


def achievements(request):
    category = request.GET.get('cat', '')
    level = request.GET.get('level', '')
    year = request.GET.get('year', '')
    ach_list = Achievement.objects.all()
    if category:
        ach_list = ach_list.filter(category=category)
    if level:
        ach_list = ach_list.filter(level=level)
    if year:
        ach_list = ach_list.filter(year=year)
    years = Achievement.objects.values_list('year', flat=True).distinct().order_by('-year')
    counts = {
        'total': Achievement.objects.count(),
        'national': Achievement.objects.filter(level__in=['national', 'international']).count(),
        'sports': Achievement.objects.filter(category='sports').count(),
        'academic': Achievement.objects.filter(category='academic').count(),
    }
    return render(request, 'main/achievements.html', {
        'achievements': ach_list, 'categories': Achievement.CATEGORIES,
        'levels': Achievement.LEVELS, 'years': years,
        'selected_cat': category, 'selected_level': level, 'selected_year': year,
        'counts': counts,
    })


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'), email=request.POST.get('email'),
            subject=request.POST.get('subject'), message=request.POST.get('message'),
        )
        messages.success(request, 'Your message has been sent! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'main/contact.html')


def admission(request):
    if request.method == 'POST':
        from .models import AdmissionApplication
        app = AdmissionApplication.objects.create(
            student_name=request.POST.get('student_name'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),
            blood_group=request.POST.get('blood_group', ''),
            applying_for_class=request.POST.get('applying_for_class'),
            previous_school=request.POST.get('previous_school', ''),
            previous_class=request.POST.get('previous_class', ''),
            previous_percentage=request.POST.get('previous_percentage', ''),
            father_name=request.POST.get('father_name'),
            father_occupation=request.POST.get('father_occupation', ''),
            father_phone=request.POST.get('father_phone'),
            mother_name=request.POST.get('mother_name'),
            mother_occupation=request.POST.get('mother_occupation', ''),
            mother_phone=request.POST.get('mother_phone', ''),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            pincode=request.POST.get('pincode'),
            how_did_you_hear=request.POST.get('how_did_you_hear', ''),
            remarks=request.POST.get('remarks', ''),
        )
        return redirect('admission_success', pk=app.pk)
    return render(request, 'main/admission.html')


def admission_success(request, pk):
    from .models import AdmissionApplication
    application = get_object_or_404(AdmissionApplication, pk=pk)
    return render(request, 'main/admission_success.html', {'application': application})
