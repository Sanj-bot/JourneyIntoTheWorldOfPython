from flask import Flask
app=Flask(__name__)

#  using decorators to make different pages.
# decorators help in adding additional functionalites.
@app.route("/") # forward slash is the root page.
@app.route("/home")
def home():
    return "<h1>Home Page<h1>"

@app.route("/about") # forward slash is the root page.
def about():
    return "<h1> About Page<h1>"

if __name__=='__main__':
    app.run(debug=True)