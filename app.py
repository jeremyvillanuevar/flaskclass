from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/routed')
def hello_world_otraruta():
    return "Hello world de otra ruta"

if __name__=="__main__":
    app.run(debug=True)