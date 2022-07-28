from flask import Flask,render_template,request
application = Flask(__name__)

@application.route("/")
def home():
    return ("Home Page")


@application.route("/webhook",methods=['POST','GET'])
def webhook():
    print(request.form)
    print("Got something from facebook")
    return ("1445710072")


if __name__ == '__main__':
    application.run(debug=True)
