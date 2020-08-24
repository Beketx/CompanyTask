from django.urls import path

from good.views import GoodBySubCategoryIdAPIView, GoodDetailsAPIView, GoodFilter

urlpatterns = [

    path('', GoodFilter.as_view()),
    path('<int:good_id>/', GoodDetailsAPIView.as_view()),
    path('<int:subcategory_id>/subcategories/', GoodBySubCategoryIdAPIView.as_view()),

]