class MyStuff(object):
    
        def __init__(self): #this is called whenever you initialize an empty object.
            self.tangerine = "And now theres a tangerine."
            
        def apple(self):
            print "I AM CLASSY APPlES!"
        
        
thing = MyStuff() #this is our newly created object
thing.apple() #this is method on line 6
print thing.tangerine #this is a statement on line 4



##if we were using modules we would use these lines
#
#mystuff.apples()
#print mystuff.tangerine

##if we were using dictionary methods. we would use these.
#mystuff['apples']

