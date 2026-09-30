import os 
from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

languages = {
	"Hindi": "You are a translation system. Translate the user's text into Hindi. Return only the translation.",
	"Telugu": "You are a translation system. Translate the user's text into Telugu. Return only the translation.",
	"French": "You are a translation system. Translate the user's text into French. Return only the translation.",
}

def language_translator(user_ques, language):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": languages[language]},
            {"role": "user", "content": user_ques},
        ],
        temperature=0.5,
        max_tokens=1000,
    )
    return response.choices[0].message.content

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
