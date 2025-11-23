🏠 InvestoXpert — Real Estate Property Search Platform

A full-stack Django-based real estate platform where users can search residential properties by State → City → Locality → BHK, view property details, explore images, amenities, configurations, and see location using Google Maps.

🚀 Features
🔍 Property Search

Users can filter properties dynamically using:

State

City

Locality

BHK (1BHK / 2BHK / 3BHK)

Live search submit using GET parameters

🗺 Google Maps Integration

Each property page includes:

Clean responsive map

Google Maps embed

Automatic fallback due to invalid URLs

🏘 Property Detail Page

Every property contains:

Title & Images

Full Description

About Section

Configuration Details

Amenities List

Developer Info

Price Range (Min/Max)

Location Map

📱 Fully Responsive Frontend

Built using:

Bootstrap 5

Custom CSS

Mobile Hero Background

Desktop Background

✔ Admin Panel Enabled

Through Django admin, you can manage:

States

Cities

Localities

Properties

All advanced fields (About, Amenities, Developer, Map URL)

🛠 Tech Stack
Category	Technology
Backend	Django 5.2
Database	SQLite3 (default)
Frontend	HTML5, CSS3, Bootstrap 5
APIs	Google Maps Embed
Deployment	GitHub (local project)
📁 Project Structure
investoexpert/
│── assigment/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates/
│   │   └── home.html
│   └── ...
│
│── home/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── property_detail.html
│
│── db.sqlite3
│── manage.py
│── venv/
└── README.md

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/Rishavkumar720/investoxpert.git
cd investoxpert

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Start Server
python manage.py runserver

🧪 Property Data Example (Admin Panel)
State
Uttar Pradesh
Delhi
Maharashtra
New State

City
Noida (Uttar Pradesh)
New Delhi (Delhi)
New City (New State)

Locality
Noida Sector 137
Moti Nagar, New Delhi
New Locality

Property Example
Field	Value
Title	Paras Tierea, Sector 137 Noida
Description	Affordable 2 & 3 BHK flats near Noida Expressway
BHK	2 BHK
Price Min	70 Lac
Price Max	90 Lac
Image	https://i.ibb.co/0X8Ghwz/noida-sector-137.jpg
About	Perfect for families & IT professionals
Configuration	2BHK – 825 sqft / 3BHK – 1100 sqft
Amenities	Swimming Pool, Gym, Clubhouse
Developer	Paras Buildtech
Map URL	Valid Google map embed link
🔗 Google Maps Embed Example

Use this format:

https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!...

📸 Popular Cities (Homepage Featured Images)

Image links used:

City	Image
Noida	https://images.unsplash.com/photo-1581092339155-1c4f6e9f52de

Gurugram	https://images.unsplash.com/photo-1567690187548-bce7fbbf67d2

Delhi	https://images.unsplash.com/photo-1587985203268-3ac41bbadd6c

Mumbai	https://images.unsplash.com/photo-1524492412937-b28074a5d7da

Bangalore	https://images.unsplash.com/photo-1656754210241-c42e6f0a3b27

Pune	https://images.unsplash.com/photo-1596178060671-7a80dcffa5bb
🎥 Testimonial Video Embed
<iframe 
  src="https://www.youtube.com/embed/fhxW8SoOZfA" 
  allowfullscreen>
</iframe>

🌐 Deployment

Project is GitHub-ready and can be deployed on:

PythonAnywhere

Railway

Render

Heroku (Docker required)

🤝 Contribution

Pull Requests are welcome!
Follow the code style and always create feature branches.

📞 Contact

Developer: Rishav Kumar
GitHub: https://github.com/Rishavkumar720

Project: InvestoXpert Real Estate Platform
