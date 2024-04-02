from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import CustomerLoginForm,Password_Change_Form,Password_Set,Password_Reset

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('category/',views.Index.as_view(),name='index'),

    path('register/',views.CustomerRegisterView.as_view(),name='register'),
    path('account/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=CustomerLoginForm),name='login'),
    path('logout/',views.user_log_out,name='logout'),

    path('About-us/',views.About,name='About-us'),

    path('contact/',views.contact,name='contact'),


    path('password-change/',auth_view.PasswordChangeView.as_view(template_name='app/password_change.html',form_class=Password_Change_Form,success_url='/password-change-success/'),name='password-change'),
    path('password-change-success/',views.Password_Change_Success,name='Password-change-success'),

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=Password_Reset),name='password_reset'),
    path('password-reset-done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_confirm.html',form_class=Password_Set),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),



    path('profile/',views.Profile.as_view(),name='profile'),
    path('remove-address/<int:id>',views.Remove_Address,name='remove-address'),


    path('mobile/',views.Mobile,name='mobile'),
    path('mobile/<slug:data>',views.Mobile,name='mobile'),

    path('smart-watch/',views.SmartWatch,name='smart-watch'),
    path('smart-watch/<slug:data>',views.SmartWatch,name='smart-watch'),

    path('camera/',views.Camera,name='camera'),
    path('camera/<slug:data>',views.Camera,name='camera'),

    path('speaker/',views.Speaker,name='speaker'),
    path('speaker/<slug:data>',views.Speaker,name='speaker'),

    path('laptop/',views.Laptop,name='laptop'),
    path('laptop/<slug:data>',views.Laptop,name='laptop'),

    path('tablet/',views.Tablet,name='tablet'),
    path('tablet/<slug:data>',views.Tablet,name='tablet'),


    path('tv/',views.Tv,name='tv'),
    path('tv/<slug:data>',views.Tv,name='tv'),

    path('product-details/<int:id>',views.Product_details.as_view(),name='product-details'),

    path('add-to-cart/',views.Add_To_Cart,name='add-to-cart'),
    path('show-cart/',views.Show_Cart,name='show-cart'),
    path('remove-cart/',views.remove_cart,name='remove-cart'),
    path('update-cart/',views.update_cart,name='update_cart'),

    path('check-out/',views.Check_Out,name='check-out'),
    path('payment/',views.Payment,name='payments'),

    path('orderplace/',views.Payment,name='payment'),
    path('Order/',views.Order,name='order'),
    path('my-order/',views.My_Order,name='my-order'),
    path('cancel-order/<int:id>',views.Cancel_order,name='cancel-order'),


    path('search/',views.search,name='search'),

    path('feedback/',views.feedback,name='feedback'),
    #path('feedback-response/',views.feedback_response,name='feedback-replay'),
    path('feedback_thanks/',views.feed_thank,name='feedback_thanks'),
    path('my-feedback/',views.My_feedback,name='my-feedback')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)