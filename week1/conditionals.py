age = 28

if age < 13:
    print('Child')
elif age < 18:
    print('Teen')
else:
    print('Adult')


revenue=5000
if revenue>4000: print('Good week')
food_cost=32
if food_cost>35: print('ALERT: too high!')

day = 'Monday'
if day == 'Sunday': 
    print('Roast Day')

if revenue>4000 and food_cost<35: 
    print('Profitable')

if day == 'Saturday' or day == 'Sunday':
    print('Weekend')

is_open = True
if not is_open:
    print('Pub is closed')

if day in ['Friday', 'Saturday', 'Sunday']:
    print('Busy Night')

if is_open:
    if revenue > 3000:
        print('Good day')

rooms = 3 
guests = 2
if guests <= rooms:
    print('Confirmed')

rooms -= guests 
print(f'{rooms} rooms left')

score = 7.2
if score >= 8:
    r = 'Excellent'
elif score >= 6:
    r = 'Good'
else:
    r = 'Needs work'
print(r)

status = 'Open' if is_open else 'Closed'
print(status)

email = 'a@b.com'
if '@' in email and '.' in email:
    print('Valid')

stock = 0
if stock == 0:
    print('OUT OF STOCK')

pub = {'name': 'Red Lion', 'rooms': 5}
if pub.get('rooms', 0) > 0:
    print('Rooms available')

staff = 2
if staff <3: 
    print('understaffed')

day = 'Monday'
if day == 'Monday' or day == 'Tuesday':
    print('slow days')

revenue=9000
if revenue>8000: print('Excellent week')