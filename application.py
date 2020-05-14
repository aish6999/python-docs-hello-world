from flask import Flask
app = Flask(__name__)

@app.route("/poc")
def hello():
    return "<h3>Subdomain Takeover by <a href="https://twitter.com/saurabhsanmane2">Saurabh Sanmane</a> & <a href="https://www.linkedin.com/in/aishwarya-kendle/" >Aishwarya Kendle"</a>
