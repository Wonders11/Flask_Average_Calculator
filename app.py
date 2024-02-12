## Creating a simple flask application

# from flask import Flask,redirect,url_for 
# redirect will redirect us to url

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app = Flask(__name__) 

# for creating different webpages like home,profile,etc we use decorator
# whenever I hit this / it will call home func
@app.route('/') # here we give what should be the link. Example: google.com/home
def home():
    return "<h1> Hello World!! </h1>"
    # in place of returning this messages we can return complete webpage using redirect and url_for class from flask library

@app.route('/welcome')
def welcome():
    return "Welcome to the flask tutorial...."

@app.route('/index')
def index():
    return render_template('index.html') # here we will return webpage index.html created inside templates folder

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and score is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and score is " + str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method == 'GET': # get is w.r.t webpage i.e get data from webpage 
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3
        result=""

        if average_marks>=50:
            result="success"
        else:
            result="fail"

        return render_template('result.html',results = average_marks)
        #return redirect(url_for(result,score=average_marks))#if we want to redirect to page in above mentioned urls we will use redirect
        # return render_template('result.html',results=average_marks) # results variable will be used in result.html page
        # return render_template('calculate.html',results=average_marks)
    

       ## Try for loop - Assignment
       # Create dictionary here and and return dict in results.html and use for loop

if __name__=='__main__':
    app.run(debug=True, port=5001) # use debug only during development and not during deployment
    # with port 5000 it was not working so change port to 5001 and it started working