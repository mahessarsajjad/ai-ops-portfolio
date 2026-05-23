name = 'Sajjad'
print(name)
age = 28
print(age)
print(type(age))
price = 12.50
print(price)
print(type(price))
is_open = True 
print(is_open)
print(type(is_open))
drinks = ['beer','wine','gin']
print(drinks)
print(drinks[-1])

drinks.append('rum')
print(drinks)

print(len(drinks))
pub = {'name':'Red Lion','town':'Chipping Campden','rooms':5}

print(pub['name'])

pub['postcode'] = 'GL55 6AS'
print(pub)
print((pub.keys()))
print((pub.values()))

greeting = f"Welcome to {pub['name']}"
print(greeting)

print(f'Price: £{price:.2f}')
total = 3 * price
print(f'3 pints = £{total:.2f}')

disc = total * 0.1
final = total - disc
print(final)

print('hello'.upper())

text = ' messy data '
cleaned = text.lower().title().strip()
print(cleaned)

print('fish and chips'.replace('and', '&'))
