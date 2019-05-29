from .models import CustomUser
from django.db.models import Q

class AuthBackend(object):
    supports_object_permission    = True
    supports_anonymous_permission = False
    supports_inactive_user        = False


    def get_user(self, user_id):
        print('I GOT HERE')
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

    def authenticate(self, username=None, password=None):
        print('I ALSO GOT HERE')
        try:
            user =  CustomUser.objects.get(
                Q(username=username) | Q(email=username)
            )
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        if user.check_password(password):
            return user
        else: 
            raise exceptions.AuthenticationFailed('Wrong password')