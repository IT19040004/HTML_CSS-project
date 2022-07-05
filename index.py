from flask import Flask, make_response, redirect, session, url_for, render_template, request, jsonify, json


app = Flask(__name__)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('user_Login')


@app.route("/")
def home():
    return render_template("Login.html")
    
@app.route('/Login', methods=['GET', 'POST'])
def login():
   
    email = request.form['email']
    password = request.form['password']

    print(email)
    print(password)
    
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]

    mail = [item.get('email') for item in all_todos]
    p = [item.get('password') for item in all_todos]
    

    for x in range(len(mail)):
        if email == mail[x]:
            result1 = 1
            break
        else:
            result1 = 0
    
    for x in range(len(p)):
        if password == p[x]:
            result2 = 1
            break
        else:
            result2 = 0
    
    if result1 == 1 and result2 == 1:
        return render_template("index.html")
    else:
         return render_template("Login.html")

@app.route('/register', methods=['POST'])
def create():
   
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        try:
            x = {
              "user" : request.form['user'],
              "email" : request.form['email'],
              "password" : request.form['password']

            }

            todo_ref.document().set(x)
            return render_template("Login.html")

        except Exception as e:
            return render_template("Login.html")
    
if __name__== "__main__":
      app.run()
