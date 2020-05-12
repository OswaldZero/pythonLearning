from flask import Flask,request,url_for,render_template
app=Flask(__name__)
@app.route('/family',methods=['GET','POST'])
def sing():
    title1='Python'
    content1='Hello nige'
    return render_template('index.html',title=title1,content=content1)
if __name__ == "__main__":
    app.run('127.0.0.1',port=10000)