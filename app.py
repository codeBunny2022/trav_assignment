import streamlit as st
import openai
from prompts import system_prompt, refine_preferences, generate_itinerary

st.title('Personalized Travel Itinerary Generator')

# Input for OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    openai.api_key = api_key
    st.write(system_prompt())

    # Collect user inputs
    st.subheader("Please provide your details")
    destination = st.text_input("Destination (e.g., Paris, Tokyo, New York)")
    budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
    duration = st.number_input("Trip Duration (in days)", min_value=1)
    purpose = st.text_input("Purpose of your trip (e.g., Leisure, Business, Adventure)")
    preferences = st.text_area("Your preferences (e.g., Food, Culture, Nature, History)")

    if st.button("Generate Itinerary"):
        # Input validation
        if not destination or not budget or duration < 1 or not preferences:
            st.error("Please fill in all fields before generating the itinerary.")
        else:
            # Generate activity suggestions dynamically
            activity_prompt = f"""
            You are a travel assistant. Suggest a detailed list of unique activities 
            for a {duration}-day trip to {destination}. The user has a {budget.lower()} budget 
            and their preferences include {preferences}. The trip purpose is {purpose}. 
            Provide unique, day-by-day activities tailored to the location and the user’s preferences. 
            Include famous attractions, hidden gems, food experiences, and any relevant cultural or outdoor activities.
            """
            try:
                # Using gpt-3.5-turbo to generate unique activities
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful travel assistant."},
                        {"role": "user", "content": activity_prompt}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )

                activities = response['choices'][0]['message']['content'].strip().split("\n")

                # Generate the itinerary
                itinerary = generate_itinerary(destination, int(duration), activities)
                st.subheader(f"Your {duration}-day itinerary for {destination}")
                st.write(itinerary)

            except Exception as e:
                st.error(f"Error generating itinerary: {e}")
else:
    st.warning("Please enter your OpenAI API key to proceed.")
