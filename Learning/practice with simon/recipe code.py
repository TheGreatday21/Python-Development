import random

ingredients = {#create  aa library containing tuples and lists
    "Protein": ["chicken", "beef", "tofu", "lentils"],
    "Vegetables": ["broccoli", "carrots", "spinach", "peppers"],
    "Grains": ["rice", "quinoa", "pasta", "couscous"],
    "Flavor": ["garlic", "ginger", "soy sauce", "lime juice"]
}

cuisines = {
    "Italian": {"Flavor": ["basil", "oregano", "parmesan"]},
    "Mexican": {"Flavor": ["cumin", "chili powder", "cilantro"]},
    "Indian": {"Flavor": ["turmeric", "coriander", "garam masala"]}
}

def generate_recipe(cuisine="Random"):
    if cuisine == "Random":
        cuisine = random.choice(list(cuisines.keys()))

    recipe = {}
    for category, options in ingredients.items():
        recipe[category] = random.choice(options)

    if cuisine in cuisines:
        recipe["Flavor"] += cuisines[cuisine]["Flavor"]

    print(f"\n{cuisine} Recipe:")
    for category, ingredient in recipe.items():
        print(f"- {category}: {ingredient}")

if __name__ == "__main__":
    while True:
        cuisine_choice = input("Choose a cuisine (Italian, Mexican, Indian, Random, or 'q' to quit # Write your text in lower case): ")
        if cuisine_choice.lower() == 'q':
            break
        generate_recipe(cuisine_choice)