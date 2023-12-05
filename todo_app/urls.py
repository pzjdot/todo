from django.urls import path
from . import views


urlpatterns = [
    # add_task
    path('addTask/', views.add_task, name="addTask"),
    # mark done
    path('mark_as_done/<int:pk>', views.mark_as_done, name="mark_as_done"),
    # mark undone
    path('mark_as_unDone/<int:pk>', views.mark_as_undone, name="mark_as_unDone"),
    # edit task
    path('edit_task/<int:pk>', views.edit_task, name="edit_task"),
    # delete task
    path('delete_task/<int:pk>', views.delete_task, name="delete_task"),
]