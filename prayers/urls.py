from django.urls import path
from .views import prayer_list, add_prayer, prayer_edit, DeletePrayerView, handle_amen, add_comment

urlpatterns = [    
    path('', prayer_list, name='home'), 
    path('add-prayer/', add_prayer, name='add_prayer'),
    path('edit-prayer/<int:pk>', prayer_edit, name='edit_prayer'),    
    path('delete-prayer/<int:pk>', DeletePrayerView.as_view(), name='delete_prayer'),    
    path('amen/<int:pk>', handle_amen, name='amen'),    
    path('blasphemy/<int:pk>', add_comment, name='comment'),    
]
