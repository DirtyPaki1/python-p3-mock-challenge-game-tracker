class Game:
    def __init__(self, title):
        self.title = title  
        # self.results = []  
        # self.players = set()
       

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if(isinstance(title,str) and not hasattr(self,"title")):
            self._title = title
        else:
            raise Exception()    
        
        


   
    def results(self):
       return [result for result in Result.all if result.game == self]


  
    def players(self):
           return list({result.player for result in Result.all if result.game == self })
        

    def add_result(self, result):
        if not isinstance(result, Result):
            raise ValueError("Results must be instances of Result class")
        self._results.append(result)

    def add_player(self, player):
        if not isinstance(player, Player):
            raise ValueError("Players must be instances of Player class")
        self._players.add(player)

    def average_score(self, player):
     if not isinstance(player,Player): 
        return None
     total_score = sum([result.score for result in self.results() if result.player == player])
     return total_score / len(self.results()) if self.results() else 0


class Player:
    def __init__(self, username):
         
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        if len(username) < 2 or len(username) > 16:
            raise ValueError("Username must be between 2 and 16 characters long")
        self._username = username
        self._games_played = set()  

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if(isinstance(username,str)and 2<=len(username)<=16):
            self._username = username
          
        
    def games_played(self):
       return list({result.game for result in Result.all if result.player == self})


   

    def played_game(self, game):
        if game in self.games_played():
            return True
        else: 
            return False

    def results(self):
        return  [result for result in Result.all if result.player == self]


    def num_times_played(self, game):
        match_games = []
        games_played = [result.game for result in self.results()]
        # Check if the game is in the dictionary of games played
        if game in games_played:

            
            
            for  games in games_played:
                if (game == games):
                    match_games.append(games)
            return len(match_games)
                    


            
        else:
           
            return 0

           

class Result:
    all = []  

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self) 

   
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if(isinstance(score,int) and not hasattr(self, 'score') and 1<=score and score<=5000):
            self._score = score

        

  
    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

 


myarray=[1,2,2,3,4]
array = len(myarray)
print(array)