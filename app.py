from flask import Flask,render_template,request,session,redirect
#Flask is a micro framework

app=Flask(__name__)
app.config["SECRET_KEY"]="1234"

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/validate_register',methods=['POST'])
def validate_register():
    username=request.form.get('username')
    email=request.form.get('password')
    password=request.form.get('password')
    confirm_password=request.form.get('confirm_password')
    message=''
    if password==confirm_password:
        print('Registration Successful')
        message='Registration Successful'
        session['username']=username
        session['authenticated']=True
        session['email'] =email
        return render_template('login.html',message=message)
    else:
        print('Password mismatch')
        message='password mismatch'
        return render_template('register.html',message=message)

@app.route('/login_page')
def login_page():
   return render_template("login.html")

@app.route('/validate_user',methods=['POST'])
def validate_user():
    users={"User_1":1234,"User_2":4321,"User_3":0000}
    user_name=request.form.get("username")
    password=request.form.get("password")
    print(password)
    session['password']=password
    get_user=users.get(user_name)
    message=""
    session_un=session.get('username')
    print(session_un)
    session_pwd=session.get('password')
    print(session_pwd)
    session_email=session.get('email')
    print(session_email)
    if session_un==user_name or session_email==user_name :
        if (session_pwd)==password :
            message="You have succesfully logged in!!!😃"
            session['username']=user_name
            session['authenticated'] =True
            return render_template('q1.html',message=message,score=0)
        else:
            message='Incorrect Password'
            session['authenticated'] =False
            return render_template('login.html',message=message)
    else:
        message='incorrect Username'
        message="You have failed to login!!!😔"
        return render_template('login_page.html',message=message)

@app.route('/riddle_1')
def riddle_1():
   return render_template("riddle_1.html",riddles=riddles)


@app.route('/r1')
def r1():
   pass

riddles=[{
    "Author":"Divvya",
    "Title":"Riddle_1",
    "Content":"What can fill a room but takes up no space?",
    "Date_Posted":"8th June 2021"
},
{
    "Author":"Divvya",
    "Title":"Riddle_2",
    "Content":"What can fill a room but takes up no space?",
    "Date_Posted":"8th June 2021"
}]



# -------Validating Quiz---Important Function---------------------
def validatequiz(correct_answer):
    option=request.form.get("choice")
    message=""
    score=session.get("user_score",0)   
    if option==correct_answer:
        message="Excellent, You are Right!!"
        score=score+20
    else:
        message="Nice try,The right answer is B"
    session["user_score"]=score
    return message


#--------------------Quiz-------------------------------------------


#--------------------Q!-------------------------------------------

@app.route('/get_q1')
def get_q1():
    session['user_score']=0
    score=session.get('user_score',0)
    return render_template("q1.html",score=score)
    
@app.route('/q1',methods=['POST'])
def Q1():
   message = validatequiz('B')
   score=session.get("user_score",0)
   return render_template("q2.html",message=message,score=score)

#--------------------Q2-------------------------------------------

@app.route('/get_q2')
def get_q2():
      return render_template("q2.html")

@app.route('/q2',methods=['POST'])
def q2():
    message = validatequiz('B')
    score=session.get("user_score",0)
    return render_template("q3.html",message=message,score=score)

#--------------------Q3-------------------------------------------

@app.route('/get_q3')
def get_q3():
      return render_template("q3.html")

@app.route('/q3',methods=['POST'])
def q3():
    message = validatequiz('B')
    score=session.get("user_score",0)
    return render_template("q4.html",message=message,score=score)

#--------------------Q4-------------------------------------------

@app.route('/get_q4')
def get_q4():
      return render_template("q4.html")

@app.route('/q4',methods=['POST'])
def q4():
    message = validatequiz('A')
    score=session.get("user_score",0)
    return render_template("q5.html",message=message,score=score)

#--------------------Q5-------------------------------------------

@app.route('/get_q5')
def get_q5():
      return render_template("q5.html")

@app.route('/q5',methods=['POST'])
def q5():
    message = validatequiz('D')
    score=session.get("user_score",0)
    return render_template("q6.html",message=message,score=score)

@app.route('/q6',methods=['POST'])
def q6():
    message = validatequiz('D')
    score=session.get("user_score",0)
    return render_template("q7.html",message=message,score=score)

@app.route('/q7',methods=['POST'])
def q7():
    message = validatequiz('D')
    score=session.get("user_score",0)
    return render_template("q8.html",message=message,score=score)

@app.route('/q8',methods=['POST'])
def q8():
    message = validatequiz('D')
    score=session.get("user_score",0)
    return render_template("q9.html",message=message,score=score)

@app.route('/q9',methods=['POST'])
def q9():
    message = validatequiz('D')
    score=session.get("user_score",0)
    return render_template("home.html",message=message,score=score,info='Your Final Score is ')
    
if __name__=="__main__":
    app.run(debug=True)