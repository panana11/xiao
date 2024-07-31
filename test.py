import openai
import pandas as pd

# Define the API key and setup OpenAI
api_key = 'your_openai_api_key_here'
openai.api_key = api_key

# Define Australian cities and seasons
cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]
seasons = ["Summer", "Autumn", "Winter", "Spring"]

# Initialize a DataFrame
df = pd.DataFrame(index=seasons, columns=cities)

# Function to fetch weather description
def get_weather_description(city, season):
    prompt = f"Describe the typical weather in {city} during {season}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60
    )
    return response.choices[0].text.strip()

# Populate the DataFrame
for city in cities:
    for season in seasons:
        df.at[season, city] = get_weather_description(city, season)

# Save to CSV
df.to_csv('weather_descriptions.csv')

# Instructions for GitHub (manual)
print("Please manually create a private GitHub repository and invite 'david@microburbs.com.au' as a collaborator.")