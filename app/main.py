import bottle
import json
import routing

smart = brains()

@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json
    smart.start(data)
	
    return json.dumps({
        'name': 'battlesnake-python',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    return smart.move()


@bottle.post('/end')
def end():
    data = bottle.request.json
	
    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
