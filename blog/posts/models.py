from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from PIL import Image
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinLengthValidator
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=35,validators=[MinLengthValidator(2,)])
    slug = models.SlugField(default="slug", editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def post_count(self):
        return self.posts.all().count()
    

class Tag(models.Model):
    name = models.CharField(max_length=35,validators=[MinLengthValidator(2,)])
    slug = models.SlugField(default="slug", editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def post_count(self):
        return self.posts.all().count()


class Post(models.Model):
    title = models.CharField(max_length=150,unique=True,validators=[MinLengthValidator(10,)])
    content = models.TextField(validators=[MinLengthValidator(20,)])
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=False,null=False)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=False)
    slug = models.SlugField(default="slug", editable=False,unique=True)
    hits = GenericRelation(HitCount, object_id_field='object_pk')
    isboost = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            img.thumbnail((500, 500))
            img.save(self.image.path)

    def set_tags(self,tags):
        tags_name_list = list()
        tags_list = tags.split(",")
        for tag_name in tags_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags_name_list.append(tag.name)
        tags = Tag.objects.filter(name__in = tags_name_list)
        self.tags.set(tags)
    
    def hits_count(self):
        hit_count = HitCount.objects.get_for_object(self)
        return hit_count.hits

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    name = models.CharField(max_length=150,validators=[MinLengthValidator(2,)])
    content = models.TextField(max_length=250,null=False,blank=False,validators=[MinLengthValidator(2,)])
    publish_date = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies',default=0, limit_choices_to={'level__lte': 0})
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=None, blank=None)

    def __str__(self) -> str:
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['publish_date']
