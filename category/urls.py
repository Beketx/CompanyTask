from django.urls import path

from category.views import CategoryListAPIView, CategoryDetailAPIView, SubCategoriesByCategoryIdAPIView

urlpatterns = [

    path('', CategoryListAPIView.as_view()),
    path('<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('<int:category_id>/subcategories/', SubCategoriesByCategoryIdAPIView.as_view()),

]