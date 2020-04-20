from flask import  Flask
app = Flask(__name__)

@app.route("/<numero>", methods= ['GET', 'POST'])
def ola(numero):
    return 'Hello, World!. {}'.format(numero)

if __name__ == "__main__":
    # esse debug é util em desenvolvimento
    app.run(debug= True)