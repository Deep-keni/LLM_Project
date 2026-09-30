from google import genai 
import os 
from dotenv import load_dotenv 
from google.genai import types
import gradio as gr

load_dotenv()

languages = {
	"Hindi": "You are a translation system. Translate the user's text into Hindi. Return only the translation.",
	"Telugu": "You are a translation system. Translate the user's text into Telugu. Return only the translation.",
	"French": "You are a translation system. Translate the user's text into French. Return only the translation.",
}

def language_translator(user_ques, language):
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise gr.Error("Set GENAI_API_KEY in your .env file to translate text.")

    client = genai.Client(api_key=api_key)
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

demo = gr.Interface(
    fn=language_translator,
    inputs=[
        gr.Textbox(label="Enter your text"),
        gr.Dropdown(choices=list(languages.keys()), label="Select a language")
    ],
    outputs=gr.Textbox(label="Translated text") , 
    title="Multi-Language Translator Assistant",
    description="This application translates text into multiple languages using the Gemini LLM. Enter your text and select a language to get the translation."
)
demo.launch(inbrowser=True)