from django.urls import path, include

# {
#    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODQ4MDU3NiwianRpIjoiMDU2YTEwNDBhYTllNDdjZTgxM2NhOTIzMTlmNTE5ZDkiLCJ1c2VyX2lkIjoxfQ.geaPkazJgvCIjP6ecMvsBakVA2oaU9k4ftPQx4CVZm0",
#    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NjUzMzc2LCJqdGkiOiI1M2M5MTg5OWViYmY0NGIzODc4MDk1OTQ5NzgzZWNiOCIsInVzZXJfaWQiOjF9.a4FvS6V7TvhcI6SDdNEc4ouNTAYEoXYANl0ma857Kn8"
# }

urlpatterns = [
    path('v1/', include([
        # базовые, для управления пользователями в Django:
        path('auth/', include('djoser.urls')),
        # JWT-эндпоинты, для управления JWT-токенами:
        path('', include('djoser.urls.jwt')),



    ]))
]
