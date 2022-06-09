from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from djangoProject import settings
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, \
    RegisterView, AllTasks

urlpatterns = [
                  path('login/', CustomLoginView.as_view(), name="login"),
                  path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('', TaskList.as_view(), name='tasks'),
                  path('all-tasks/', AllTasks.as_view(), name='all_tasks'),
                  path('task/<int:pk>', TaskDetail.as_view(), name='task'),
                  path('task-create/', TaskCreate.as_view(), name='task_create'),
                  path('task-update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
                  path('task-delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
