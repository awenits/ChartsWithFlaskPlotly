import plotly

def chart(a, b, c):
    """Return a bar chart for specified corona cases as HTML."""

    # offline plot
    # https://plot.ly/python/bar-charts/
    # https://plot.ly/python/reference/#bar
    figure = {
        "data": [
            {
                "x": ["USA", "Spain", "Italy", "France", "Germany", "China", "UK", "Iran", "Turkey", "Belgium"],
                "y": [a, b, c, 124869, 122171, 81953, 73758, 68192, 47029, 26667],
                "hoverinfo": "none",
                "type": "bar"
            }
        ],
        "layout": {
            "showlegend": False,
            "title": "Top 10 Countries",
            "xaxis_title":"Countries",
            "yaxis_title": "Total Corona Cases",
            }
    }
    return plotly.offline.plot(figure, output_type="div", show_link=False, link_text=False)
