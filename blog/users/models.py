from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify  
from PIL import Image
from .validators import validate_age,validate_ref_code
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from django.core.validators import MinLengthValidator
from .utils import generate_ref_code
# Create your models here.

        
class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True, blank=False, null=False
    )
    first_login = models.BooleanField(default=True)
    birthdate = models.DateField(blank=None, null=None,max_length=50,validators=[validate_age])
    ref = models.CharField(max_length=12,blank=True, null=True,validators=[validate_ref_code])
    REQUIRED_FIELDS = ["email", "birthdate","ref"]

    def save(self, *args, **kwargs):
        if not self.id and not self.is_superuser:
            self.is_active = False 

        super().save(*args, **kwargs)

        
    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,validators=[MinLengthValidator(10,)])
    image = models.ImageField(upload_to='profiles/',blank=True,null=True,default='default/profile.png')
    biography = models.TextField(blank=True,null=True,max_length=250)
    username = models.CharField(editable=False,max_length=50)
    hits = GenericRelation(HitCount, object_id_field='object_pk')
    ref_code = models.CharField(max_length=12,blank=True)
    recommended_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="recommended_user")

    def save(self, *args, **kwargs) -> None:
        self.username = self.user.username

        if self.image != None:
            img = Image.open(self.image.path)
            if img.height > 512 or img.width > 512:
                img.thumbnail((512, 512))
                img.save(self.image.path)   
        
        if self.ref_code != None:
            code = generate_ref_code()
            self.ref_code = code

        super(Profile, self).save(*args, **kwargs)

    def hits_count(self):
        hit_count = HitCount.objects.get_for_object(self)
        return hit_count.hits
    
    def __str__(self):
        return self.user.username