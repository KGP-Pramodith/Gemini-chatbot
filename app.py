from google import genai
from google.genai import types

client = genai.Client(api_key="****************add_your_api_key_here****************")

while True:
    question = input("USER : ")
    if question.lower() != "bye":
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            ),
        )
        print(response.text)
    else:
        print("Bye...!")
        break