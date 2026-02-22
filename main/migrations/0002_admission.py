from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5)),
                ('applying_for_class', models.CharField(max_length=10)),
                ('previous_school', models.CharField(blank=True, max_length=200)),
                ('previous_class', models.CharField(blank=True, max_length=20)),
                ('previous_percentage', models.CharField(blank=True, max_length=10)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100)),
                ('father_phone', models.CharField(max_length=15)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(blank=True, max_length=100)),
                ('mother_phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('how_did_you_hear', models.CharField(blank=True, max_length=100)),
                ('remarks', models.TextField(blank=True)),
                ('application_number', models.CharField(blank=True, max_length=20, unique=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('under_review', 'Under Review'), ('shortlisted', 'Shortlisted'), ('admitted', 'Admitted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.CharField(default='2024-25', max_length=20)),
            ],
            options={'ordering': ['-applied_at']},
        ),
    ]
