# from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.dispHome),
    path('home/', views.dispHome),
    path('Universities/IIS-Bangalore/', views.dispIIS),
    path('Universities/Jawaharlal-Nehru-University/', views.dispJnu),
    path('Universities/Jamia-Millia-Islamia-University/', views.dispJmiu),
    path('Universities/Jadavpur-University/', views.dispJadavpur),
    path('Universities/Jadavpur-University/Engineering-&-Technology/', views.dispJDPEngTech),
    path('Universities/Jadavpur-University/Science/', views.dispJDPSci),
    path('Universities/Jadavpur-University/ISLM/', views.dispJDPISLM),
    # path('Universities/Jadavpur-University/Arts/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/Engineering-&-Technology/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/Science/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/ISLM/', include("CalendarHome.urls")),
    path('Universities/Amrita-Vishwa-Vidyapeetham/', views.dispAVV),
    path('Universities/VIT/', views.dispVIT),
    path('Universities/BHU/', views.dispBHU),
    path('Universities/DUpost/', views.dispDUpost),
    path('Universities/DUunder/', views.dispDUunder),
    path('Universities/University-Of-Hyderabad/', views.dispUOH),
    path('Universities/Amity/', views.dispAmity),
    path('Universities/Bharathiar-University/', views.dispBU),
    path('Universities/Panjab-University/', views.dispPU),
    path('Universities/Mysore-University/', views.dispMysore),
    path('Universities/Chandigarh-University/', views.dispCU),
    path('Universities/Andhra-University/', views.dispAU),
    path('Universities/Guru-Nanak-Dev-University/', views.dispGNDU),
    path('Universities/University-Of-Kashmir/', views.dispKashmir),
    path('Universities/University-Of-Jammu/', views.dispJammu),
    path('Universities/Pondicherry-University/', views.dispPondicherry),
    path('Universities/Tezpur-University/', views.dispTezpur),
    path('Universities/Gauhati-University/', views.dispGauhati),
    path('aboutUs/', views.dispAboutUs),
    path('filter-by-date/', views.dispFilter),
    path('filter-by-date/<str:date>/', views.filter_by_date, name='filter_by_date'),
    path('chatbot/', views.dispChatbot),
    path('logout/', views.dispLogout, name='logout'),
    path('signUp/', views.dispSignUp, name='signUp'),
    path('login', views.dispLogin, name='login'),
    path('profile/', views.dispProfile),
]
