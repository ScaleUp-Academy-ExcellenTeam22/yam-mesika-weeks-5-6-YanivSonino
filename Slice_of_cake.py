

def get_recipe_price(prices, **ingredients):
    if not prices or not ingredients:
        return 0

    sum = 0
    for item, amount in ingredients.items():
        if prices.get(item) == 'optionals':
            continue
        if prices.get(item):
            sum += prices.get(item) * amount/100
    return int(sum)


# tests
print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))