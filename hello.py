from flask import Flask  
app = Flask(__name__)    
@app.route('/')          


def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def success():
    return "Dojo"

@app.route('/say/<string:name>')
def name(name):
    return "Hi " + name

@app.route("/repeat/<int:number>/<name>")
def repeat(name, number):
    return name * number

if __name__=="__main__":   
    app.run(debug=True) 