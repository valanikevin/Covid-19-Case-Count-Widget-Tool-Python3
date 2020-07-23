
#Author: Kevin Valani
from flask import Flask, render_template
from covid import Covid

app = Flask(__name__)
covid = Covid(source="worldometers")

@app.template_filter()
def caseFormat(value):
    value = float(value)
    return "${:.2f}".format(value)

@app.route('/')
def hello_world():
    cases = covid.get_data()
    return render_template("headers.html", cases = cases, pageTitle = "Covid-19 Widgets | Kevin Valani")

@app.route('/widget/<cName>')
def widget(cName):
    cases = covid.get_status_by_country_name(cName)
    return render_template("widget.html", case=cases, pageTitle = cName+ " Covid-19 Widget")


if __name__ == '__main__':
    app.run(debug=False)
