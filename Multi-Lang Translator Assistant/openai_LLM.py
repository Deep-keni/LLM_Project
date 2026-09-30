import os 
from dotenv import load_dotenv 
from openai import OpenAI
import gradio as gr

load_dotenv()

languages = {
	"Hindi": "You are a translation system. Translate the user's text into Hindi. Return only the translation.",
	"Telugu": "You are a translation system. Translate the user's text into Telugu. Return only the translation.",
	"French": "You are a translation system. Translate the user's text into French. Return only the translation.",
}

def language_translator(user_ques, language):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise gr.Error("Set GROQ_API_KEY in your .env file to translate text.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": languages[language]},
            {"role": "user", "content": user_ques},
        ],
        temperature=0.5,
        max_tokens=1000,
    )
    return response.choices[0].message.content

demo = gr.Interface(
    fn=language_translator,
    inputs=[
        gr.Textbox(label="Enter your text"),
        gr.Dropdown(choices=list(languages.keys()), label="Select a language")
    ],
    outputs=gr.Textbox(label="Translated text") ,
    title="Multi-Language Translator Assistant",
    description="This application translates text into multiple languages using the LLaMA LLM. Enter your text and select a language to get the translation."
)
demo.launch(inbrowser=True)