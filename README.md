# 🏫 Greenwood Public School – Complete Django Website

A fully-featured, mobile-responsive school website built with Django.

---

## 📄 Pages

| URL | Page |
|-----|------|
| `/` | Home (Hero, Notices, Teachers preview, Labs, Gallery, Achievements) |
| `/about/` | About School, Vision/Mission, Departments, Leadership |
| `/teachers/` | All Teachers (filterable by dept, searchable) |
| `/teachers/<id>/` | Teacher Detail Page |
| `/labs/` | Labs & Facilities (10 labs with details) |
| `/gallery/` | Photo Gallery with Lightbox & category filters |
| `/achievements/` | Awards & Achievements with filters |
| `/notices/` | Notice Board (Exam/Result/Event/Holiday/Info/Admission) |
| `/notices/<id>/` | Notice Detail |
| `/fee-payment/` | Fee Payment Portal |
| `/fee-payment/receipt/<id>/` | Printable Payment Receipt |
| `/contact/` | Contact Form |
| `/admin/` | Django Admin |

---

## 🚀 Quick Start

```bash
cd school_website
pip install django pillow
python manage.py migrate
python manage.py seed_data    # Creates admin + all sample data
python manage.py runserver
```

Open: **http://127.0.0.1:8000**
Admin: **http://127.0.0.1:8000/admin/** → `admin` / `admin123`

---

## 📱 Mobile Features
- Fully responsive Bootstrap 5 layout
- Collapsible hamburger menu with dropdowns
- Touch-friendly gallery lightbox
- Mobile-optimized cards and grids
- Back-to-top button
- All pages tested at 320px–1440px

## 🗂️ Models
- **Post** – Notice board entries (6 types)
- **Teacher** – Staff with designation, dept, subjects, photo
- **Department** – Academic departments
- **Lab** – Labs & facilities with equipment list
- **GalleryImage / GalleryCategory** – Photo gallery
- **Achievement** – Awards with category & level
- **FeePayment** – Fee records with transaction ID
- **ContactMessage** – Contact form submissions

## 🎨 Design
- Primary: Deep Navy `#1a3a6e`
- Accent: Gold `#e8a020`
- Font: Poppins + Playfair Display
- Bootstrap 5 + Font Awesome 6
- Animated hero, floating card, marquee ticker

## ⚙️ Production Checklist
- Set `DEBUG = False` in `settings.py`
- Change `SECRET_KEY` to a secure random value
- Configure `ALLOWED_HOSTS`
- Use PostgreSQL for production
- Run `python manage.py collectstatic`
- Deploy with gunicorn + nginx
