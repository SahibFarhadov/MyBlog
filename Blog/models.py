from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(null=False, editable=False,unique=True,db_index=True)
    
    def __str__(self):
        return f"{self.name}"


    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    image = models.ImageField(upload_to="blogs/%Y/%m",verbose_name="Şəkil")
    description = RichTextUploadingField()
    is_active = models.BooleanField(verbose_name="Aktiv status")
    is_home = models.BooleanField(verbose_name="Ana səhifə aktiv")
    slug=models.SlugField(editable=False,unique=True,db_index=True,null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    lastmodified=models.DateField("Sonuncu deyişiklik tarixi",auto_now=True)
    borndate=models.DateField("Yaranma tarixi",auto_now_add=True,null=True)
    snippet=models.CharField(max_length=50,default="Oxumaq üçün klikləyin...")

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

