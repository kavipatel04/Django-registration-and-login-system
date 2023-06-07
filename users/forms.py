from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile, User, Event, PointReport


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class SubmitPointsForm(forms.ModelForm):
    EVENT_OPTIONS = []
    for event in Event.objects.all():
        EVENT_OPTIONS.append((event, event.title))
    
    points_requested = forms.DecimalField(decimal_places=1, max_digits=2)
    event = forms.CharField(label='Event Name: ', widget=forms.Select(choices=EVENT_OPTIONS))
    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)

    print("Just ran submit points form class")
    class Meta:
        model = PointReport
        fields = ['points_requested', 'event']

    def create(self, data, my_user):
        print(data)
        print(my_user)
        my_event = None
        for event in Event.objects.all():
            if event.title == data['event']:
                my_event = event
                print(my_event)
                break
        
        PointReport.objects.create(user=my_user, event=my_event, points_requested=data['points_requested'], notes=data['notes'])


class SponsorVerificationForm(forms.ModelForm):
    myReports = PointReport.objects.filter(points_granted=0.0)
    points_approved = forms.DecimalField(decimal_places=1, max_digits=3)
    

    class Meta:
        model = PointReport
        fields = ['points_granted', 'verified_by']
    
    def load_user(self, my_user):
        self.user = my_user
        print(self.instance)

    def load_form(self):
        print("User is " + self.instance.first_name + " " + self.instance.last_name)
        for report in self.myReports:
            if self.instance.username == report.event.sponsor.username:
                self.event_name = report.event.title
                self.event_date = report.event.event_date
                self.points_requested = report.points_requested
                self.submitter_fname = report.user.first_name
                self.submitter_lname = report.user.last_name
    

    def update_verification(self, data):
        print(data)
    
    


