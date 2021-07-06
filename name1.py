from flask import Flask
name1=Flask(__name__)
@name1.route("/")
def prerna():
    return "Hello World"
if __name__=="__main__":
    name1.run()