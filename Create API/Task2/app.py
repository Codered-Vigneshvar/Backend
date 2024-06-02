from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login(): 
    if request.method == 'POST':
        user = request.form['userName']
        password = request.form['userPassword']
        if user == 'Vignesh' and password == '1234':
            return 'Welcome %s' % user
        else:
            return 'Login failed for user %s' % user
    else:
        user = request.args.get('userName')
        password = request.args.get('userPassword')
        if user == 'Vignesh' and password == '1234':
            return 'Welcome %s' % user
        else:
            return 'Login failed for user %s' % user

if __name__ == "__main__":
    app.run(debug=True)

