from flask import Flask, render_template, request   ##from은 데이터를 서버로 부터 가져오는 것 

app = Flask(__name__)

@app.route("/") #web -> address=(url),Localhost:5000/
def index():
    return "Hello world"

@app.route("/second")  #Localhost:5000/second로 접속시 바로 아래 함수가 실행
def second():
    return "Second page"

@app.route("/img")
def img():
     return render_template("(6)_image.html")  ##기본 파일이 지정되어 있어서 지정만 해주면 index.html이 됨

#Localhost:5000/Login 접속(request) > Login.html을 rendering 한다. > 
@app.route("/login")
def login():
    return render_template("login.html")     

##id=test,plass=1234인 경우 로그인 성공 메세지
##아니면 로그인 실패 메세지

@app.route("/login2")
def login2():
    _id= request.args.get("id")
    _pass=request.args.get("pass")
    print(_id,_pass)
    if _id =="test" and _pass == "1234":
        return "로그인 성공"
    else:
        return "로그인 실패"