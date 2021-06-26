from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test_fun():
   return render_template('index.htm')

if __name__=='__main__':
    app.run()