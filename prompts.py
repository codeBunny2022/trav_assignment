def system_prompt():
    return """I am an AI travel assistant. Please answer the following questions to help me create a personalized travel itinerary for you."""

def gather_user_input():
    return """Please provide the following details:
    - Destination: Where are you traveling to?
    - Budget: How much are you willing to spend on this trip (low, moderate, high)?
    - Trip Duration: How many days will you be traveling?
    - Purpose: What’s the purpose of your trip (leisure, business, adventure)?
    - Preferences: Any specific interests (e.g., food, culture, nature)?"""

def refine_preferences():
    return """Could you provide more details about your preferences?
    - Do you have any dietary restrictions?
    - Would you prefer luxury or budget accommodation?
    - Do you prefer more famous tourist attractions or offbeat hidden gems?
    - Are there any mobility or walking preferences (e.g., walking tours, relax mode)?"""

def activity_suggestions(budget, preferences):
    return f"""Based on your {budget} budget and preferences for {preferences}, I will suggest a set of activities. Do you prefer a mix of famous and hidden attractions, or focus on one category?"""

def generate_itinerary(destination, duration, activities):
    itinerary = []
    for day in range(1, duration + 1):
        activity = activities[day % len(activities)]
        itinerary.append(f"Day {day}: {activity}")
    return f"Here is your {duration}-day itinerary for {destination}:\n" + "\n".join(itinerary)
