import bottle
import os
import random
import json


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#0087ff',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'battlesnake-python'
    }


@bottle.post('/move')
def move():
	directions = ['up', 'down', 'left', 'right']
	
    data = bottle.request.json
	
	my_x = data["you"]["body"]["data"][0].x
	my_y = data["you"]["body"]["data"][0].y
	my_x_neck = data["you"]["body"]["data"][1].x
	my_y_neck = data["you"]["body"]["data"][1].y
	my_x_tail = data["you"]["body"]["data"][-1].x
	my_y_tail = data["you"]["body"]["data"][-1].y
	
	if my_x <= 0:
		directions.remove('left') #NOT LEFT
		
	elif my_x >= board_width-1:
		directions.remove('right') #NOT RIGHT
		
	elif my_y <= 0:
		directions.remove('down') #NOT DOWN
		
	elif my_y >= board_height-1:
		directions.remove('up') #NOT UP
		
	elif my_x > my_x_tail && my_y == my_y_tail:
		
	
    # TODO: Do things with data

    return {
        'move': random.choice(directions),
        'taunt': 'These guys are weaker than overcooked noodles!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
