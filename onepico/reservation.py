from datetime import timedelta, datetime
import time
from .models import Restaurant, Booking, TableLunch, TableDinner
import random


def check_double_booking_date(people, requested_date, requested_time, phone):

    customer_records = Booking.objects.filter(phone=phone).all()
    if len(customer_records) >= 1:
        customer_records_requested_date = Booking.objects. \
            filter(phone=phone, date=requested_date)
        for value in customer_records_requested_date.values():
            name = value['name']
            last_name = value['last_name']
            phone = value['phone']
            customer_record_date_str = value['date'].strftime('%Y-%m-%d')
            customer_record_start_time_str = value['start_time']. \
                strftime('%H:%M')
            requested_date_str = requested_date.strftime('%Y-%m-%d')
            week_number_customer_record_str = value['date'].strftime('%U')
            week_number_requested_date_str = requested_date.strftime('%U')
            if customer_record_date_str == requested_date_str:
                print("**** There seems to be another booking")
                print("with same details for the same date ****")
                print("**** Booking details:")
                print("****" + " " + name + " " + last_name + ", date" +
                      " " + customer_record_date_str + " " + "at" +
                      " " + customer_record_start_time_str +
                      ", contact number" + " " + str(phone) + " " + "****")
                return False
            else:
                return True


def get_table_available(people, requested_date, requested_time, booking_id):
    """
    Function to check restaurant availability
    to make sure requested date matches opening days
    and check requested booking time
    """
    # minutes_slot = 120
    # delta = timedelta(seconds=60*minutes_slot)
    # slotime = requested_time + delta
    # print(requested_time)
    # print(slotime)

    # converts date into a string and gets weekday name
    requested_date_str = datetime.strftime(requested_date,
                                           "%Y-%m-%d")
    date_name_day = time.strftime('%A', time.strptime(requested_date_str,
                                                      "%Y-%m-%d"))
    requested_time_str = datetime.strftime(requested_time, "%H:%M")
    people = people
    requested_date_str = requested_date_str
    requested_time_str = requested_time_str

    if date_name_day in Restaurant.opening_days:
        request = Booking.objects.filter(id=booking_id)
        # loop through the requested booking object and get values
        for value in request.values():
            people_requested = value['party_size']
            booking_id = value['id']
            customer_name = value['name']
            date = value['date']
            start_time = value['start_time']

        if requested_time_str >= "12:00" and requested_time_str <= "14:30":
            if check_lunch_time(people_requested, booking_id,
                                customer_name,
                                date, people, start_time):
                print("Room fully booked at lunch time for the date requested")
                print(", try at another date.")
                return False
            else:
                return True
        elif requested_time_str >= "18:00" and requested_time_str <= "21:30":
            if check_dinner_time(people_requested, booking_id,
                                 customer_name,
                                 date, people, start_time):
                print("Room fully booked at dinner time for")
                print("the date requested try at another date")
                return True
            else:
                print("BOOKED")
                return False
        else:
            raise Exception("""Service hours, Lunch from 12:00pm to 14:30
                            Dinner, from 18:00pm to 21:30pm""")
    else:
        raise Exception("Day of the week do not coincidence with opening days")


def check_lunch_time(people_requested, booking_id,
                     customer_name, date, people,
                     start_time):
    """
    Function to check party size and call
    functions  according to it, to look for
    best suitable tables at lunch time
    """
# get Booking instance to pass it into the new_table object as table_id value
    booking_id = Booking.objects.get(id=booking_id)

    if people_requested == 1 or people_requested == 2:
        check_small_tables_available_lunch(people_requested,
                                           booking_id,
                                           customer_name,
                                           date, people,
                                           start_time)
    elif people_requested == 3 or people_requested == 4:
        check_medium_tables_available_lunch(people_requested,
                                            booking_id,
                                            customer_name,
                                            date, people,
                                            start_time)
    elif people_requested >= 5 or people_requested <= 7:
        check_large_tables_available_lunch(people_requested,
                                           booking_id,
                                           customer_name,
                                           date,
                                           people,
                                           start_time)


