import gradio as gr
import pandas as pd


def get_plot(lam: float, mu: float, beta: float, gamma: float, S: float, I: float, R: float, T: int):
    if S + I + R != 1:
        raise ValueError("S + I + R must be 1")
    S_data, I_data, R_data = [], [], []
    for time in range(int(T)):
        S_data.append(S)
        I_data.append(I)
        R_data.append(R)
        dS = lam - beta * S * I - mu * S
        dI = beta * S * I - gamma * I - mu * I
        dR = gamma * I - mu * R
        S += dS
        I += dI
        R += dR

    symbol = []
    for i in ['S', 'I', 'R']:
        for _ in range(int(T)):
            symbol.append(i)

    rates = []
    for data in [S_data, I_data, R_data]:
        for j in data:
            rates.append(j)

    graphData = pd.DataFrame({
        "symbol": symbol,
        "time": list(range(int(T))) * 3,
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
            lam = gr.Number(label="λ(출생률)")
            mu = gr.Number(label="µ(사망률)")
            beta = gr.Number(label="β(전파율)")
            gamma = gr.Number(label="γ(회복률)")
        with gr.Column():
            S = gr.Number(label="S(취약자 비율)")
            I = gr.Number(label="I(감염자 비율)")
            R = gr.Number(label="R(회복자 비율)")
            T = gr.Number(label="TIME(시행 횟수)", value=1000)
    runButton = gr.Button("Run")
    plot = gr.LinePlot(show_label=False)
    runButton.click(get_plot, [lam, mu, beta, gamma, S, I, R, T], plot)

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', server_port=8080)