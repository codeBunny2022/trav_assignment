import streamlit as st
import openai
from prompts import system_prompt, gather_user_input, refine_preferences, activity_suggestions, generate_itinerary

# Setup OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

st.title('Personalized Travel Itinerary Generator')

st.write(system_prompt())

st.subheader("Please provide your details")
destination = st.text_input("Destination")
budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
duration = st.number_input("Trip Duration (in days)", min_value=1)
purpose = st.text_input("Purpose of your trip")
preferences = st.text_area("Your preferences")

if st.button("Generate Itinerary"):
    user_input = f"{destination}, {budget}, {duration} days, {purpose}, {preferences}"
    st.write(f"User Input: {user_input}")

    refine_prompt = refine_preferences()
    refined_preferences = st.text_area(refine_prompt)
    
    activity_prompt = activity_suggestions(budget, refined_preferences)
    st.write(activity_prompt)

    activities = [
        "Arrival, local sightseeing",
        "Museum visit, city tour",
        "Hiking, cultural experience",
        "Relaxing at the beach/spa",
        "Shopping and local food experience"
    ]
    itinerary = generate_itinerary(destination, duration, activities)
    st.write(itinerary)
