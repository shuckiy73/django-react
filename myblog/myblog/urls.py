from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from blog.views import PostListView  # Импорт из приложения `blog`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', obtain_auth_token, name='api_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/pair/', TokenObtainPairView.as_view(), name='token_pair'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    # path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]