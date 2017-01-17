from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
        Hi! This is the home page.<br>
        <a href="/hello">Introduce yourself</a>
      <html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <div>
            Choose a compliment
              <select name="compliment">
                <option value="awesome">Awesome</option>
                <option value="terrific">Terrific</option>
                <option value="fantastic">Fantastic</option>
                <option value="neato">Neato</option>
                <option value="fantabulous">Fantabulous</option>
                <option value="smashing">Smashing</option>
              </select>
          </div>
          <input type="submit">
        </form>
        <br><br>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <div>
            Choose a diss
              <select name="diss">
                <option>mean</option>
                <option>meh</option>
                <option>okay at best</option>
                <option>fine I guess</option>
              </select>
          </div>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name and diss."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>Get Wrecked</title>
      </head>
      <body>
        Hi %s I think you're %s.
      </body>
    </html>
    """ % (player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
