from django.db import models

# Create your models here.
# model for station table with fields: name, location
class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name + self.location
    

# model for train table with fields: name, source, destination, no_of_seats
class Train(models.Model):
    name = models.CharField(max_length=100)
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_from')    
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_to')
    no_of_seats = models.IntegerField(default=500)

    def __str__(self):
        return self.name

# model for schedules of each train
class Schedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='schedules')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='schedules')
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    class Meta:
        unique_together = ('train', 'station', 'arrival_time', 'departure_time')
    def __str__(self):
        return f"{self.train.name} - {self.station.name} ({self.arrival_time} - {self.departure_time})"

# Train Stop
# class TrainStop(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='stops')
#     station = models.ForeignKey(Station, on_delete=models.CASCADE)
#     arrival_time = models.DateTimeField()
#     departure_time = models.DateTimeField()
#     stop_number = models.IntegerField()  # To maintain order of stops

#     def __str__(self):
#         return f"Stop {self.stop_number} - {self.station.name}"


# model for admin table with fields: admin username, email, password
class Admin(models.Model):
    admin_username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_username
    

# model for ticket table with fields: train, passenger_name, seat_number, booking_date
class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.passenger_name
    
