# this functions adds two number together
def add (a, b):
	c = a + b
	print c

number_1 = 20
number_2 = 35

add (5, 6)
add (number_1, number_2)

def car (want_a_car, color, doors, cost):
	if want_a_car.lower() == 'yes' and int(cost) > 5000:
		print 'Great!'
		print 'You want a %s car. we can do that' % color
		print 'you want %s doors. I guess we can do that' % doors
		print 'sold'

	else: 
		print 'okay fine'

	want_a_car = raw_input ('want a car?: ')
	colors = raw_input ('what a color?: ')
	doors = raw_input ('how many doors?: ')


