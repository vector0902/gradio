#!/usr/bin/env gradio

import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    celsius = (temperature - 32) * 5 / 9
    greeting = f"{salutation} {name}. It is {temperature} degrees F, {celsius} degrees C today"
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
    api_name="predict"
)
if __name__ == "__main__":
    demo.launch()
