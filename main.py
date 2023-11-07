import gradio as gr


def fn(mu: int, beta: int, gamma: int, S: int, I: int, R: int):
    return mu, beta, gamma, S, I, R


# demo = gr.Interface(
#     fn=fn,
#     inputs=["number"],
#     outputs=["number"],
#     title="SIR Model",
#     article="KyungHee High School, Math II Performance Evaluation Exploration Tasks for the 2nd Semester of 2023",
#     css="footer{display:none !important}",
# )

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            mu = gr.Number(label="µ(개인의 사망률 & 모집단의 출생률)")
            beta = gr.Number(label="β(전파율)")
            gamma = gr.Number(label="γ(회복률)")
        with gr.Column():
            S = gr.Number(label="S(0)")
            I = gr.Number(label="I(0)")
            R = gr.Number(label="R(0)")
    gr.Button("Run")

if __name__ == "__main__":
    demo.launch()
