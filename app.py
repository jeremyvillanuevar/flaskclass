from flask import Flask, render_template, jsonify
app=Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    return app.url_for('give_greeting', name='Mark')

@app.route('/helloworld')
def hello_world():
    return "Hello world"

@app.route('/routed')
def hello_world_otraruta():
    return "Hello world de otra ruta"

@app.route('/temp')
def hello_world_temp():
    lista ={1,2,3,4,5}
    return render_template("ejemplo.html",nombre="Jeremy",lista=lista)

@app.route("/hello/<username>")
def hello_user(username):
    print(app.url_for('hello_world_otraruta', name='Mark'))
    return "Hello {} !".format(username)

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)

@app.route('/obtener_lista')
def obtener_lista():
    lista = [
        {'num':1, 'visible':True},
        {"num":2, "visible":True},
        {"num":3, "visible":False}
    ]
    return jsonify(lista)

if __name__=="__main__":
    app.run(debug=True)