from flask import Flask,request,url_for
app=Flask(__name__)
@app.route('/nige',methods=['get','post'])
def nige():
    return url_for('nige')
if __name__ == "__main__":
    app.run('127.0.0.1',port=10000,debug=True)
    