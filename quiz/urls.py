from django.urls import path
from .views import quiz_home, start_quiz, attempt_quiz, user_quiz_attempts, user_attempt_result

urlpatterns = [
    path('', quiz_home, name="quiz_home"),
    path("start/<int:id>/", start_quiz, name="start_quiz"),
    path("attempt/<int:id>/", attempt_quiz, name="attempt_quiz"),
    path("user/attempt-history/<int:quiz_id>/", user_quiz_attempts, name="attempt_history"),
    path("result/attempt/<int:id>/", user_attempt_result, name="attempt_result")
]
