from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator, print_json

from examples import custom_style_2

import mysql.connector

import time

import pyfiglet

import datetime

from prettytable import PrettyTable

import re

def checktime(input):
    try:
        time.strptime(input, '%H:%M:%S')
        return True
    except ValueError:
        return False

def isnumeric(x):
    if x.isdigit():
        return True
    else:
        return False
    
def isstr(x):
    return bool(re.search(r'\d', x))

def checkdate(input):
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.datetime.strptime(input, date_format)
        return True
    except ValueError:
        return False

welcome_screen = [
    {
        'type': 'list',
        'name': 'Logging in as',
        'message': 'Are you an admin or receptionist',
        'choices': [
            'Login as admin',
            'Login as receptionist'
        ]
    }
]

loginAdmin = [
    {
        'type': 'input',
        'name': 'admin username',
        'message': 'Enter your username : '
    }
]

loginRecep = [
    {
        'type': 'input',
        'name': 'receptionist username',
        'message': 'Enter your username : '
    }
]

adminPass = [
    {
        'type': 'password',
        'message': 'Enter your password : ',
        'name': 'Password'
    }
]

recepPass = [
    {
        'type': 'password',
        'message': 'Enter your password : ',
        'name': 'Password'
    }
]

receptionist_screen = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'Select from the following operations',
        'choices': [
            'Create a new passenger record',
            'Update details of an existing passenger record',
            'View all available flights in a particular time period',
            'Generate ticket record for a particular passenger for a particular flight',
            'View the cheapest flight',
            'View flight history of a particular passenger',
            'Cancel a particular ticket record',
            'Logout'
        ]
    }
]

admin_screen = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'Select from the following operations',
        'choices': [
            'Add a new flight record',
            'Update details of an existing flight record',
            'Cancel a particular flight record',
            'View all flights landing and taking off for a particular airport on that day',
            'View every table of the database in tabular form', 
            'Logout'
        ]
    }
]

update_flight = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to update?',
        'choices': [
            'Departure airport',
            'Arrival airport',
            'Departure time',
            'Arrival time',
            'Departure date',
            'Airplane',
            'Fare'
        ]
    }
]

update_passenger = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to update?',
        'choices': [
            'Passenger name',
            'Address',
            'Phone',
            'Nationality'
        ]
    }
]

granted = False
logout = False
correct_time = False

result = pyfiglet.figlet_format("Airline DB", font = "larry3d") 
print('''                 ____
                |        | ___\          /~~~|
                _:_______|/'(..)`\_______/  | |
                <_|``````  \__~~__/  PAK  ___|_|
                :\_____(=========,(*),--\__|_/
                |       \       /---'
                        | (*) /
                        |____/

''')
print('')
print(result) 

print('')

w_s = prompt(welcome_screen, style=custom_style_2)

