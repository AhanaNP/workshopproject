from django.urls import path

from new_app import views, manager_views, customer_views, admin_views

urlpatterns = [
   path('',views.home,name='home'),
   path('dash',views.dash,name='dash'),
   path('customer_reg',views.customer_reg,name='customer_reg'),
   path('manager',views.manager_login,name='manager'),
   path('adminpage',views.adminpage,name='adminpage'),
   path('managerpage',views.managerpage,name='managerpage'),
   path('customerpage',views.customerpage,name='customerpage'),
   path('view_login',views.login_view,name='view_login'),
   path('customertable',views.customertable,name='customertable'),
   path('managertable',views.managertable,name='managertable'),
   path('managerupdate<int:id>/',views.managerupdate,name='managerupdate'),
   path('managerdelete<int:id>/',views.managerdelete,name='managerdelete'),
   path('customerdelete<int:id>/',views.customerdelete,name='customerdelete'),
   path('profile_view',manager_views.profile_view, name='profile_view'),
   path('customer_profile',customer_views.customer_profile,name='customer_profile'),
   path('feedback',customer_views.feedback,name='feedback'),
   path('customer_feedback',admin_views.customer_feedback,name='customer_feedback'),
   path('feedback_view',customer_views.feedback_view,name='feedback_view'),
   path('feedupdate<int:id>/',admin_views.reply_feedback,name='feedupdate'),
   path('schedule',admin_views.scheduledetails,name='schedule'),
   path('scheduledata',admin_views.scheduledata,name='scheduledata'),
   path('disable<int:id>/',admin_views.disable,name='disable'),
   path('slotschedule',customer_views.slotschedule,name='slotschedule'),
   path('bookingschedule<int:id>/',customer_views.bookingschedule,name='bookingschedule'),
   path('customer_bookingview',customer_views.customer_bookingview,name='customer_bookingview'),
   path('booking_view',manager_views.booking_view,name='booking_view'),
   path('approval<int:id>/',manager_views.approval,name='approval'),
   path('reject<int:id>/',manager_views.reject,name='reject'),
   path('approved',admin_views.approved_view,name='approved'),
   path('creatework<int:id>/',admin_views.creatework,name='creatework'),
   path('manager_workview',manager_views.manager_workview,name='manager_workview'),
   path('managerworkupdate<int:id>/',manager_views.managerworkupdate,name='managerworkupdate'),
   path('workstatus',customer_views.workstatus,name='workstatus'),
   path('payment_field<int:id>/',customer_views.payment_field,name='payment_field')

]