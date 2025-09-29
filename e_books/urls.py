from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',v.Usersignup,name='usersignup'),
    path('userlogin/',v.Userlogin,name='userlogin'),
    path('userhome/',v.Userhome,name='Userhome'),
    path('user_logout/',v.user_logout,name='user_logout'),
    path('addbook/',v.AddBook,name='addbook'),
    path('details/',v.Details,name='details'),
    path('update/<int:pk>/',v.Update,name='update'),
    path('delete/<int:pk>/',v.Book_delete,name='delete'),



    



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)