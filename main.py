import gradio as gr
import pandas as pd


def get_plot(mu: int, beta: int, gamma: int, S: int, I: int, R: int):
    S_data, I_data, R_data = [], [], []
    TIME = 1000
    for time in range(TIME):
        S_data.append(S)
        I_data.append(I)
        R_data.append(R)
        dS = mu - beta * S * I - mu * S
        dI = beta * S * I - gamma * I - mu * I
        dR = gamma * I - mu * R
        S += dS
        I += dI
        R += dR

    symbol = []
    for i in ['S', 'I', 'R']:
        for _ in range(TIME):
            symbol.append(i)

    rates = []
    for data in [S_data, I_data, R_data]:
        for j in data:
            rates.append(j)

    graphData = pd.DataFrame({
        "symbol": symbol,
        "time": list(range(TIME)) * 3,
        "rates": rates
    })

    return gr.LinePlot(
        graphData,
        x="time",
        y="rates",
        color="symbol",
        color_legend_position="bottom",
        title="SIR Model",
        tooltip=["time", "rates", "symbol"],
        height=300,
        width=500,
    )


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            mu = gr.Number(label="µ(개인의 사망률 & 모집단의 출생률)")
            beta = gr.Number(label="β(전파율)")
            gamma = gr.Number(label="γ(회복률)")
        with gr.Column():
            S = gr.Number(label="S(취약자 비율)")
            I = gr.Number(label="I(감염자 비율)")
            R = gr.Number(label="R(회복자 비율)")
    runButton = gr.Button("Run")
    plot = gr.LinePlot(show_label=False)
    runButton.click(get_plot, [mu, beta, gamma, S, I, R], plot)

if __name__ == "__main__":
    demo.launch(share=True)
