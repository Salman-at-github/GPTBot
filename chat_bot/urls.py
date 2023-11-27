from django.urls import path
from chat_bot import views

urlpatterns = [
    path('test', views.test, name="test"),    
    path('home', views.home, name="home"),
    path('chatbot', views.chatbot, name="chatbot"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),

]
