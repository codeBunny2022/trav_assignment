
```markdown
# Personalized Travel Itinerary Generator

This project is an AI-powered travel itinerary generator built with **Streamlit** and **OpenAI**. It allows users to provide their travel preferences, budget, duration, and destination, and the system will generate a personalized day-by-day itinerary.

## **Objective**

The goal of this project is to create a prompt system that gathers user input, refines preferences, and generates a detailed travel itinerary using OpenAI’s GPT-3 model. The prompts aim to simulate a conversation with the user to understand their travel preferences in depth and suggest personalized activities accordingly.

## **Project Structure**
```

personalized_travel_itinerary/
│
├── [app.py](http://app.py)                   # Main Streamlit app file
├── [prompts.py](http://prompts.py)               # Contains the prompt system
├── requirements.txt         # List of dependencies
└── [README.md](http://README.md)                # Project documentation

```

## **Technologies Used**

- **Streamlit**: For building the web interface.
- **OpenAI GPT-3**: For generating personalized itineraries based on user input.
- **Python**: The main language for development.

## **How It Works**

### **Prompt System Breakdown**

1. **System Prompt**: 
   - **Purpose**: To set the context for the AI model and inform it that it’s helping a user plan a personalized travel itinerary.
   - **Reasoning**: Starting with a broad, clear instruction ensures that the AI understands the goal and prepares to collect relevant details.

2. **Gather User Input Prompt**:
   - **Purpose**: To collect key information about the user's trip, such as destination, budget, duration, and preferences.
   - **Reasoning**: This is the foundation for personalizing the itinerary. By asking for these specifics, we ensure that the AI can generate a plan suited to the user's needs.

3. **Refining Preferences Prompt**:
   - **Purpose**: To dive deeper into the user's specific preferences and clarify ambiguous inputs.
   - **Reasoning**: Some user inputs are broad or vague, so asking follow-up questions allows for better precision in the final itinerary. For example, asking whether they prefer luxury or budget accommodation ensures that the generated plan aligns with the user’s financial expectations.

4. **Activity Suggestions Prompt**:
   - **Purpose**: Based on the user's preferences, generate activity suggestions, including famous tourist spots and hidden gems.
   - **Reasoning**: Tailoring suggestions to the user’s preferences (famous vs. offbeat, nature vs. city life) ensures that the itinerary is unique and meaningful.

5. **Generate Itinerary Prompt**:
   - **Purpose**: To create a day-by-day breakdown of the itinerary, incorporating suggested activities and optimizing the schedule.
   - **Reasoning**: This step brings everything together into a coherent structure, ensuring the user gets a detailed and well-organized travel plan.

### **Handling Vague or Incomplete Inputs**

The system includes an **Input Refinement** process where, if a user’s input is vague, they are prompted for more information. For example, if a user says they have a "moderate budget" but doesn't elaborate, the system will ask for more specifics. This ensures that the AI has enough context to generate precise and useful suggestions.

### **Bonus Challenge: Flexible Input Formats**

The prompt system tackles the bonus challenge by handling mixed input formats and refining vague responses. For instance:

- If the user says, "I have a moderate budget and I want a mix of famous and offbeat places," the system refines the query by asking whether they want famous attractions in the morning and offbeat locations in the afternoon, thus organizing their preferences better.
- If the user provides an incomplete input, like “I like nature,” the system prompts for clarification by asking, “Would you prefer mountains, beaches, or forests?” This ensures the system understands the specifics of the user’s interests.

## **How to Run the App**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/personalized_travel_itinerary.git
```

### **2. Install Dependencies**

Navigate to the project directory and install the necessary libraries:

```bash
pip install -r requirements.txt
```

### **3. Set up OpenAI API Key**

To use OpenAI’s GPT-3 model, you need to set up an API key. Replace `'YOUR_OPENAI_API_KEY'` in `app.py` with your actual API key.

### **4. Run the Application Locally**

Once dependencies are installed, you can run the application:

```bash
streamlit run app.py
```

This will launch the app locally, and you can access it in your browser at `http://localhost:8501`.

### **5. Deploy on Streamlit Community Cloud**


1. Create an account on [Streamlit Cloud](https://streamlit.io/cloud).
2. Push your project to GitHub.
3. Link your GitHub repository to Streamlit and deploy the app.

### **6. User Testing**

Once deployed, you can share the live URL with others for testing and feedback.


```

---

### **Explanation of Key Sections**:

1. **Prompt System**: The prompts have been designed to progressively narrow down the user's preferences. The system starts by gathering general information and then refines those details with follow-up questions. This ensures the final itinerary is well-aligned with the user's expectations.

2. **Flexible Input Handling**: We implemented flexible input processing by asking for additional details when necessary. This allows us to refine the user input and generate an itinerary that is highly personalized.

3. **Bonus Challenge**: We tackled the challenge by refining broad statements like "moderate budget" and "I want a mix of famous and offbeat places" into more specific preferences that guide the itinerary generation.

Let me know if you need more details on any part of the project or any adjustments!
```


