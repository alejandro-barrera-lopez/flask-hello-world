from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
	return "APP ACTUALIZADA"

if __name__ == "__main__":
	app.run()

