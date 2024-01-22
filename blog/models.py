from djongo import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

# Create your models here.

STATUS = ((0,"Draft"),(1,"Publish"))
CATEGORY = ((0,""),(1,"Itinerary"))


class Category(models.Model):
	_id = models.ObjectIdField()
	category_name = models.CharField(max_length=30,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	description = models.CharField(max_length=30)

	def __str__(self):
		return self.category_name


class Post(models.Model):
	_id = models.ObjectIdField()
	title=models.CharField(max_length=200, unique=True)
	sub_heading=models.CharField(max_length=200,default="")
	slug = models.SlugField(max_length=200, unique=True)
	# category = models.ForeignKey(Category, on_delete=models.CASCADE)
	category = models.IntegerField(choices=CATEGORY, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	content = RichTextField(blank=True, null=True)
	# author = models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.get(id=1).id)
	status = models.IntegerField(choices=STATUS, default=0)
	cover_img = models.CharField(max_length=200,null=True)
	

	def __str__(self):
		return self.title