# A Flask App to Track Stock Prices

This project ties together concepts from The Data Incubator's 12 day prep course. Including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The [finished app](https://savel-milestone.herokuapp.com) accepts input about a particularly stock and tracks various pricing information for that particular stock.

## Heroku

- This app uses Heroku for hosting purposes
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).
- This app runs using the app.py script, which calls StockGraphs.py, as well as template.html.

## Accessing Data from API

- This project utilizes the pandas DataReader to access The Investors Exchange (IEX) provides a wide range of data through an API.
- Additional documentation on the reader can be found [here](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-iex). 


## Using Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- A plotting function exists in the StockGraphs.py.
- The plotting function is called by the app to plot whichever stock prices the users input data requires
- Flask is used to make the plot visible on the website through embedded HTML

