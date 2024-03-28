from django import forms
from users.models import CustomUser
from django.core.mail import send_mail

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "username", "password")

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()

        # send email
        if user.email:
            send_mail(
                "Tabrik xati",
                f"Salom, {user.username}.\n Sizni saytimizdan o'rganligimizdan xursandmiz",
                "mukhammadjon4530@gmail.com",
                [user.email]
            )
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")