if w_s['Logging in as'] == 'Login as admin':
    # pprint(w_s)
    print('')
    print ('Welcome admin please verify your credentials')
    print('')
    while granted != True:
        l_A = prompt(loginAdmin, style=custom_style_2)
        # pprint(l_A)
        a_P = prompt(adminPass, style=custom_style_2)
        adminuser = l_A['admin username']
        adminpassword = a_P['Password']
        print('')
        print('Please wait verifying your details')
        print('')
        
        mydb = mysql .connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
    )
        mycursor = mydb.cursor()
        mycursor.execute("USE airline")
        mycursor.execute("SELECT * FROM ADMIN")
        data = mycursor.fetchall()
        for d in data:
            if d[1] != adminuser or d[2] != adminpassword:
                print ('Access denied! Invalid username or password. Please try again')
                print('')
                break
            else:
                print('Access granted!')
                granted = True
                break
    print('')
    while logout != True:
        adminscreen = prompt(admin_screen, style=custom_style_2)
        
        if adminscreen['menu'] == 'Logout':
            logout = True
            print('')
            result = pyfiglet.figlet_format("Signed out...!", font = "larry3d") 
            print(result) 
            
        elif adminscreen['menu'] == 'Add a new flight record':
            fi = str(input ('Enter flight ID :  '))
            fi = fi.upper()
            sql1 = 'SELECT flight_id FROM flight WHERE flight_id = %s'
            value1 = (fi, )
            mycursor.execute(sql1, value1)
            data1 = mycursor.fetchall()
            if len(data1) != 0:
                print('Flight ID ', fi, ' already exists!')
                print('')
            else:
                is_str = True
                while is_str != False:
                    dep_air = input('Enter departure airport : ')
                    is_str = isstr(dep_air)
                    if is_str == True:
                        print('No numerics allowed!')
                    else:
                        is_str = False
                is_str = True
                while is_str != False:
                    arr_air = input('Enter arrival airport : ')
                    is_str = isstr(arr_air)
                    if is_str == True:
                        print('No numerics allowed!')
                    else:
                        is_str = False
                is_str = True
                
                dep_air = dep_air.upper()
                arr_air = arr_air.upper()
                
                while correct_time != True:
                    dep_t = input ('Enter departure time (hh:mm:ss) :  ')
                    flag = checktime(dep_t)
                    if flag == True:
                        correct_time = True
                    else:
                        print('Invalid time format! Enter again')
                        
                correct_time = False
                
                while correct_time != True:
                    arr_t = input ('Enter arrival time (hh:mm:ss) :  ')
                    flag = checktime(arr_t)
                    if flag == True:
                        correct_time = True
                    else:
                        print('Invalid time format! Enter again')
                
                correct_time = False
                
                plane = str(input ('Enter airplane name :  '))
                plane = plane.upper()
                farecheck = False
                while farecheck != True:
                        fare = input('Enter fare : ')
                        isnum = isnumeric(fare)
                        if isnum == False or int(fare) < 0:
                            print('Please enter positive numeric number!')
                        else:
                            farecheck = True
                    
                farecheck = False
                
                while correct_time != True:
                    dep_date = input ('Enter departure date (yyyy-mm-dd) :  ')
                    flag = checkdate(dep_date)
                    if flag == True:
                        correct_time = True
                    else:
                        print('Invalid date format! Enter again')
                
                correct_time = False
                
                sql = 'INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)' #%H:%M:%S
                val = (fi, dep_air, arr_air, dep_t, arr_t, dep_date, plane, fare)
                mycursor.execute(sql, val)
                mydb.commit()
                print('')
                print('New flight record added successfully!')
                print('')
            
        elif adminscreen['menu'] == 'Update details of an existing flight record':
            updateflight = prompt(update_flight, style=custom_style_2)
            print('')        
            if updateflight['menu'] == 'Departure airport':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    is_str = True
                    while is_str != False:
                        newdep = input('Enter new departure airport : ')
                        is_str = isstr(newdep)
                        if is_str == True:
                            print('No numerics allowed!')
                        else:
                            is_str = False
                    is_str = True
                    newdep = newdep.upper()
                    sql = 'UPDATE FLIGHT SET departure_airport = %s WHERE flight_id = %s'
                    val = (newdep, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Departure airport for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Arrival airport':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    is_str = True
                    while is_str != False:
                        newarr = input('Enter new arrival airport : ')
                        is_str = isstr(newarr)
                        if is_str == True:
                            print('No numerics allowed!')
                        else:
                            is_str = False
                    is_str = True
                    newarr = newarr.upper()
                    sql = 'UPDATE FLIGHT SET arrival_airport = %s WHERE flight_id = %s'
                    val = (newarr, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Arrival airport for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Departure time':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    while correct_time != True:
                        newdeptime = input('Enter new departure time (hh:mm:ss) :  ')
                        flag = checktime(newdeptime)
                        if flag == True:
                            correct_time = True
                        else:
                            print('Invalid time format! Enter again')
                    correct_time = False
                    sql = 'UPDATE FLIGHT SET departure_time = %s WHERE flight_id = %s'
                    val = (newdeptime, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Departure time for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Arrival time':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    while correct_time != True:
                        newarrtime = input('Enter new arrival time (hh:mm:ss) :  ')
                        flag = checktime(newarrtime)
                        if flag == True:
                            correct_time = True
                        else:
                            print('Invalid time format! Enter again')
                    correct_time = False
                    sql = 'UPDATE FLIGHT SET arrival_time = %s WHERE flight_id = %s'
                    val = (newarrtime, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Arrival time for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Airplane':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                mycursor.execute("SELECT * FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                        to_replace = x[6]
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    newplane = str(input('Enter new plane name : '))
                    newplane = newplane.upper()
                    sql = 'UPDATE FLIGHT SET airplane = %s WHERE flight_id = %s'
                    val = (newplane, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Airplane for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Fare':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                farecheck = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    while farecheck != True:
                        newfare = input('Enter new fare : ')
                        isnum = isnumeric(newfare)
                        if isnum == False or int(newfare) < 0:
                            print('Please enter positive numeric number!')
                        else:
                            farecheck = True
                    
                    farecheck = False
                    
                    sql = 'UPDATE FLIGHT SET fare = %s WHERE flight_id = %s'
                    val = (newfare, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Fare for flight id ', id, ' has been updated!')
                    print('')
            elif updateflight['menu'] == 'Departure date':
                id = str(input('Enter flight id :  '))
                id = id.upper()
                found = False
                farecheck = False
                mycursor.execute("SELECT flight_id FROM FLIGHT")
                for x in mycursor:
                    if x[0] == id:
                        found = True
                if found == False:
                    print('No such flight ID exists! Cannot perform update operation')
                    print('')
                else:
                    correct_time = False
                    while correct_time != True:
                        newdep_date = input ('Enter new departure date (yyyy-mm-dd) :  ')
                        flag = checkdate(newdep_date)
                        if flag == True:
                            correct_time = True
                        else:
                            print('Invalid date format! Enter again')
                
                    correct_time = False
                    
                    sql = 'UPDATE FLIGHT SET departure_date = %s WHERE flight_id = %s'
                    val = (newdep_date, id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Departure date for flight id ', id, ' has been updated!')
                    print('')
                    
        elif adminscreen['menu'] == 'Cancel a particular flight record':
            id = str(input('Enter flight id :  '))
            id = id.upper()
            found = False
            mycursor.execute("SELECT flight_id FROM FLIGHT")
            for x in mycursor:
                if x[0] == id:
                    found = True
            if found == False:
                print('No such flight ID exists! Cannot perform removal operation')
                print('')
            else: 
                sql = 'DELETE FROM FLIGHT WHERE flight_id = %s'
                val = (id, )
                mycursor.execute(sql, val)
                mydb.commit()
                
                sql2 = 'DELETE FROM TICKET_HISTORY WHERE flight_id = %s'  # to maintain referential integrity
                val2 = (id, )
                mycursor.execute(sql2, val2)
                mydb.commit()
                print('')
                print('Flight record with flight id ', id, ' has been cancelled!')
                print('')
        elif adminscreen['menu'] == 'View every table of the database in tabular form':
            mycursor.execute('SELECT * FROM PASSENGER')
            data = mycursor.fetchall()
            x = PrettyTable(["passenger_id", "passenger_name", "address", "phone", "nationality"])
            for d in data:
                x.add_row([d[0], d[1], d[2], d[3], d[4]])
            print('')
            print(x)
            print('')
            mycursor.execute('SELECT * FROM FLIGHT')
            data = mycursor.fetchall()
            x2 = PrettyTable(["Flight ID", "Departure IATA code", "Arrival IATA code", "Dep_time", "Arr_time", "Dep_date", "Airplane", "Fare"])
            for d in data:
                x2.add_row([d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
            print('')
            print(x2)
            print('')
            mycursor.execute('SELECT * FROM TICKET_HISTORY')
            data = mycursor.fetchall()
            x3 = PrettyTable(["ticket_id", "flight_id", "passenger_id", "seat_number", "booking_date"])
            for d in data:
                x3.add_row([d[0], d[1], d[2], d[3], d[4]])
            print('')
            print(x3)
            print('')
            mycursor.execute('SELECT * FROM ADMIN')
            data = mycursor.fetchall()
            x4 = PrettyTable(["admin_id", "admin_name", "password"])
            for d in data:
                x4.add_row([d[0], d[1], d[2]])
            print('')
            print(x4)
            print('')
            mycursor.execute('SELECT * FROM RECEPTIONIST')
            data = mycursor.fetchall()
            x5 = PrettyTable(["receptionist_id", "receptionist_name", "password"])
            for d in data:
                x5.add_row([d[0], d[1], d[2]])
            print('')
            print(x5)
            print('')
        elif adminscreen['menu'] == 'View all flights landing and taking off for a particular airport on that day':
            is_str = True
            while is_str != False:
                airport = input('Enter airport name : ')
                is_str = isstr(airport)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            airport = airport.upper()
            correct_date = False
            while correct_date != True:
                day = input ('Enter date (yyyy-mm-dd) :  ')
                flag = checkdate(day)
                if flag == True:
                    correct_date = True
                else:
                    print('Invalid date format! Enter again')
        
            correct_date = False
            is_str = True
            sql = 'SELECT * FROM FLIGHT WHERE (departure_airport = %s OR arrival_airport = %s) AND (departure_date = %s)'
            value = (airport, airport, day)
            mycursor.execute(sql, value)
            data = mycursor.fetchall()
            if len(data) == 0:
                print('No flights available')
                print('')
            else:
                x = PrettyTable(["Flight ID", "Departure IATA code", "Arrival IATA code", "Dep_time", "Arr_time", "Dep_date", "Airplane", "Fare"])
                for d in data:
                    x.add_row([d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
                print('')
                print('These are the available flights')
                print('')
                print(x)
                print('')
            
else: # Login as receptionist
    #pprint(w_s)
    print('')
    print ('Welcome receptionist please verify your credentials')
    print('')
    while granted != True:
        l_R = prompt(loginRecep, style=custom_style_2)
        #pprint(l_A)
        r_P = prompt(recepPass, style=custom_style_2)
        receptionistuser = l_R['receptionist username']
        receptionistpassword = r_P['Password']
        print('')
        print('Please wait verifying your details')
        print('')
        
        mydb = mysql .connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
    )
        mycursor = mydb.cursor()
        mycursor.execute("USE airline")
        mycursor.execute("SELECT * FROM RECEPTIONIST")
        data = mycursor.fetchall()
        for d in data:
            if d[1] != receptionistuser or d[2] != receptionistpassword:
                print ('Access denied! Invalid username or password. Please try again')
                print('')
                break
            else:
                print('Access granted!')
                granted = True
                break
    print('')
    while logout != True:
        receptionistscreen = prompt(receptionist_screen, style=custom_style_2)
        if receptionistscreen['menu'] == 'Logout':
            logout = True
            print('')
            result = pyfiglet.figlet_format("Signed out...!", font = "larry3d") 
            print(result)
        
        elif receptionistscreen['menu'] == 'Create a new passenger record':
            cnicheck = False
            phonecheck = False
            is_str = True
            while is_str != False:
                name = input('Please enter full name : ')
                is_str = isstr(name)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            is_str = True
         
            mycursor.execute("SELECT passenger_id FROM PASSENGER") 
            listcnic = []
            for data in mycursor:
                listcnic.append(data[0])
                
            while cnicheck != True:
                cnic = input('Please enter CNIC : ')
                isnum = isnumeric(cnic)
                if len(cnic) != 13 or isnum == False or int(cnic) < 0:
                    print('Please enter CNIC in valid format (13 digit number)')
                elif int(cnic) in listcnic:
                    print('CNIC numbers cannot be same! Please enter a unique one')
                else:
                    cnicheck = True
                    
            cnicheck = False
            
            addr = input('Please enter address : ')
            addr = addr.upper()
            
            while phonecheck != True:
                phone = input('Please enter phone : ')
                isnum = isnumeric(phone)
                if len(phone) != 11 or isnum == False or int(phone) < 0:
                    print('Please enter phone in valid format (11 digit number)')
                else:
                    phonecheck = True
            phonecheck = False
        
            while is_str != False:
                nationality = input('Please enter nationality : ')
                is_str = isstr(nationality)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            is_str = True
            
            nationality = nationality.lower()
            
            listcnic.clear()
            
            sql = 'INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES (%s, %s, %s, %s, %s)' 
            val = (cnic, name, addr, phone, nationality)
            mycursor.execute(sql, val)
            mydb.commit()
            print('')
            print('Passenger created successfully!')
            print('')
            
        elif receptionistscreen['menu'] == 'Update details of an existing passenger record':
            print('')
            updatepassenger = prompt(update_passenger, style=custom_style_2)
            if updatepassenger['menu'] == 'Passenger name':
                cnicheck = False
                while cnicheck != True:
                    Cnic = input('Enter your cnic :  ')
                    isnum = isnumeric(Cnic)
                    if len(Cnic) != 13 or isnum == False or int(Cnic) < 0:
                        print('Please enter CNIC in valid format (13 digit number)')
                    else:
                        cnicheck = True
                cnicheck = False
                found = False
                mycursor.execute("SELECT passenger_id FROM PASSENGER")
                for x in mycursor:
                    if x[0] == int(Cnic):
                        found = True
                    
                if found == False:
                    print('No such CNIC exists! Cannot perform update operation')
                    print('')
                else:
                    is_str = True
                    while is_str != False:
                        newname = input('Enter new passenger name : ')
                        is_str = isstr(newname)
                        if is_str == True:
                            print('No numerics allowed!')
                        else:
                            is_str = False
                    is_str = True
                    sql = 'UPDATE PASSENGER SET passenger_name = %s WHERE passenger_id = %s'
                    val = (newname, Cnic)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Passenger name for passenger having CNIC ', Cnic, ' has been updated!')
                    print('')
            elif updatepassenger['menu'] == 'Address':
                cnicheck = False
                while cnicheck != True:
                    Cnic = input('Enter your cnic :  ')
                    isnum = isnumeric(Cnic)
                    if len(Cnic) != 13 or isnum == False or int(Cnic) < 0:
                        print('Please enter CNIC in valid format (13 digit number)')
                    else:
                        cnicheck = True
                cnicheck = False
                found = False
                mycursor.execute("SELECT passenger_id FROM PASSENGER")
                for x in mycursor:
                    if x[0] == int(Cnic):
                        found = True

                if found == False:
                    print('No such CNIC exists! Cannot perform update operation')
                    print('')
                else:
                    newaddr = input('Enter new address : ')
                    newaddr = newaddr.upper()
                    sql = 'UPDATE PASSENGER SET address = %s WHERE passenger_id = %s'
                    val = (newaddr, Cnic)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Address for passenger having CNIC ', Cnic, ' has been updated!')
                    print('')
            elif updatepassenger['menu'] == 'Phone':
                cnicheck = False
                while cnicheck != True:
                    Cnic = input('Enter your cnic :  ')
                    isnum = isnumeric(Cnic)
                    if len(Cnic) != 13 or isnum == False or int(Cnic) < 0:
                        print('Please enter CNIC in valid format (13 digit number)')
                    else:
                        cnicheck = True
                cnicheck = False
                found = False
                mycursor.execute("SELECT passenger_id FROM PASSENGER")
                for x in mycursor:
                    if x[0] == int(Cnic):
                        found = True
                if found == False:
                    print('No such CNIC exists! Cannot perform update operation')
                    print('')
                else:
                    flag = False
                    while flag != True:
                        newphone = input('Please enter new phone : ')
                        isnum = isnumeric(newphone)
                        if len(newphone) != 11 or isnum == False or int(newphone) < 0:
                            print('Please enter phone in valid format (11 digit number)')
                        else:
                            flag = True
                    flag = False
                    sql = 'UPDATE PASSENGER SET phone = %s WHERE passenger_id = %s'
                    val = (newphone, Cnic)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Phone for passenger having CNIC ', Cnic, ' has been updated!')
                    print('')
            elif updatepassenger['menu'] == 'Nationality':
                cnicheck = False
                while cnicheck != True:
                    Cnic = input('Enter your cnic :  ')
                    isnum = isnumeric(Cnic)
                    if len(Cnic) != 13 or isnum == False or int(Cnic) < 0:
                        print('Please enter CNIC in valid format (13 digit number)')
                    else:
                        cnicheck = True
                cnicheck = False
                found = False
                mycursor.execute("SELECT passenger_id FROM PASSENGER")
                for x in mycursor:
                    if x[0] == int(Cnic):
                        found = True
    
                if found == False:
                    print('No such CNIC exists! Cannot perform update operation')
                    print('')
                else:
                    is_str = True
                    while is_str != False:
                        newnationality = input('Enter new nationality : ')
                        is_str = isstr(newnationality)
                        if is_str == True:
                            print('No numerics allowed!')
                        else:
                            is_str = False
                    is_str = True
                    newnationality = newnationality.lower()
                    sql = 'UPDATE PASSENGER SET nationality = %s WHERE passenger_id = %s'
                    val = (newnationality, Cnic)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print('')
                    print('Nationality for passenger having CNIC ', Cnic, ' has been updated!')
                    print('')
   
        elif receptionistscreen['menu'] == 'View all available flights in a particular time period':
            is_str = True
            while is_str != False:
                dep = input('Enter departure airport :  ')
                is_str = isstr(dep)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            is_str = True
            while is_str != False:
                arr = input('Enter arrival airport :  ')
                is_str = isstr(arr)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            is_str = True
            dep = dep.upper()
            arr = arr.upper()
            correct_time = False
            while correct_time != True:
                dep_date = input ('Enter departure date (yyyy-mm-dd) :  ')
                flag = checkdate(dep_date)
                if flag == True:
                    correct_time = True
                else:
                    print('Invalid date format! Enter again')
            correct_time = False
            sql = 'SELECT * FROM FLIGHT WHERE departure_airport = %s AND arrival_airport = %s AND departure_date = %s'
            val = (dep, arr, dep_date,)
            mycursor.execute(sql, val)
            data = mycursor.fetchall()
            # print(data)
            if len(data) == 0:
                print('No flights available')
                print('')
            else:
                x = PrettyTable(["Flight ID", "Departure IATA code", "Arrival IATA code", "Dep_time", "Arr_time", "Dep_date", "Airplane", "Fare"])
                for d in data:
                    x.add_row([d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
                print('These are the available flights')
                print('')
                print(x)
                print('')
                
        elif receptionistscreen['menu'] == 'Generate ticket record for a particular passenger for a particular flight':
            cnicheck = False
            while cnicheck != True:
                id = input('Enter your cnic :  ')
                isnum = isnumeric(id)
                if len(id) != 13 or isnum == False or int(id) < 0:
                    print('Please enter CNIC in valid format (13 digit number)')
                else:
                    cnicheck = True
            cnicheck = False
            id2 = str(input('Enter flight id :  ')) # flight id
            id2 = id2.upper()
            found = False
            found2 = False
            mycursor.execute("SELECT passenger_id FROM PASSENGER")
            for x in mycursor:
                if x[0] == int(id):
                    found = True
                    
            mycursor.execute("SELECT flight_id FROM FLIGHT")
            for x2 in mycursor:
                if x2[0] == id2:
                    found2 = True

            if found == False:
                print('CNIC', ' ', id, ' does not exist! Cannot generate ticket.')
                print('')
            elif found2 == False:
                print('Flight ID', ' ', id2, ' does not exist! Cannot generate ticket.')
                print('')
            else:
                s = False
                d = False
                flag = False
                while s != True:
                    seat = input('Enter seat number : ')
                    s = isnumeric(seat)
                    if s == False:
                        print('Please use numerics for seat number!')
                    else:
                        s = True
                while d != True:
                    book_date = input ('Enter booking date (yyyy-mm-dd) :  ')
                    flag = checkdate(book_date)
                    if flag == True:
                        sql = 'SELECT departure_date FROM FLIGHT WHERE flight_id = %s'
                        val = (id2, )
                        mycursor.execute(sql, val)
                        data = mycursor.fetchall()
                        for da in data:
                            original = da[0]
                        comp = book_date.split('-')
                        x = datetime.date(int(comp[0]), int(comp[1]), int(comp[2]))
                        if x > original:
                            print('Booking date cannot be greater than departure date which is : ', original)
                        else:
                            d = True
                    else:
                        print('Invalid date format! Enter again')
                d = False
                s = False
                sql = 'INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES (%s, %s, %s, %s)' 
                val = (id2, id, seat, book_date)
                mycursor.execute(sql, val)
                mydb.commit()
                print('')
                print('Ticket record generated successfully!')
                print('')
                
        elif receptionistscreen['menu'] == 'View flight history of a particular passenger':
            cnicheck = False
            while cnicheck != True:
                cnic = input('Please enter CNIC : ')
                isnum = isnumeric(cnic)
                if len(cnic) != 13 or isnum == False or int(cnic) < 0:
                    print('Please enter CNIC in valid format (13 digit number)')
                else:
                    cnicheck = True
            cnicheck = False
            sql = 'SELECT * FROM TICKET_HISTORY WHERE passenger_id = %s'
            value = (cnic, )
            mycursor.execute(sql, value)
            data = mycursor.fetchall()
            if len(data) == 0:
                print('No history available!')
                print('')
            else:
                x = PrettyTable(["Ticket ID", "Flight ID", "CNIC", "Seat Number", "Booking Date"])
                for d in data:
                    x.add_row([d[0], d[1], d[2], d[3], d[4]])
                print('Flight history for passenger ', cnic, ' is this')
                print('')
                print(x)
                print('')
        elif receptionistscreen['menu'] == 'Cancel a particular ticket record':
            cnicheck = False
            while cnicheck != True:
                cnic = input('Please enter CNIC : ')
                isnum = isnumeric(cnic)
                if len(cnic) != 13 or isnum == False or int(cnic) < 0:
                    print('Please enter CNIC in valid format (13 digit number)')
                else:
                    cnicheck = True
            cnicheck = False
            id = str(input('Enter flight id :  '))
            id = id.upper()
            sql = 'SELECT * FROM TICKET_HISTORY WHERE (flight_id = %s AND passenger_id = %s)'
            val = (id, cnic)
            mycursor.execute(sql, val)
            data = mycursor.fetchall()
            if len(data) == 0:
                print ('No such ticket record exists!')
                print('')
            else:
                sql2 = 'DELETE FROM TICKET_HISTORY WHERE (flight_id = %s AND passenger_id = %s)'
                val2 = (id, cnic)
                mycursor.execute(sql2, val2)
                mydb.commit()
                print('')
                print('Ticket record(s) cancelled successfully')
                print('')
                
        elif receptionistscreen['menu'] == 'View the cheapest flight':
            is_str = True
            while is_str != False:
                dep = input('Enter departure airport IATA code : ')
                is_str = isstr(dep)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            is_str = True
            while is_str != False:
                arr = input('Enter arrival airport IATA code : ')
                is_str = isstr(arr)
                if is_str == True:
                    print('No numerics allowed!')
                else:
                    is_str = False
            dep = dep.upper()
            arr = arr.upper()
            sql = 'SELECT * FROM FLIGHT WHERE (departure_airport = %s AND arrival_airport = %s) ORDER BY fare ASC'
            value = (dep, arr)
            mycursor.execute(sql, value)
            data = mycursor.fetchall()
            if len(data) == 0:
                print('No flights available for provided IATA codes!')
                print('')
            else:
                print('')
                print('The following flight is cheapest')
                print('')
                x = PrettyTable(["Flight ID", "Departure IATA code", "Arrival IATA code", "Dep_time", "Arr_time", "Dep_date", "Airplane", "Fare"])
                for d in data:
                    x.add_row([d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
                    break
                print(x)
                print('')
                