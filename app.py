from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "This is a home page"

@app.route('/welcome')
def welcome():
    return("Welcome")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Gradesheet',methods=['POST','GET'])

def Gradesheet():
    if request.method=='GET':
       return render_template("calculate.html")
    else:
        maths=int(request.form['maths'])
       
        chemistry=int(request.form["chemistry"])
        physics=int(request.form["physics"])
        avg_marks=(maths+chemistry+physics)/3
      
        percent=round(avg_marks)
        print(percent)
        return render_template("result.html",result=percent)
        #return str(percent)
    
if __name__=="__main__":
    app.run()