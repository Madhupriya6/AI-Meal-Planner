import load_api_key
from scrapers.bongeats_scraper import search_recipe
from agents.planner_agent import generate_weekly_menu

DEFAULT_PANTRY = [
    "onion",
    "garlic",
    "ginger",
    "coriander leaves",
    "tomato",
    "potato",
    "moong daal",
    "masoor daal",
    "urad daal",
    "cholar daal",
    "peanuts",
    "posto",
    "soyabean",
    "eggs",
    "curd",
]


def get_ingredients():
    raw = input("Enter grocery ingredients, separated by commas: ").strip()
    user_items = [item.strip() for item in raw.split(",") if item.strip()]
    ingredients = []

    if user_items:
        ingredients.extend(user_items)
    else:
        print("No ingredients entered. Using default groceries plus pantry staples.")

    for item in DEFAULT_PANTRY:
        if item not in ingredients:
            ingredients.append(item)

    return ingredients


def show_recipe_links(recipes):
    answer = input("Would you like a recipe link for a specific dish? (y/n): ").strip().lower()
    if answer not in {"y", "yes"}:
        return

    print("\nAvailable recipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"  {index}. {recipe['title']}")

    choice = input("Enter the recipe number or name you want the link for: ").strip()
    if not choice:
        print("No recipe selected.")
        return

    selected = None
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(recipes):
            selected = recipes[index]
    else:
        normalized = choice.lower()
        for recipe in recipes:
            if normalized == recipe["title"].lower() or normalized in recipe["title"].lower():
                selected = recipe
                break

    if selected:
        print(f"\nSelected recipe:\n- {selected['title']}: {selected['url']}")
    else:
        print("Recipe not found. Please try again with a valid number or title.")


def main():
    ingredients = get_ingredients()

    recipes = []
    for item in ingredients:
        recipes.extend(search_recipe(item))

    if not recipes:
        print("No recipes found for the provided ingredients.")
        return

    recipe_titles = [recipe["title"] for recipe in recipes]
    menu = generate_weekly_menu(recipe_titles, ingredients)
    print(menu)

    show_recipe_links(recipes)


if __name__ == "__main__":
    main()
