from django.db import models 

class Disease(models.Model):
    name = models.CharField(max_length=30)
    symptoms = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Patient(models.Model): 
    name = models.CharField(max_length=100) 
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='patient') 
    doctor_assigned = models.CharField(max_length=100) 
    age = models.IntegerField() 
    room_number = models.IntegerField()
    patient_image = models.ImageField(upload_to='doc_img/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self): 
        return f"{self.name} --> Room: {self.room_number}"