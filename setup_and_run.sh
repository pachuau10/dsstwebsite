#!/bin/bash
echo "🏫 Setting up Greenwood Public School Website..."
echo ""
echo "📦 Installing dependencies..."
pip install django pillow
echo ""
echo "🗄️ Running migrations..."
python manage.py migrate
echo ""
echo "🌱 Seeding sample data..."
python manage.py seed_data
echo ""
echo "✅ Setup complete! Open: http://127.0.0.1:8000"
echo "   Admin: http://127.0.0.1:8000/admin/ | admin / admin123"
echo ""
python manage.py runserver
