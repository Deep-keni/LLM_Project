from google import genai 
import os 
from dotenv import load_dotenv 
from google.genai import types

load_dotenv() 

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

languages = {
	"Hindi": "You are a translation system. Translate the user's text into Hindi. Return only the translation.",
	"Telugu": "You are a translation system. Translate the user's text into Telugu. Return only the translation.",
	"French": "You are a translation system. Translate the user's text into French. Return only the translation.",
}

def language_translator(user_ques, language):

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_ques,
        config=types.GenerateContentConfig(
            system_instruction=languages[language],
            temperature = 0.5,
            max_output_tokens = 1000
        )
    )
    return response.text

print("Select the language to translate into:")
for index, language_name in enumerate(languages, start=1):
    print(f"{index}. {language_name}")

while True:
    choice = input("Enter a number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(languages):
        language = list(languages)[int(choice) - 1]
        break
    print("Please enter a valid language number.")

user_ques = input("Enter your text: ")
output = language_translator(user_ques, language)
print(f"Translated text in {language}: {output}")
