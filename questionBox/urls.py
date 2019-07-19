
from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=True)),
    path('index/', views.index, name='index'),
    path('question/<int:pk>/', views.question_detail, name='question'),
    path ('category-list/<int:category_pk>', views.questions_by_category, name='category-list'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.simple.urls')),
    path('markanswercorrect/', views.mark_answer_correct, name='markanswercorrect')
]

