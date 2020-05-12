from flask import Flask,request,url_for,render_template,flash,abort
app=Flask(__name__)
app.secret_key='123'
@app.route('/family',methods=['GET','POST'])
def sing():
    title1='Python'
    content1=['hello','hi','ni']
    return render_template('index.html',title=title1,content=content1)
@app.route('/child')
def sound():
    return render_template('base_one.html')
@app.route('/father')
def lee():
    return render_template('base_two.html')
@app.route('/mother')
def nico():
    flash('nigo')
    return render_template('info.html')
@app.route('/may')
def query_user():
    uid=request.args.get("uid")
    if(int(uid)):
        return uid
    else:
        abort(404)
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
if __name__ == "__main__":
    app.run('127.0.0.1',port=10000)