# SET travel_agent TO EMPTY ARRAY
travel_agent = []
# SET booking number TO EMPTY ARRAY
booking_number = []
# SET dates TO EMPTY ARRAY
dates = []
# LOOP 3 TIMES
for index in range(3):
#      RECEIVE travel agent FROM (STRING) KEYBOARD
    travelagent = input("Enter travel agent")
#      RECEIVE booking number FROM (INTEGER) KEYBOARD
    bookingnumber = input("Enter booking number")
#      RECEIVE date FROM (STRING) KEYBOARD
    date = input("Enter date")
#      ADD booking number TO booking number ARRAY
    booking_number.append(bookingnumber)
#      ADD date no TO dates ARRAY
    dates.append(date)
#      ADD travel agent TO travel_agent ARRAY
    travel_agent.append(travelagent)
# NEXT

# DISPLAY travel_agent, booking number AND dates ARRAYS
print(travel_agent, booking_number, dates)
