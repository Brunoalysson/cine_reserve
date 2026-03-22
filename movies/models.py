from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField(null=True, blank=True)
    room = models.CharField(max_length=50) 
    
    def __str__(self):
        return f"{self.movie.title} - {self.start_time.strftime('%d/%m %H:%M')} - {self.room}"


class Seat(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('RESERVED', 'Reserved'),
        ('PURCHASED', 'Purchased'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=10)  
    number = models.IntegerField()         
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AVAILABLE')

    def __str__(self):
        return f"{self.session} - {self.row}{self.number} ({self.status})"