import os
import openai
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a helpful and kind AI assistant named Botsby"}
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(
    lines=7,
    label="Ask Botsby anything!"
)
outputs = gr.outputs.Textbox(
    label="Botsby"
)

gr.Interface(
    fn=chatbot,
    inputs=inputs,
    outputs=outputs,
    title="Botsby, most helpful AI assistant",
    description="Chat with Botsby!",
    theme="default"
).launch(share=True)
