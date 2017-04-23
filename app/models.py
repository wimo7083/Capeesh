from app import db




class User(db.Model):

    UID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index = True)
    current_level = db.Column(db.Integer, index = True)
    initial_level = db.Column(db.Integer, index = True)
    first_success = db.Column(db.Integer, index = True) 
    
    
    def __repr__(self):
        return '<User %r>' % (self.name)
  
class Level_attempt(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    two = db.Column(db.Integer, index = True)     
    three = db.Column(db.Integer, index = True)
    four = db.Column(db.Integer, index = True)
    five = db.Column(db.Integer, index = True)
    six = db.Column(db.Integer, index = True)
    seven = db.Column(db.Integer, index = True)
    eight = db.Column(db.Integer, index = True)
    nine = db.Column(db.Integer, index = True)
    
    def __repr__(self, level_num):    
        return '<Level_attempt %r>' % (self.level_num)
        
        
       
class Level_mistake(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    two = db.Column(db.Integer, index = True)     
    three = db.Column(db.Integer, index = True)
    four = db.Column(db.Integer, index = True)
    five = db.Column(db.Integer, index = True)
    six = db.Column(db.Integer, index = True)
    seven = db.Column(db.Integer, index = True)
    eight = db.Column(db.Integer, index = True)
    nine = db.Column(db.Integer, index = True)
    
    def __repr__(self, level_num):    
        return '<Level_attempt %r>' % (self.level_num)
        
        
     
    
class two(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
        
class three(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)

class four(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
class five(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
class six(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
class seven(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
class eight(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
        
class nine(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    
    
    def __repr__(self):
        return '<Word %r>' % (self.word)
   