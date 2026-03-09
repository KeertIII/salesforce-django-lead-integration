from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    salesforce_id = models.CharField(max_length=50, blank=True, null=True)
    lead_score = models.IntegerField(default=0)
    lead_status = models.CharField(max_length=20, default='Cold')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"