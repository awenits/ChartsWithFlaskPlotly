from flask import Flask, render_template

import helpers


app = Flask(__name__)

@app.route('/')
def hello_world():

    # using chart function which is in helpers to generate chart
    # you can pass the dynamic values(data scraped from worldometer which you are converting into dictionary)
    # to chart function and use data in chart function acordingly
    # currently I just used some static values here.
    chart = helpers.chart(502876, 158273, 147577)

    # render results
    return render_template("plot.html", chart=chart)

if __name__ == '__main__':
    app.run()

