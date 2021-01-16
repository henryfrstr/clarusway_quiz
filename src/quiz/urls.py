from django.urls import path
from .views import CategoryList, CategoryDetail, QuizDetail

urlpatterns = [
    path("category/", CategoryList.as_view(), name="category"),
    path("category/<category>/", CategoryDetail.as_view(), name="category-detail"),
    path("question/<title>/", QuizDetail.as_view(), name="question")
]
