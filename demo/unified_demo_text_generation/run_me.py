#!/usr/bin/env gradio

import gradio as gr
from openai import OpenAI

# my endpoint:
url = "http://localhost:4000"
model = "my-fixed-model"
key = "anykey"

client = OpenAI(
    base_url=url,
    api_key=key
)

def generate_text(text_prompt):
  response = client.chat.completions.create(
      model=model,
      messages=[{"role": "user", "content": text_prompt}],
      # max_tokens=30,
      n=5
  )
  return response.choices[0].message.content

textbox = gr.Textbox()

demo = gr.Interface(generate_text, textbox, textbox, api_name="predict")

if __name__ == "__main__":
    demo.launch()
