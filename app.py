import streamlit as st
import openai
from prompts import system_prompt, gather_user_input, refine_preferences, activity_suggestions, generate_itinerary

st.title('Personalized Travel Itinerary Generator')

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    openai.api_key = api_key
    st.write(system_prompt())

    st.subheader("Please provide your details")
    destination = st.text_input("Destination")
    budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
    duration = st.number_input("Trip Duration (in days)", min_value=1)
    purpose = st.text_input("Purpose of your trip")
    preferences = st.text_area("Your preferences")

    if st.button("Generate Itinerary"):
        if not destination or not budget or duration < 1 or not preferences:
            st.error("Please fill in all fields before generating the itinerary.")
        else:
            st.write("Refining preferences...")
            refine_prompt = refine_preferences()
            refined_preferences = st.text_area(refine_prompt)

            st.write("Generating activity suggestions...")
            activity_prompt = activity_suggestions(budget, refined_preferences)
            st.write(activity_prompt)

            activities = [
                "Arrival, local sightseeing",
                "Museum visit, city tour",
                "Hiking, cultural experience",
                "Relaxing at the beach/spa",
                "Shopping and local food experience",
            ]
            itinerary = generate_itinerary(destination, int(duration), activities)
            st.write(itinerary)
else:
    st.warning("Please enter your OpenAI API key to proceed.")
