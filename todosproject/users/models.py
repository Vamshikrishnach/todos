from django.contrib.auth.models import AbstractUser
from django.db.models import CharField,IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    """
    Default custom user model for Todosproject.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = CharField(_("Email"), blank=True, max_length=255)
    otp = CharField("user otp",max_length=6, blank=True, null= True)
    
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

def generate_token(user):
    print(user)
    token = Token.objects.get_or_create(user=user)
    return token