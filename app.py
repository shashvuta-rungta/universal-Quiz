from flask import Flask,render_template,request
app=Flask(__name__)
#flask is a micro framework
@app.route("/")
def home():
    return " Shashvuta"
@app.route('/name')
def name():
    return render_template("hello.html")

@app.route('/string')
def string():
    return render_template("hello.html")

@app.route('/reverse')
def reverse():
    str1=request.args.get("string")
    rev_str=""
    for i in str1 :
        rev_str=i+rev_str
    return render_template("hello.html",rev_str=rev_str)

@app.route('/getq1')
def getq1():
     return render_template("q1.html")
    
@app.route('/q1')
def q1():
     option=request.args.get("choice") 
     message=""  
     if option=="A":
         message="correct"
     else:
         message="wrong" 
     return render_template("q1.html",message=message)

@app.route('/getq2')
def getq2():                                     
    return render_template("q2.html")
    
@app.route('/q2')
def q2():
     option=request.args.get("choice")
     print (option) 
     message=""  
     if option=="D":
         message="correct"
     else:
         message="wrong" 
     return render_template("q2.html",message=message) 

@app.route('/getq3')
def getq3():                                     
    return render_template("q3.html")     

@app.route('/q3')
def q3():
     option=request.args.get("choice")
     print (option) 
     message=""  
     if option=="C":
         message="correct"
     else:
         message="wrong" 
     return render_template("q3.html",message=message)

@app.route('/getq4')
def getq4():                                     
    return render_template("q4.html")     

@app.route('/q4')
def q4():
     option=request.args.get("choice")
     print (option) 
     message=""  
     if option=="B":
         message="Correct"
     else:
         message="Wrong" 
     return render_template("q4.html",message=message)  

@app.route('/login')
def login():
   return render_template("registration.html")

@app.route('/validateuser')
def validateuser():
    users={"user1":1234,"user2":4321,"user3":0000}
    username=request.args.get("username")
    password=request.args.get("password",type=int)
    getuser=users.get(username)
    message=''
    if getuser==password:
        message="logged in succesfully" 
    else:
        message="incorrect credentials"
    return render_template("registration.html",message=message)


if __name__=="__main__":
    app.run(debug=True)

