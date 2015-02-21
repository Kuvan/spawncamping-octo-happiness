import json

class brains:
	def start(self, data):
		self.mInfo = json.load[data]
		self.mWidth = self.mInfo["width"]
		self.mHeight = self.mInfo["height"]
		self.mGameID = self.mInfo["game_id"]
		#print(self.mGameID)
		self.Board[self.mWidth,self.mHeight]
		
	def move(self):
		return json.dumps({
        	'move': 'right',
        	'taunt': 'battlesnake-python!'
    	})
	
