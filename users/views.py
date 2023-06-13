from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, SubmitPointsForm, SponsorVerificationForm


def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def submit_points(request):
    if request.method == 'POST':
        points_form = SubmitPointsForm(request.POST, instance=request.user)
        points_form.load_events()
        print("Ran 1")
        if points_form.is_valid():
            if (points_form.get_e_code_match(points_form.cleaned_data)):
                if (points_form.verify_points(points_form.cleaned_data)):
                    my_message = 'Your points submission has been successfully submitted.'
                    points_form.create(points_form.cleaned_data, request.user, points_form.cleaned_data['points_requested'])
                else:
                    my_message = 'Your points form has been submitted!'
                    points_form.create(points_form.cleaned_data, request.user, 0)
            else:
                my_message = 'Your points form has been submitted!'
                points_form.create(points_form.cleaned_data, request.user, 0)

            messages.success(request, my_message)
            
            
            return redirect(to='users-points')
    else:
        points_form = SubmitPointsForm(instance=request.user)
        points_form.load_events()
        print("Ran 2")

    return render(request, 'users/points.html', {'points_form': points_form})
    
@login_required
def verify_points(request):
    if request.method == 'POST':
        sponsor_form = SponsorVerificationForm(request.POST, instance=request.user)
        sponsor_form.load_form()
        
        if sponsor_form.is_valid():
            sponsor_form.update_verification(sponsor_form.cleaned_data)
            sponsor_form.submit(sponsor_form.cleaned_data)
            messages.success(request, 'Your points submission has been successfully sent')
            return redirect(to='users-verifications')
    else:
        sponsor_form = SponsorVerificationForm(instance=request.user)
        sponsor_form.load_form()

    return render(request, 'users/verifications.html', {'sponsor_form': sponsor_form})