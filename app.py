from flask import Flask, render_template, request, redirect, abort
from bokeh.embed import components
import csv

app = Flask(__name__)

app.vars={}

# Load in stock data, writing as sg to be able to call to the functions later on
import StockGraphs as sg

@app.route('/',methods=['POST'])
def index_savel ():

    # Creating list of stocksymbols users can enter, and giving in error message if they enter letters that aren't stock
    myfile = open("stocktickers.csv", "r")
    stocksymbols = csv.reader(myfile)
    stocksymbolslist = []
    for row in stocksymbols:
        stocksymbolslist.append(row[0])


    # request was a POST
    app.vars['ticker_symbol'] = request.form['stockform']
    if app.vars['ticker_symbol'] in stocksymbolslist:
        return index(app.vars['ticker_symbol'])
    else:
        abort(406)




# Index page
@app.route('/',methods=['GET'])
# putting the equal sign after sets a default value
def index(co='AAPL'):
    # which metric was selected by user
    metric = request.form.get("feature_name")
    # setting a default metric
    if metric == None:
        metric = "close"



    options = ['open', 'close', 'high', 'low', 'volume']




    # Make the Plot

    plot = sg.getstockplot(co,metric)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)


    return render_template("template.html", script=script, div=div,
        feature_names=options,  current_feature_name=metric)





if __name__ == '__main__':
  app.run(port=33507)