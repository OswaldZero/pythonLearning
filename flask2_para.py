from flask import Flask,request
app=Flask(__name__)
@app.route("/user/<uid>",methods=['GET','POST'])
def hello_user():
    print
    return 'hello user'
@app.route("/nige",methods=['GET','POST'])
def hello_nige():
    uid=request.args.get('uid')
    return "hello nige"+uid
    return 
if __name__ == "__main__":
    app.run('127.0.0.1','10000',debug=True)