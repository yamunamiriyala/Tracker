from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! from yamunas PCs'



if __name__ == '__main__':
	app.run(host = '192.168.0.127',port = 8080, debug = True)