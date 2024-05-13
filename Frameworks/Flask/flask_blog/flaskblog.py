from flask import Flask
app=Flask(__name__)

#  using decorators to make different pages.
# decorators help in adding additional functionalites.
@app.route("/") # forward slash is the root page.
def hello():
    return "Hello World!"