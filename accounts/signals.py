from django.db.models.signals import post_save  #import post_save signal
from django.dispatch import receiver  #import receiver decorator
#import the user model
from .models import userprofile ,User #import the userprofile model

#    always try to managee signas in signal.py file for better management of signals
#   and import them in apps.py file  for now we are using signals in models.py file

@receiver(post_save,sender=User)  #post_save signal decorator
# def create_profile_receiver(**kwargs):  #post_save signal receiver
#     if kwargs['created']:
#         user_profile=userprofile.objects.create(user=kwargs['instance'])
#         user_profile.save()
#     else:
#         pass
#above will also work but
#below is the better way to write the receiver function
def create_profile_receiver(sender,instance,created,**kwargs):  #post_save signal receiver
    if created:  # Use the parameter directly
        user_profile=userprofile.objects.create(user=instance)  # Use instance parameter directly
        user_profile.save()
    else:
        try:
            user_profile=userprofile.objects.get(user=instance)  # Use instance parameter directly
            user_profile.save()
            pass
        except:
            user_profile=userprofile.objects.create(user=instance)
            user_profile.save()

# post_save.connect(create_profile_receiver,sender=User)  #connect the signal with the receiver  use this line if you are not using the decorator
#this signal will create a user profile for every user that is created
