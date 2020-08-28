# In Movie X+Y, Nathan was given a problem like : 20 random cards are placed in a row, all face down. Move consists of turning a face down card, face up and turning over the card immediately to the right. Show that no matter what the choice of cards to turn, this sequence of moves must terminate.
# (with all the cards facing up).

def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else: 
                b[i+1] = '0'
        
    return b


a = list("11111111111111111111")  
# These 20 cards were given to Nathan.Face Down represented by 1... And face Up represented by 0...
print(a)
while a != transform(a.copy()):
    a = transform(a.copy())
print(a)