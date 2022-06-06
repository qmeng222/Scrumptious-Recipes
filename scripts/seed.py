from recipes.models import FoodItem, Ingredient, Measure, Recipe, Step


def run():
    # Delete all the existing items
    Recipe.objects.all().delete()
    Ingredient.objects.all().delete()
    Measure.objects.all().delete()
    FoodItem.objects.all().delete()
    Step.objects.all().delete()

    # Create some recipes

    cake1 = Recipe.objects.create(
        name="One Bowl Chocolate Cake",
        author="shirleyo",
        description="This is a rich and moist one bowl chocolate cake. It only takes a few minutes to prepare the batter. Frost with your favorite chocolate frosting.",
        image="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F43%2F2022%2F04%2F22%2F17981-one-bowl-chocolate-cake-iii-Dianne-1x1-1.jpg&w=272&h=272&c=sc&poi=%5B620%2C880%5D&q=60",
    )

    cake2 = Recipe.objects.create(
        name="Back-of-the-Box Hershey's Chocolate Cake",
        author="rach56",
        description="A rich moist chocolate cake with a chocolate buttercream icing. This is the best cake in the world!",
        image="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F693494.jpg&w=272&h=272&c=sc&poi=face&q=60",
    )

    # Create the measures
    cups = Measure.objects.create(name="Cups", abbreviation="cups")
    tsp = Measure.objects.create(name="Teaspoons", abbreviation="tsp")
    tbsp = Measure.objects.create(name="Tablespoons", abbreviation="tbsp")
    na = Measure.objects.create(name="", abbreviation="")

    # Create the FoodItems
    # Trick: Use a loop to keep from repeating ourselves!
    foods = [
        "white sugar",
        "all-purpose flour",
        "cocoa powder",
        "baking powder",
        "baking soda",
        "salt",
        "eggs",
        "milk",
        "vegetable oil",
        "vanilla extract",
        "boiling water",
    ]

    # This will hold our completed food objects
    food_objects = []
    for food in foods:
        food_object = FoodItem.objects.create(name=food)
        # Make sure to save the food objects, we need the later
        # for ingredients
        food_objects.append(food_object)

    # Create ingredients for the first cake
    # Note we have to use the foods from our food_objects list
    Ingredient.objects.create(
        amount=2, measure=cups, recipe=cake1, food=food_objects[0]
    )
    Ingredient.objects.create(
        amount=1.25, measure=cups, recipe=cake1, food=food_objects[1]
    )
    Ingredient.objects.create(
        amount=0.75, measure=cups, recipe=cake1, food=food_objects[2]
    )
    Ingredient.objects.create(
        amount=1.5, measure=tsp, recipe=cake1, food=food_objects[3]
    )
    Ingredient.objects.create(
        amount=1.5, measure=tsp, recipe=cake1, food=food_objects[4]
    )
    Ingredient.objects.create(
        amount=1, measure=tsp, recipe=cake1, food=food_objects[5]
    )
    Ingredient.objects.create(
        amount=2, recipe=cake1, measure=na, food=food_objects[6]
    )
    Ingredient.objects.create(
        amount=1, recipe=cake1, measure=cups, food=food_objects[7]
    )
    Ingredient.objects.create(
        amount=0.5, recipe=cake1, measure=cups, food=food_objects[8]
    )
    Ingredient.objects.create(
        amount=2, recipe=cake1, measure=tsp, food=food_objects[9]
    )
    Ingredient.objects.create(
        amount=1, measure=cups, recipe=cake1, food=food_objects[10]
    )

    # Create steps for the first cake
    Step.objects.create(
        order=1,
        recipe=cake1,
        directions="Preheat oven to 350 degrees F (175 degrees C). Grease and flour two nine inch round pans.",
    )

    Step.objects.create(
        order=2,
        recipe=cake1,
        directions="In a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda and salt. Add the eggs, milk, oil and vanilla, mix for 2 minutes on medium speed of mixer. Stir in the boiling water last. Batter will be thin. Pour evenly into the prepared pans.",
    )

    Step.objects.create(
        order=3,
        recipe=cake1,
        directions="Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick. Cool in the pans for 10 minutes, then remove to a wire rack to cool completely.",
    )
