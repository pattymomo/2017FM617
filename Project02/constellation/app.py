from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['projectFilepath']
    # your code
    # return a response
    description = "這是說明"
    return render_template('results.html', name=name, description=description)

if __name__=="__main__":
    app.run()
