from django.db import models

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20, unique=True)
    PasswordHash = models.CharField(max_length=255)
    Role = models.CharField(max_length=50, choices=[('Customer', 'Customer'), ('Provider', 'Provider'), ('Admin', 'Admin')])
    Address = models.CharField(max_length=255, blank=True, null=True)
    Verified = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class Providers(models.Model):
    ProviderID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    SkillDescription = models.TextField(blank=True, null=True)
    Certifications = models.CharField(max_length=255, blank=True, null=True)
    AvailableFrom = models.TimeField(blank=True, null=True)
    AvailableTo = models.TimeField(blank=True, null=True)
    Status = models.CharField(max_length=50, default='Available', choices=[('Available', 'Available'), ('Busy', 'Busy'), ('Inactive', 'Inactive')])
    Rating = models.FloatField(default=0)
    NumberOfRatings = models.IntegerField(default=0)

class Services(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=0)
    Duration = models.IntegerField()  

class ProviderServices(models.Model):
    ProviderServiceID = models.AutoField(primary_key=True)
    ProviderID = models.ForeignKey(Providers, on_delete=models.CASCADE)
    ServiceID = models.ForeignKey(Services, on_delete=models.CASCADE)

class Appointments(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Users, on_delete=models.CASCADE)
    ProviderID = models.ForeignKey(Providers, on_delete=models.CASCADE)
    ServiceID = models.ForeignKey(Services, on_delete=models.CASCADE)
    AppointmentDate = models.DateTimeField()
    Status = models.CharField(max_length=50, default='Pending', choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')])
    CreatedAt = models.DateTimeField(auto_now_add=True)

class Payments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    AppointmentID = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentMethod = models.CharField(max_length=50, choices=[('Bank Transfer', 'Bank Transfer'), ('Cash', 'Cash')])
    PaymentDate = models.DateTimeField(auto_now_add=True)
    PaymentStatus = models.CharField(max_length=50, default='Pending', choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

class Reviews(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Users, on_delete=models.CASCADE)
    ProviderID = models.ForeignKey(Providers, on_delete=models.CASCADE)
    Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
    Comment = models.TextField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class Blogs(models.Model):
    BlogID = models.AutoField(primary_key=True)
    AuthorID = models.ForeignKey(Users, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Content = models.TextField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

