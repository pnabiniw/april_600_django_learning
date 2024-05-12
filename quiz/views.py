from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import OuterRef, Exists
from .models import Quiz, UserQuizAttempt, AttemptRecord


@login_required
def quiz_home(request):
    quizzes = Quiz.objects.all().prefetch_related("quiz_users").annotate(is_attempted=Exists(
        UserQuizAttempt.objects.filter(user=request.user, quiz_id=OuterRef("id"))
    ))
    for quiz in quizzes:
        print(quiz.is_attempted)
    return render(request, template_name="quiz/quiz_home.html", context={"quizzes": quizzes})


@login_required
def start_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    attempt = UserQuizAttempt.objects.create(quiz=quiz, user=request.user)
    return redirect("attempt_quiz", attempt.id)


@login_required
def attempt_quiz(request, id):
    attempt = UserQuizAttempt.objects.get(id=id)
    quiz = attempt.quiz
    questions = quiz.questions.all()
    if request.method == "POST":
        for question in questions:
            selected_answer = request.POST.get(f"selected_option_{question.id}")
            if not selected_answer:
                selected_answer = "Not Selected"
            AttemptRecord.objects.create(attempt=attempt, question=question, answer=selected_answer)
        messages.success(request, "Quiz completed successfully")
        return redirect("quiz_home")
    return render(request, template_name="quiz/attempt_quiz.html", context={"questions": questions, "attempt": attempt})


@login_required
def user_quiz_attempts(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    attempts = UserQuizAttempt.objects.filter(user=request.user, quiz=quiz).order_by('-id')
    return render(request, template_name="quiz/attempt_history.html", context={"attempts": attempts})


@login_required
def user_attempt_result(request, id):
    records = AttemptRecord.objects.filter(attempt_id=id)
    total_score = 0
    percentage = 0
    if records.exists():
        for record in records:
            if record.question.correct_answer == record.answer:
                total_score += 1

        percentage = total_score / records.count() * 100
    return render(request, template_name="quiz/attempt_result.html",
                  context={"records": records, "total_score": total_score, "percentage": round(percentage, 1)})
