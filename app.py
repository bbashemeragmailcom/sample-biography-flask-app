from flask import Flask, request, render_template,redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def base():
    return render_template("index.html")   

@app.route('/project', methods=['GET', 'POST'])
def project():
    #if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('project.html')

@app.route('/terms', methods=['GET', 'POST'])
def terms():
    #if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('terms.html')

@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    #if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('privacy.html')

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()