def check_dinner_time(people_requested,
                      booking_id,
                      customer_name,
                      date,
                      people,
                      start_time):
    """
    Function to check party size and call
    functions according to it, to look for
    best suitable tables at dinner time
    """
# get Booking instance to pass it into the new_table object as table_id value
    booking_id = Booking.objects.get(id=booking_id)

    if people_requested == 1 or people_requested == 2:
        check_small_tables_available_dinner(people_requested,
                                            booking_id,
                                            customer_name,
                                            date, people,
                                            start_time)
    elif people_requested == 3 or people_requested == 4:
        check_medium_tables_available_dinner(people_requested,
                                             booking_id,
                                             customer_name,
                                             date,
                                             people,
                                             start_time)
    elif people_requested >= 5 or people_requested <= 7:
        check_large_tables_available_dinner(people_requested,
                                            booking_id,
                                            customer_name,
                                            date, people,
                                            start_time)


def check_small_tables_available_lunch(people_requested, booking_id,
                                       customer_name,
                                       date,
                                       people,
                                       start_time):
    """
    Function to check small tables
    available at lunch time.
    If no small tables, will look for medium tables available
    """
    active = True
    small_tables_booked_list = []
    print(small_tables_booked_list)
    while active:
        random_table_object = random.choice(Restaurant.small_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')
        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()

        # loop through tables booked for requested day...
        # ...and get table number and start time
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_finishing_time = "14:30"
            print("""Print one table number(lunch time)
                  for every loop and push it into small tables booked list""",
                  table_number_booked, "table start time",
                  table.get('start_time'))
            if booked_tables_start_time_str <= service_finishing_time:
                if table_number_booked <= 4 and table_number_booked \
                                            not in small_tables_booked_list:
                        small_tables_booked_list.append(table_number_booked)
                        print("List small tables booked at lunch time",
                              small_tables_booked_list)

        if table_number in small_tables_booked_list \
                and len(small_tables_booked_list) == 4:
            print("Table number at lunch time", table_number,
                  "already booked")

        if table_number in \
                small_tables_booked_list \
                and len(small_tables_booked_list) >= 4:
            print("tables length", len(small_tables_booked_list))
            print("tables booked", small_tables_booked_list)
            print("SMALL TABLES AT LUNCH TIME FULLY BOOKED")
            check_medium_tables_available_lunch(people_requested,
                                                booking_id,
                                                customer_name,
                                                date, people,
                                                start_time)
            active = False

        if table_number not in small_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            small_tables_booked_list.append(table_number)
            print("Table number", table_number, "now booked")
            print("Small tables list length", len(small_tables_booked_list))
            print("""Tables number booked(lunch time)
                  in small tables list(lunch time)""",
                  small_tables_booked_list)
            active = False


def check_medium_tables_available_lunch(people_requested,
                                        booking_id,
                                        customer_name,
                                        date,
                                        people,
                                        start_time):
    """
    Function to check medium tables
    available at lunch time.
    If no medium tables, will look for large tables available
    """
    medium_tables_booked_list = []
    active = True
    while active:
        random_table_object = random.choice(Restaurant.medium_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')

        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()
        # loop through tables booked for the requested...
        # day and get table number and start time
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            print("""Print one table number for every search and push it
                  into tables booked""", table['table_number'])
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_finishing_time = "14:30"
            if booked_tables_start_time_str <= service_finishing_time:
                if table_number_booked == 5 or \
                            table_number_booked == 6 and \
                            table_number_booked not in \
                            medium_tables_booked_list:
                        print(table_number_booked, 'uuuuuuuuu')
                        medium_tables_booked_list.append(table_number_booked)
                        print("List medium tables booked(lunch time)",
                              medium_tables_booked_list)

        if table_number in medium_tables_booked_list and \
                len(medium_tables_booked_list) < 2:
            print("Table number", table_number, "already booked")
            continue

        if table_number in medium_tables_booked_list and \
                len(medium_tables_booked_list) >= 2:
            print("medium tables list length", len(medium_tables_booked_list))
            print("Medium tables booked", medium_tables_booked_list)
            print("MEDIUM TABLES FULLY BOOKED AT LUNCH TIME")
            check_large_tables_available_lunch(people_requested, booking_id,
                                               customer_name, date,
                                               people, start_time)
            active = False

        if table_number not in medium_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            medium_tables_booked_list.append(table_number)
            print("Table number", table_number, "now booked")
            print("Medium tables list length", len(medium_tables_booked_list))
            print("Medium tables number booked at lunch time",
                  medium_tables_booked_list)
            active = False


def check_large_tables_available_lunch(people_requested,
                                       booking_id,
                                       customer_name,
                                       date,
                                       people,
                                       start_time):
    """
    Function to check large tables
    available at lunch time.
    If no large tables, will show a message of no tables available
    """
    large_tables_booked_list = []
    active = True
    while active:
        random_table_object = random.choice(Restaurant.large_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')
        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_finishing_time = "14:30"
            print("""Print one table number(lunch time) for every loop
                  and push it into tables booked""", table_number_booked,
                  "table start time", table.get('start_time'))
            if table_number_booked >= 7 and table_number_booked <= 8:
                if booked_tables_start_time_str <= service_finishing_time and \
                        table_number_booked not in large_tables_booked_list:
                    large_tables_booked_list.append(table_number_booked)
                    print("Large tables booked list(lunch time)",
                          large_tables_booked_list)

        if table_number in large_tables_booked_list and \
                len(large_tables_booked_list) < 2:
            print("Table number", table_number,  "already booked")
            continue

        elif table_number in large_tables_booked_list and \
                len(large_tables_booked_list) >= 2:
            print("tables length", len(large_tables_booked_list))
            print("List large tables booked", large_tables_booked_list)
            print("LARGE TABLES FULLY BOOKED AT LUNCH TIME")
            active = False

        if table_number not in large_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            large_tables_booked_list.append(table_number)
            print("Table number", table_number, " now booked")
            print("large tables list length", len(large_tables_booked_list))
            print("List large tables booked(lunch time)",
                  large_tables_booked_list)
            active = False


def check_small_tables_available_dinner(people_requested,
                                        booking_id,
                                        customer_name,
                                        date,
                                        people,
                                        start_time):
    """
    Function to check small tables
    available at dinner time.
    If no small tables, will look for medium tables available
    """
    active = True
    small_tables_booked_list = []
    while active:
        random_table_object = random.choice(Restaurant.small_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')
        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()
        # loop through tables booked for requested day...
        # ...and get table number and start time
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_starting_time = "18:00"
            print("""Print one table number(dinner time) for every loop
                  and push it into tables booked""", table_number_booked,
                  "table start time", table.get('start_time'))
            if booked_tables_start_time_str >= service_starting_time:
                if table_number_booked <= 4 and table_number_booked not in \
                        small_tables_booked_list:
                    small_tables_booked_list.append(table_number_booked)
                    print("List small tables booked(dinner time)",
                          small_tables_booked_list)

        if table_number in small_tables_booked_list and \
                len(small_tables_booked_list) < 4:
            print("Table number", table_number, "already booked")
            continue
        elif table_number in small_tables_booked_list and \
                len(small_tables_booked_list) >= 4:
            print("tables length", len(small_tables_booked_list))
            print("tables booked", small_tables_booked_list)
            print("SMALL TABLES FULLY BOOKED AT DINNER TIME")
            check_medium_tables_available_lunch(people_requested,
                                                booking_id,
                                                customer_name,
                                                date,
                                                people,
                                                start_time)

        if table_number not in small_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            small_tables_booked_list.append(table_number)
            print("Table number", table_number, " now booked")
            print("Small tables list length", len(small_tables_booked_list))
            print("Tables in small tables list(dinner time)",
                  small_tables_booked_list)
            active = False


def check_medium_tables_available_dinner(people_requested,
                                         booking_id,
                                         customer_name,
                                         date, people,
                                         start_time):
    """
    Function to check medium tables
    available at lunch time.
    If no medium tables, will look for large tables available
    """
    medium_tables_booked_list = []
    active = True
    while active:
        random_table_object = random.choice(Restaurant.medium_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')
        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()
        # loop through tables booked for requested day...
        # ...and get table number and start time
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            print("""Print one table number for every search
                  and push it into tables booked""", table['table_number'])
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_starting_time = "18:00"
            print("""Print one table number for every loop
                  and push it into tables booked""", table_number_booked,
                  "table start time", table.get('start_time'))
            if table_number_booked >= 5 and table_number_booked <= 6:
                if booked_tables_start_time_str >= service_starting_time and\
                        table_number_booked not in\
                        medium_tables_booked_list:
                    medium_tables_booked_list.append(table_number_booked)
                    print("List medium tables booked(dinner time)",
                          medium_tables_booked_list)

        if table_number in medium_tables_booked_list and \
                len(medium_tables_booked_list) < 2:
            print("Table number", table_number, "already booked")
            continue

        elif table_number in medium_tables_booked_list and \
                len(medium_tables_booked_list) >= 2:
            print("medium tables list length", len(medium_tables_booked_list))
            print("Medium tables booked", medium_tables_booked_list)
            print("MEDIUM TABLES FULLY BOOKED AT DINNER TIME")
            check_large_tables_available_lunch(people_requested,
                                               booking_id,
                                               customer_name,
                                               date, people,
                                               start_time)

        if table_number not in medium_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            medium_tables_booked_list.append(table_number)
            print("Table number", table_number, " now booked")
            print("Medium tables list length", len(medium_tables_booked_list))
            print("Medium tables booked(dinner time)",
                  medium_tables_booked_list)
            active = False


def check_large_tables_available_dinner(people_requested,
                                        booking_id,
                                        customer_name,
                                        date,
                                        people,
                                        start_time):
    """
    Function to check large tables
    available at dinner time.
    If no large tables, will show a message of not table available
    """
    large_tables_booked_list = []
    active = True
    while active:
        random_table_object = random.choice(Restaurant.large_table)
        table_number = random_table_object.get('table')
        table_max_people = random_table_object.get('max_px')
        tables_booked_requested_date = TableLunch.objects. \
            filter(date=date).all()
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time'). \
                strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str
            service_starting_time = "18:00"
            print("""Print one table number(dinner time) for every loop
                  and push it into tables booked""",
                  table_number_booked, "table start time",
                  table.get('start_time'))
            if table_number_booked >= 7 and table_number_booked <= 8:
                if booked_tables_start_time_str >= service_starting_time and\
                        table_number_booked not in large_tables_booked_list:
                    large_tables_booked_list.append(table_number_booked)
                    print("Large tables booked list(dinner time)",
                          large_tables_booked_list)

        if table_number in large_tables_booked_list and \
                len(large_tables_booked_list) < 2:
            print("Table number", table_number,  "already booked")
            continue

        elif table_number in large_tables_booked_list and\
                len(large_tables_booked_list) >= 2:
            print("tables length", len(large_tables_booked_list))
            print("List large tables booked", large_tables_booked_list)
            print("LARGE TABLES FULLY BOOKED AT DINNER TIME")
            active = False

        if table_number not in large_tables_booked_list:
            new_table = TableLunch.objects.create(table_id=booking_id,
                                                  table_number=table_number,
                                                  booked_for=people,
                                                  table_max_people=table_max_people,
                                                  table_status='confirmed',
                                                  customer_name=customer_name,
                                                  date=date,
                                                  start_time=start_time)
            large_tables_booked_list.append(table_number)
            print("Table number", table_number, " now booked")
            print("large tables list length", len(large_tables_booked_list))
            print("Large tables booked(dinner time)", large_tables_booked_list)
            active = False
