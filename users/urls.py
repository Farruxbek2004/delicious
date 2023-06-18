from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import (
    RegisterView,
    SendEmailVerificationCodeView,
    CheckEmailVerificationCodeView,
    CheckEmailVerificationCodeWithParams,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/geogle/', GoogleLogin.as_view(), name='google_login'),
    # path('token/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('email/verification/', SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path('email/check-verification/', CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path('email/check-verification-code/', CheckEmailVerificationCodeWithParams.as_view(), name="check-email")
]
