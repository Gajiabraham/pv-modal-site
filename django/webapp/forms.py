# from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# class CustomAuthenticationForm(AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         if not user.is_staff:
#             raise forms.ValidationError(
#                 "Only staff members are allowed to log in."
#             )
