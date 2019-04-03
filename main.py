from flask import Flask, request
from caesar import rot

app = Flask(__name__)


form = '''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rot">ROTATE BY</label>
                <input id="rot" type="text"/>
                <textarea id="textToRot"></textarea>
                <input type="submit" value="submit"/>
            </form>
        </body>
    </html>
'''

@app.route('/')
def index():
    return form

@app.route('/encrypt', methods=['POST'])
def encrypt(val, text):
    data = rot(val, text)
    return form                   #<----------left off here



if __name__ == '__main__':
    app.run(debug=True)