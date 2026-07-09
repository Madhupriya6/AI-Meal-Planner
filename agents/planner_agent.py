from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_weekly_menu(recipes, ingredients):

    prompt = f"""
    Available ingredients:
    {ingredients}

    Available Bengali recipes:
    {recipes}

    Create a 7-day Bengali meal plan starting from Sunday evening.
    Cooking happens every evening.
    Each dinner should be reused as the next day's lunch.
    For example, Sunday dinner and Monday lunch should be the same meal.
    Avoid repetition across different dinners.

    Use the following cooking-time priorities:
    - Sunday and Monday: heavier dishes are fine because you have more time to cook.
      On these days, include one dal-based dish plus one non-veg dish or a heavier/complex vegetarian meal.
      Prefer fish or chicken for one of the early-week meals (Sunday or Monday) where possible.
    - Friday: you usually eat dinner outside, so make Friday dinner optional or suggest a light/simple meal that can be skipped if you go out.
    - Tuesday, Wednesday, and Thursday: suggest lighter, quicker meals such as khichudi, daal, simple stir-fries, or quick one-pot Bengali dishes.
    - Saturday can be moderate or based on the remaining ingredient mix.

    Make sure chicken and fish dishes are separated by at least two days in the schedule.

    Every day should include one curry-style dish in the menu.

    Format the output as pairs such as:
      Sunday dinner and Monday lunch: [meal name]
      Monday dinner and Tuesday lunch: [meal name]
      Tuesday dinner and Wednesday lunch: [meal name]
      Wednesday dinner and Thursday lunch: [meal name]
      Thursday dinner and Friday lunch: [meal name]
      Friday dinner and Saturday lunch: [meal name]
      Saturday dinner and Sunday lunch: [meal name]
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
