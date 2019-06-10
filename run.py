from flask import Flask,render_template,request,redirect

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    # print(request.headers)
    if 'Referer' in request.headers:
        print('Referer',request.headers['Referer'])
    return render_template("index.html")


@app.route("/list")
def list_view():
    # print('Referer',request.headers)
    if 'Referer' in request.headers:
        print('Referer',request.headers['Referer'])
    return render_template("list.html")


@app.route("/parent")
def parent():
    return render_template("parent.html")


@app.route("/child")
def child():
    return render_template("child.html")

@app.route("/request")
def request_view():
    print(dir(request))
    print(request.args["uname"])
    return render_template("child.html",request=request)

@app.route('/get',methods=['GET','POST'])
def show():
    if request.method=='GET':
        print(request.args.get('uname','xxx'))
        print(request.args.get('upwd',123))
        print(request.args.getlist('hobby'))
        # 重定向
        # res=redirect('/')
        # print(res)
        return render_template("get.html")
    else:
        print(request.form)
        print(request.form.get('uname','xxx'))
        print(request.form.get("upwd",123))
        print(request.files)
    # return render_template("get.html")
        return render_template("get.html")

@app.route("/form")
def form_view():
    return render_template("get.html")


if __name__ == '__main__':
    app.run(debug=True)
