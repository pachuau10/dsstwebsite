from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Post, Teacher, Department, Lab, Achievement, GalleryCategory, GalleryImage


class Command(BaseCommand):
    help = 'Seeds the database with sample school data'

    def handle(self, *args, **kwargs):
        # Admin user
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser('admin', 'admin@school.edu', 'admin123')
            admin.first_name = 'School'; admin.last_name = 'Administrator'; admin.save()
        else:
            admin = User.objects.get(username='admin')
        self.stdout.write('✅ Admin user ready')

        # Departments
        depts_data = [
            ('Science', 'fas fa-flask', '#2e7d32'),
            ('Mathematics', 'fas fa-calculator', '#1a3a6e'),
            ('English', 'fas fa-pen', '#7b1fa2'),
            ('Social Studies', 'fas fa-globe', '#e65100'),
            ('Computer Science', 'fas fa-laptop', '#1565c0'),
            ('Physical Education', 'fas fa-running', '#c62828'),
            ('Arts & Music', 'fas fa-palette', '#ad1457'),
        ]
        depts = {}
        for i, (name, icon, color) in enumerate(depts_data):
            d, _ = Department.objects.get_or_create(name=name, defaults={'icon': icon, 'color': color, 'order': i})
            depts[name] = d
        self.stdout.write('✅ Departments seeded')

        # Teachers
        teachers_data = [
            ('Dr. Anand Kumar', 'principal', None, 'Ph.D (Education), M.A', 20, 'Visionary educationist with 20 years of leadership. Former CBSE resource person.', '', True, 1),
            ('Mrs. Sunita Sharma', 'vice_principal', 'Science', 'M.Sc Chemistry, B.Ed', 15, 'Expert in curriculum design and student mentorship.', 'Chemistry, Science', True, 2),
            ('Mr. Rajesh Gupta', 'hod', 'Mathematics', 'M.Sc Mathematics, B.Ed', 12, 'Makes mathematics fun and accessible for all students.', 'Mathematics, Statistics', True, 3),
            ('Ms. Priyanka Nair', 'hod', 'Science', 'M.Sc Physics, B.Ed', 10, 'Passionate physics teacher and science quiz coordinator.', 'Physics, Science', True, 4),
            ('Mrs. Kavita Singh', 'hod', 'English', 'M.A English, B.Ed, CELTA', 14, 'Literature enthusiast and debate team coordinator.', 'English, Literature', True, 5),
            ('Mr. Vivek Mishra', 'senior_teacher', 'Computer Science', 'MCA, B.Ed', 8, 'Full-stack developer turned educator. Leads coding club.', 'Computer Science, Python, Web Dev', True, 6),
            ('Ms. Anjali Rao', 'teacher', 'Science', 'M.Sc Biology, B.Ed', 6, 'Biology teacher and nature club in-charge.', 'Biology, Environmental Science', False, 7),
            ('Mr. Deepak Tiwari', 'teacher', 'Social Studies', 'M.A History, B.Ed', 9, 'History and civics teacher. School magazine editor.', 'History, Civics, Geography', False, 8),
            ('Ms. Ritu Agarwal', 'teacher', 'Mathematics', 'M.Sc, B.Ed', 5, 'Specializes in making complex topics simple.', 'Mathematics, Vedic Maths', False, 9),
            ('Mr. Sanjay Verma', 'sports_coach', 'Physical Education', 'B.P.Ed, NIS Certificate', 11, 'State-level cricket player and certified sports coach.', 'Cricket, Football, Athletics', False, 10),
            ('Ms. Pooja Mehta', 'teacher', 'Arts & Music', 'B.F.A, Diploma Music', 7, 'Classical vocalist and art teacher.', 'Fine Arts, Music, Dance', False, 11),
            ('Mrs. Neha Joshi', 'counsellor', None, 'M.A Psychology, RCI Certified', 8, 'School counsellor focused on student well-being and career guidance.', 'Counselling, Career Guidance', False, 12),
        ]
        teacher_objs = {}
        for name, desig, dept, qual, exp, bio, subjects, featured, order in teachers_data:
            dept_obj = depts.get(dept) if dept else None
            t, _ = Teacher.objects.get_or_create(name=name, defaults={
                'designation': desig, 'department': dept_obj, 'qualification': qual,
                'experience_years': exp, 'bio': bio, 'subjects': subjects,
                'is_featured': featured, 'order': order
            })
            teacher_objs[name] = t
        self.stdout.write('✅ Teachers seeded')

        # Labs
        labs_data = [
            ('Computer Laboratory – I', 'computer', 'Equipped with 60 high-performance desktops, high-speed internet, and smart board. Used for programming, robotics, and digital literacy sessions.', 60, 'Intel Core i7 PCs\nHigh-Speed Wi-Fi\nSmart Interactive Board\nProgramming Software (Python, Java, C++)\nRobotics Kits\nOnline Learning Platform', 'Block A, Ground Floor', True, 0),
            ('Physics Laboratory', 'physics', 'Well-equipped lab for practical experiments in mechanics, optics, electricity, and modern physics. Regular practical sessions for Classes IX–XII.', 40, 'Optical Bench & Lenses\nElectricity Apparatus\nVernier Callipers & Screw Gauge\nOscilloscope\nMechanics Trolleys\nSpectrometer', 'Block B, First Floor', True, 1),
            ('Chemistry Laboratory', 'chemistry', 'Modern chemistry lab with fume hoods, individual workstations, and a full range of reagents for organic and inorganic experiments.', 40, 'Fume Hood\nAnalytical Balance\nBunsen Burners\nGlass Apparatus Set\nChemical Reagents\nSafety Equipment', 'Block B, Ground Floor', True, 2),
            ('Biology Laboratory', 'biology', 'Spacious lab featuring microscopes, dissection tools, preserved specimens, models of human anatomy, and a mini greenhouse.', 40, 'Compound Microscopes (30)\nDissection Kits\nAnatomical Models\nPermanent Slides Collection\nMini Greenhouse\nDNA Model Kits', 'Block B, First Floor', True, 3),
            ('Mathematics Laboratory', 'math', 'Interactive maths lab with manipulatives, geometry boards, and educational software to make abstract concepts tangible.', 35, 'Geometry Boards\nTangrams & Puzzles\nGraph Plotters\nMath Software (GeoGebra)\nFraction Models\n3D Shape Models', 'Block C, Ground Floor', True, 4),
            ('School Library', 'library', 'A vast collection of 8000+ books, journals, e-books, and newspapers. Digital catalogue and reading lounge for students and staff.', 80, '8000+ Books\nDigital E-Library Access\nNewspapers & Magazines\nProject Reference Section\nComputers for Research\nQuiet Reading Pods', 'Block A, First Floor', True, 5),
            ('Sports & Fitness Centre', 'sports', 'Multi-sport facilities including a cricket ground, football field, basketball court, badminton court, and an indoor fitness room.', 200, 'Cricket Ground & Pitch\nFootball Field\nBasketball Court\nBadminton Courts (3)\nTT Tables\nIndoor Gym Equipment', 'Main Ground', True, 6),
            ('Language Laboratory', 'language', 'Digital language lab with audio-visual equipment for improving spoken English, Hindi, and foreign language proficiency.', 30, 'Individual Headphone Stations\nAudio-Visual Systems\nLanguage Software\nPronunciation Tools\nRecording Studio\nSmart Display', 'Block C, First Floor', True, 7),
            ('Art & Craft Studio', 'art', 'Creative studio with ample natural light, equipped with drawing materials, pottery wheel, and display boards for student artwork.', 30, 'Drawing Tables\nPottery Wheel\nPainting Supplies\nSculpture Materials\nDisplay Boards\nDigital Art Tablets', 'Block D, Ground Floor', True, 8),
            ('Music Room', 'music', 'Sound-proofed music room with classical and contemporary instruments for individual practice and group performances.', 20, 'Piano & Keyboard\nTabla & Mridangam\nGuitars (Acoustic & Electric)\nVocal Mics & PA System\nDrum Kit\nVioling & String Instruments', 'Block D, First Floor', True, 9),
        ]
        teacher_map = {'Computer Laboratory – I': 'Mr. Vivek Mishra', 'Physics Laboratory': 'Ms. Priyanka Nair', 'Chemistry Laboratory': 'Mrs. Sunita Sharma', 'Biology Laboratory': 'Ms. Anjali Rao', 'School Library': 'Mrs. Kavita Singh', 'Sports & Fitness Centre': 'Mr. Sanjay Verma'}
        for name, ltype, desc, cap, equip, loc, featured, order in labs_data:
            incharge = teacher_objs.get(teacher_map.get(name))
            Lab.objects.get_or_create(name=name, defaults={
                'lab_type': ltype, 'description': desc, 'capacity': cap,
                'equipment': equip, 'location': loc, 'is_featured': featured,
                'incharge': incharge, 'order': order
            })
        self.stdout.write('✅ Labs seeded')

        # Achievements
        achievements_data = [
            ('National Science Olympiad – Gold Medal', 'science', 'national', 'Priya Sharma won the Gold Medal at the National Science Olympiad 2024, competing against 5000+ students from 28 states.', 'Priya Sharma', 'Class X – A', 2024, True),
            ('State Chess Championship – 1st Place', 'sports', 'state', 'Arjun Mehta clinched the State Under-17 Chess Championship title, remaining undefeated in 8 rounds.', 'Arjun Mehta', 'Class IX – B', 2024, True),
            ('Best School Award – CBSE District', 'academic', 'district', 'Greenwood was awarded Best School in the District for 100% Board Results and holistic student development initiatives.', 'Greenwood Public School', '', 2024, True),
            ('National Dance Competition – 2nd Place', 'arts', 'national', 'Our cultural team secured 2nd place in the National Bharatnatyam Group Competition held in Bengaluru.', 'Cultural Team (12 students)', 'Mixed Classes', 2024, False),
            ('Inter-School Football Trophy', 'sports', 'district', 'Greenwood Football Team won the Annual Inter-School Football Championship for the third consecutive year.', 'Football Team', 'Classes VIII–X', 2024, True),
            ('INSPIRE Science Award', 'science', 'national', 'Ananya Roy received the prestigious INSPIRE Award from DST for her project on biodegradable plastics from agricultural waste.', 'Ananya Roy', 'Class XI – Science', 2024, True),
            ('State Debate Championship', 'academic', 'state', 'Our debate team secured 1st place in the State Inter-School Hindi Debate competition, defeating 45 schools.', 'Debate Team (3 students)', 'Class XII', 2023, False),
            ('CBSE Board – District Topper', 'academic', 'district', 'Rahul Gupta topped the district in CBSE Class X boards with 98.8%, achieving perfect scores in Mathematics and Science.', 'Rahul Gupta', 'Class X', 2024, False),
        ]
        for title, cat, level, desc, winner, wcls, year, featured in achievements_data:
            Achievement.objects.get_or_create(title=title, defaults={
                'category': cat, 'level': level, 'description': desc,
                'winner_name': winner, 'winner_class': wcls, 'year': year, 'is_featured': featured
            })
        self.stdout.write('✅ Achievements seeded')

        # Gallery Categories
        cats_data = [
            ('Annual Day', 'annual-day'),
            ('Sports Events', 'sports-events'),
            ('Science Exhibition', 'science-exhibition'),
            ('Cultural Programs', 'cultural-programs'),
            ('Campus Life', 'campus-life'),
            ('Labs & Infrastructure', 'labs-infrastructure'),
        ]
        for name, slug in cats_data:
            GalleryCategory.objects.get_or_create(slug=slug, defaults={'name': name})
        self.stdout.write('✅ Gallery categories seeded')

        # Posts
        posts = [
            ('Annual Examination Schedule 2024-25', 'exam', True, '''The Annual Examination for all classes is scheduled as follows:\n\nClasses I–V: December 1–10, 2024\nClasses VI–VIII: December 3–14, 2024\nClasses IX & XI: December 5–18, 2024\nClasses X & XII (Pre-Board): November 25 – December 5, 2024\n\nImportant Instructions:\n• Carry your admit card to the exam hall\n• No entry after 15 minutes of commencement\n• Mobile phones strictly prohibited\n• Arrive 30 minutes early''', 'Annual Exam scheduled Dec 1–18 for all classes. Detailed timetable at the school office.'),
            ('Mid-Term Result Declaration – October 2024', 'result', True, 'Results for all classes have been declared.\n\nReport cards will be distributed on November 20, 2024.\nParent-Teacher Meeting: November 25, 2024\n\nClass X Average: 78.5%\nClass XII Average: 80.2%\nDistrict Topper: Priya Sharma (Class X) – 98.6%', 'Mid-term results declared. Report cards on Nov 20. PTM on Nov 25.'),
            ('Admission Open for 2024-25', 'admission', True, 'Admissions are open for Nursery to Class XII.\n\nProcess:\n1. Obtain form from school office (₹200)\n2. Submit with documents\n3. Appear for admission test (Class II onwards)\n\nImportant Dates:\n• Forms: Oct 15 – Nov 30, 2024\n• Test: December 10–12\n• Result: December 20\n• Fee submission: January 10, 2025', 'Admissions open for 2024-25. Forms available till November 30.'),
            ('Annual Sports Day – December 15, 2024', 'event', False, 'Annual Sports Day on December 15, 2024.\n\nSchedule:\n8:00 AM – March Past\n9:00 AM – Track Events (Classes I–V)\n10:30 AM – Track Events (Classes VI–X)\n12:00 PM – Prize Distribution\n2:00 PM – Cultural Show\n\nChief Guest: Mr. Rajiv Mehta, District Sports Officer\nAll parents cordially invited!', 'Annual Sports Day on December 15. Track events, prize distribution, cultural show. Parents invited.'),
            ('Winter Holiday Schedule 2024', 'holiday', False, 'Winter Holidays: December 25, 2024 – January 5, 2025\n\nSchool Reopens: January 6, 2025 (Monday)\n\nLibrary open for Board students: December 28–29\nSports practice for district team: December 26–27\n\nWishing all a wonderful holiday season! 🎄', 'Winter break Dec 25 – Jan 5. School reopens January 6, 2025.'),
            ('Science Exhibition & Project Fair – Nov 28', 'event', False, 'Annual Science Exhibition on November 28, 2024.\n\nTheme: "Technology for Sustainable Future"\n\nOpen for Classes VI–XII\nRegistration deadline: November 20\n\nPrizes:\n🥇 1st: ₹5,000 + Trophy\n🥈 2nd: ₹3,000 + Trophy\n🥉 3rd: ₹1,500 + Trophy', 'Annual Science Exhibition Nov 28. Theme: Technology for Sustainable Future. Classes VI-XII.'),
            ('Fee Payment Reminder – November 2024', 'information', False, 'Fee Payment Due Date: November 15, 2024\nLate fee: ₹50 per day after due date\n\nPayment Methods:\n1. Online via Fee Portal on this website\n2. Cash at accounts office (9 AM – 2 PM)\n3. NEFT to school bank account\n\nFor queries: accounts@greenwoodschool.edu', 'November 2024 fee due by November 15. Late fee applies after due date.'),
        ]
        for title, ptype, pinned, content, summary in posts:
            Post.objects.get_or_create(title=title, defaults={
                'post_type': ptype, 'is_pinned': pinned, 'content': content,
                'summary': summary, 'author': admin, 'is_published': True
            })
        self.stdout.write('✅ Posts seeded')

        self.stdout.write(self.style.SUCCESS('\n🎉 All sample data seeded successfully!'))
        self.stdout.write('👉 Admin: http://127.0.0.1:8000/admin/ | Username: admin | Password: admin123')
        self.stdout.write('🌐 Website: http://127.0.0.1:8000')
