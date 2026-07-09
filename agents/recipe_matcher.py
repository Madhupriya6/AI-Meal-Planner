def ingredient_overlap(recipe_ingredients, available):

    recipe_set = set(recipe_ingredients)
    available_set = set(available)

    overlap = recipe_set.intersection(available_set)

    return len(overlap) / len(recipe_set)
