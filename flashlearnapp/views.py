from django.shortcuts import render
from .forms import TextInputForm
from .summarizer import generate_dynamic_summary, generate_questions_and_answers
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, "landing.html")  # Otherwise, show the landing page

def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        # Check if the email is already taken
        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists. Please sign in.")
            return render(request, "signup.html")

        try:
            # Create the user with email as both username and email field
            myuser = User.objects.create_user(username=email, email=email, password=password1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            messages.success(request, "Your account has been successfully created.")
            return redirect("signin")

        except IntegrityError:
            messages.error(request, "An error occurred during account creation. Please try again.")
            return render(request, "signup.html")

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']

        user = authenticate(username=email, password=password1)

        if user is not None:
            login(request, user)
            return redirect('flashlearnapp')  # Redirect to the flashcards view
        else:
            messages.error(request, "Invalid Credentials! Please try again.")
            return redirect('signin')  # Redirect back to the sign-in page

    return render(request, "signin.html")

def flashcards_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            summary = generate_dynamic_summary(text)
            qa_pairs = generate_questions_and_answers(summary)
            return render(request, 'flashcards.html', {'summary': summary, 'qa_pairs': qa_pairs})
    else:
        form = TextInputForm()
    return render(request, 'input.html', {'form': form})
