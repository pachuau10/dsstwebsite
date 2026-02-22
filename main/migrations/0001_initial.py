from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('icon', models.CharField(default='fas fa-chalkboard-teacher', max_length=60)),
                ('color', models.CharField(default='#1a3a6e', max_length=20)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', 'name'], 'verbose_name_plural': 'Gallery Categories'},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FeePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=20)),
                ('section', models.CharField(blank=True, max_length=5)),
                ('fee_type', models.CharField(choices=[('tuition', 'Tuition Fee'), ('exam', 'Exam Fee'), ('library', 'Library Fee'), ('sports', 'Sports Fee'), ('transport', 'Transport Fee'), ('misc', 'Miscellaneous')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('payment_method', models.CharField(default='online', max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('principal', 'Principal'), ('vice_principal', 'Vice Principal'), ('hod', 'Head of Department'), ('senior_teacher', 'Senior Teacher'), ('teacher', 'Teacher'), ('assistant_teacher', 'Assistant Teacher'), ('prt', 'Primary Teacher'), ('sports_coach', 'Sports Coach'), ('counsellor', 'Counsellor')], default='teacher', max_length=30)),
                ('qualification', models.CharField(blank=True, max_length=200)),
                ('experience_years', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('bio', models.TextField(blank=True)),
                ('subjects', models.CharField(blank=True, max_length=200)),
                ('achievements', models.TextField(blank=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('joined_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='main.department')),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lab_type', models.CharField(choices=[('science', 'Science Lab'), ('physics', 'Physics Lab'), ('chemistry', 'Chemistry Lab'), ('biology', 'Biology Lab'), ('computer', 'Computer Lab'), ('language', 'Language Lab'), ('math', 'Mathematics Lab'), ('art', 'Art & Craft Studio'), ('music', 'Music Room'), ('sports', 'Sports Facility'), ('library', 'Library'), ('other', 'Other')], max_length=20)),
                ('description', models.TextField()),
                ('capacity', models.IntegerField(default=0)),
                ('equipment', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='labs/')),
                ('is_featured', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labs_incharge', to='main.teacher')),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('academic', 'Academic'), ('sports', 'Sports'), ('arts', 'Arts & Culture'), ('science', 'Science & Technology'), ('social', 'Social Service'), ('other', 'Other')], max_length=20)),
                ('level', models.CharField(choices=[('school', 'School Level'), ('district', 'District Level'), ('state', 'State Level'), ('national', 'National Level'), ('international', 'International Level')], max_length=20)),
                ('description', models.TextField()),
                ('winner_name', models.CharField(blank=True, max_length=200)),
                ('winner_class', models.CharField(blank=True, max_length=50)),
                ('year', models.IntegerField(default=2024)),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievements/')),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-year', 'category']},
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='main.gallerycategory')),
            ],
            options={'ordering': ['order', '-uploaded_at']},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_type', models.CharField(choices=[('exam', 'Exam Notice'), ('result', 'Result'), ('information', 'Information'), ('event', 'Event'), ('holiday', 'Holiday Notice'), ('admission', 'Admission')], default='information', max_length=20)),
                ('content', models.TextField()),
                ('summary', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('is_pinned', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={'ordering': ['-is_pinned', '-created_at']},
        ),
    ]
