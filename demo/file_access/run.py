#!/usr/bin/env gradio

import gradio as gr


def greet(name):
    return "Hello " + name + "!"

gr.set_static_paths("/tmp/")
# check: http://127.0.0.1:7860/gradio_api/file=/tmp/README.md

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox", api_name="predict")
# demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()
