from recipes.models import Recipe


def run():
    recipes = Recipe.objects.all()

    for recipe in recipes:
        # now loop through the steps
        for step in recipe.steps.all():
            print(step.directions)
