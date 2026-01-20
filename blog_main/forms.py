from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# extend user creation form and create our own user
class RegistrationForm(UserCreationForm):
    class Meta:
        # create model using user
        model=User
        fields=('email','username','password1','password2')
        # we need to load this form 