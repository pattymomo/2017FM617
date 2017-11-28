import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    df = pd.read_csv("nyse.csv")
    return df.to_html()

@app.route('/nyse/<symbol>')
def nyse(symbol):
    df = pd.read_csv("nyse.csv")
    goto = df.loc[df['Symbol']
    return goto.to_html()

@app.route('/nasdaq')
def nyse():
    df = pd.read_csv("nasdaq.csv")
    return df.to_html()

@app.route('/nasdaq/<symbol>')
def nasdq(symbol):
    df = pd.read_csv("nasdaq.csv")
    goto = df.loc[df['Symbol']
    return goto.to_html()

@app.route('/amex')
def amex():
    df = pd.read_csv("amex.csv")
    return df.to_html()

@app.route('/amex/<symbol>')
def nasdq(symbol):
    df = pd.read_csv("amex.csv")
    goto = df.loc[df['Symbol']
    return goto.to_html()

if __name__ == '__main__':
    app.run()
