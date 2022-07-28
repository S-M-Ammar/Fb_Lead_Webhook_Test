from flask import Flask,render_template,request
application = Flask(__name__)

@application.route("/")
def home():
    return ("Home Page")


@application.route("/webhook",methods=['POST','GET'])
def webhook():
    print(request.form)
    print("Got something from facebook")
    x = request.args.get("hub.challenge")
    return (x)


if __name__ == '__main__':
    application.run(debug=True)
