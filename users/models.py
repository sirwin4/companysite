from django.db import models
from django.contrib.auth.models import User
from PIL import	Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	
	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name} Profile' 
	
	def save(self, force_insert=False, force_update=False, using=None):
		super().save()
		
		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
			
class Address(models.Model):
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=25, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    street = models.CharField(max_length=250, blank=True)
    apartment = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = 'address'
        verbose_name_plural = 'addresses'

    def __unicode__(self):
        return ','.join([self.city, self.state, self.zipcode,self.street,self.apartment])
        
    def save(self, force_insert=False, force_update=False, using=None):
        super().save()