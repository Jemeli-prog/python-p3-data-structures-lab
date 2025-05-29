
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [n.get('name', 'Key does not exist') for n in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [n for n in spicy_foods if n.get('heat_level') > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(n.get('name'), end=' (')
        print(n.get('cuisine'), end=') | ')
        print('Heat Level: '+ '🌶'* n.get('heat_level'))
        
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        for n in spicy_foods:
            if n.get('cuisine') == cuisine:
                return(n)


def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n.get('heat_level') > 5:
            print(n.get('name'), end=' (')
            print(n.get('cuisine'), end=') | ')
            print('Heat Level: '+ '🌶'* n.get('heat_level'))

def get_average_heat_level(spicy_foods):
    count = 0
    for n in spicy_foods:
        count += n.get('heat_level')
    return count / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

get_spiciest_foods(spicy_foods)
