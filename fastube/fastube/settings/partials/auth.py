AUTH_USER_MODEL = "users.User"

LOGIN_UTL = "/login/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입이 되었습니다"
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인이 되었습니다."
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다."

AUTHENTICATION_BACKENDS = [
    "social.backends.facebook.FacebookOAuth2",

    "django.contrib.auth.backends.ModelBackend",
]
