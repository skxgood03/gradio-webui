import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("文生图"):
        with gr.Row():
            with gr.Column(scale=13):
                text1 = gr.Textbox(label="正向提示词", lines=2)
                text2 = gr.Textbox(label="反向提示词", lines=2)
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button("1")
                button2 = gr.Button("2")
                button3 = gr.Button("3")
                button4 = gr.Button("4")
            with gr.Column(scale=6):
                button_big = gr.Button("提交", variant='primary')
                with gr.Row():
                    xlk1 = gr.Dropdown(["1", "2", "3"], label="xlk1")
                    xlk2 = gr.Dropdown(["1", "2", "3"], label="xlk2")
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown1 = gr.Dropdown(["1", "2", "3"], label="dropdown1")
                    slider1 = gr.Slider(minimum=0, maximum=100, label='slider1')

                checkbox1 = gr.CheckboxGroup(['a', 'b', 'c'])
                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=1000, label='slider2')
                    slider3 = gr.Slider(minimum=0, maximum=1000, label='slider3')
                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=1000, label='slider4')
                    slider5 = gr.Slider(minimum=0, maximum=1000, label='slider5')
                slider6 = gr.Slider(minimum=0, maximum=1000, label='slider6')
                with gr.Row():
                    dropdown2 = gr.Dropdown(["1", "2", "3"], label="dropdown2")
                    button5 = gr.Button("5")
                    button6 = gr.Button("6")
                    check = gr.Checkbox(label="check")
                script = gr.Dropdown(["1", "2", "3"], label="script")
            with gr.Column():
                image1 = gr.Gallery(label="image1",columns=3)
                with gr.Row():
                    button7 = gr.Button("7",min_width=1)
                    button8 = gr.Button("8",min_width=1)
                    button9 = gr.Button("9",min_width=1)
                    button10 = gr.Button("10",min_width=1)
                    button11 = gr.Button("11",min_width=1)
                    button12 = gr.Button("12",min_width=1)
                tex3 = gr.Textbox(label="text3", lines=4)
    with gr.Tab("图生图"):
        pass
    with gr.Tab("..."):
        pass
demo.launch()
