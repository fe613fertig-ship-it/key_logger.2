from flask import Flask,request
app = Flask(__name__)

messages = []
@app.route('/')
def home():
    return '''
    <h1>keylogger center</h1>
    <form method="POST" action="/user">
        <input type="text" name="user" placeholder="enter your name">
        <button type="submit">send</button>
    </form>
    <h2> user exist:</h2>
    ''' + '<br>'.join( messages )

@app.route('/user', methods=['POST'])
def start_logging():
    return '''
    <style>body{background-color:black;} h1{color:green;}</style>
    <h1>Logging started</h1>'''

@app.route('/stop', methods=['POST'])
def stop_logging():
    return 'Logging stopped'

@app.route('/keys', methods=['GET'])
def get_logged_keys():
    return 'List of logged keys'


if __name__ == '__main__':
    app.run(debug=True)