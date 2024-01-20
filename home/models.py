from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('customer', 'Customer'),
        ('professional', 'Professional'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)

    def __str__(self):
        return self.user





class Service(models.Model):
    category_choices = [
        ('home_maintenance', 'Home Maintenance'),
        ('carpentry', 'Carpentry and Woodworking'),
        ('construction', 'Construction and Remodeling'),
        ('landscaping', 'Landscaping and Outdoor Services'),
        ('cleaning', 'Cleaning Services'),
        ('technology', 'Technology and Electronics'),
        ('automotive', 'Automotive Services'),
        ('event', 'Event Services'),
        ('health', 'Health and Fitness'),
        ('tutoring', 'Tutoring and Educational Services'),

    ]
    category = models.CharField(max_length=50, choices=category_choices)
    image=models.ImageField(upload_to="service_image")


    def __str__(self):
        return f"{self.category}"


class OurServices(models.Model):
    our_service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    name=models.CharField(max_length=255)
    service_charge=models.PositiveIntegerField()
    description =models.TextField()
    image =models.ImageField(upload_to="our_service_images", blank=True, null=True)
    def __str__(self):
        return self.name

    



class Booking(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    service =models.ForeignKey(Service, on_delete=models.CASCADE)
    professional =models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_professional')
    date =models.DateField(auto_now_add=True) 
    time =models.TimeField(auto_now_add=True) 
    # date=models.DateTimeField()

    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

class Review(models.Model):
    booking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    comment=models.TextField()


