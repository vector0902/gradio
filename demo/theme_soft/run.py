import gradio as gr
import time

# https://www.gradio.app/guides/theming-guide

# after theme change, need restart to work
theme=gr.themes.Soft()
theme=gr.themes.Base()
# theme=gr.themes.Color()
theme=gr.themes.Default()
theme=gr.themes.Glass()
theme=gr.themes.Monochrome()
theme=gr.themes.Origin()
theme=gr.themes.Citrus()
theme=gr.themes.Ocean()
# theme=gr.themes.GoogleFont()

with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Name", value=f"hi {theme}")
    slider = gr.Slider(label="Count", minimum=0, maximum=100, step=1, value=2)
    with gr.Row():
        button = gr.Button("Submit", variant="primary")
        clear = gr.Button("Clear")
    output = gr.Textbox(label="Output")

    def repeat(name, count):
        # time.sleep(3)
        return name * count

    button.click(repeat, [textbox, slider], output)

if __name__ == "__main__":
    demo.launch(
        theme=theme
        # theme=gr.themes.Soft()
        # theme=gr.themes.Base()
        # theme=gr.themes.Glass()
        )
