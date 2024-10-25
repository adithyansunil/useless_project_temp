import google.generativeai as genai
import os

# Set your API key
GOOGLE_API_KEY = "AIzaSyAtwMj6sTnjcXyKZO4c0j1Mc_kMbrLACdE"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Define the character and scenario prompt
character_prompt = "You are a politician."
user_input = input("Enter your prompt: ")  # Get user input

# Combine prompts
combined_prompt = f"{character_prompt} {user_input}"

# Generate response
try:
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Use generate_content without specifying 'content' or 'prompt'
    response = model.generate_content(
        combined_prompt  # Pass combined_prompt directly
    )
    
    print(response)  # Print the generated content
except Exception as e:
    print(f"Error: {e}")