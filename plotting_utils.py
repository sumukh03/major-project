from plotly import graph_objs as go

def plot_raw_data(data,color):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"],y=data["Close"],name="stock_close"))
    # fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True,yaxis_rangeslider_visible=True)
    fig.update_layout(
        dict(
            title="Time series with range slider and selectors",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list(
                        [
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="YTD", step="year", stepmode="todate"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(step="all"),
                        ]
                    )
                ),
                rangeslider=dict(visible=True),
                type="date",
            ),
        )
    )
    fig.update_traces(line=dict(color=color))
    return fig

