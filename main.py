from flask import Flask, request
from caesar import rot

app = Flask(__name__)

#html form as a string var
form = '''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form, header {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                header {{
                    text-align: center;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <header>
                <h2>Web-Caesar</h2>
                <p>John Durham kilo.kilo.delta8@gmail.com</p>
                <small>LaunchCode Memphis 2019</small>
            </header>
            <form action="/encrypt" method="POST">
                <label for="rotBy">ROTATE BY</label>
                <input type="text" name="rotBy" value="0" />
                <textarea name="textToRot">{}</textarea>
                <input type="submit" value="submit" />
            </form>
        </body>
    </html>
'''


#index route, returning html form var
@app.route('/')
def index():
    return form.format('')


#encrypt method
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    val = request.form.get('rotBy')
    if val == None:
        val = int(13)
    data = request.form.get('textToRot')
    retData = rot(data, val)
    return form.format(retData)        



if __name__ == '__main__':
    app.run(debug=True) #<-------turn on/off debug mode here