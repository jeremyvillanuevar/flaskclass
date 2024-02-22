from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    print(app.url_for('give_greeting', name='Mark'))

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

if __name__=="__main__":
    app.run(debug=True)