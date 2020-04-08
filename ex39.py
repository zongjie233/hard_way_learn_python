# kaws
states = {
    'Oregon' :  'OR',
    'Florida' : 'FL',
    'California' :'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'

}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'

}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print(f"OR State has: {cities['OR']}")

#print some states  abbreviation:缩写
print('-' * 10)
print("Michigan's abbreviation is ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("sorry, no Texas")

#get a city with a default value
#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")













