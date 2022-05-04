from django.db import models

# Create your models here.

STATUS = ((0, "draft"), (1, "booked"))
PREFIX = [
    ('+353'),
    ('+34'),
    ('+35'),
]

class Restaurant():

    # tables = [
    #     {'table number': 1, 'px': 2, 'table_id': None},
    #     {'table number': 2, 'px': 2, 'table_id': None},
    #     {'table number': 3, 'px': 4, 'table_id': None},
    #     ]
    # minutes_slot = 90
    # delta = timedelta(seconds=60*minutes_slot)
             
    table_for_2 = 4
    table_for_4 = 1
    table_for_6 = 4
    opening_days = ["Tuesday","Wednesday","Thursday","Friday","Saturday"]
    opening_time= '12:00'
    closing_time = '21:30'

    def __str__(self):
        return f"Table for 2, {self.tables[0]}, table for 4, {self.tables[1]}, table for 6, {self.tables[2]}"
    

class Booking(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time} {self.id}'


class Lunch(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    opening_time = models.TimeField('%H:%M')
    closing_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'

class Dinner(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    opening_time = models.TimeField('%H:%M')
    closing_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'


class Table(models.Model):
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    leave_time = models.TimeField('%H:%M')
    table_number = models.PositiveIntegerField()
    px = models.BigIntegerField()
    status = models.BigIntegerField(choices=STATUS, default=0) 
    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="book_table")
    # number_of_tables = models.PositiveIntegerField()

    def __str__(self):
        return f"Table_id {self.table_id}, table status, {self.status}, table number,{self.table_number}, px, {self.px}, start time, {self.start_time}, leave table, {self.leave_time}"

