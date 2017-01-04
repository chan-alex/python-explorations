#!env python3

# Utilize python special methods to make your data and object play well with the
# rest of python.

import collections


MahjongTile = collections.namedtuple('MahjongTile', [ 'group', 'tile' ])


class MahjongTiles:
    suits = [ 'dots', 'bamboo', 'characters']
    winds = [ 'north', 'south', ' east', 'west']
    dragons = ['center', 'blank', 'fortune']
    seasons = ['spring', 'summer', 'autumn', 'winter']
    flowers = [ 'plum', 'orchid', 'chrysanthemum', 'bamboo' ]
    
    
    def __init__(self):
        
        all_suits = [ d for group in self.suits
                             for tile in range(1, 10)
                             for d in [MahjongTile( group, tile)] * 4 ]

        all_winds   = [ t for tile in self.winds for t in [MahjongTile('winds', tile)]*4 ]
        all_dragons = [ d for tile in self.dragons for d in [MahjongTile('dragon', tile)]*4 ] 
        all_seasons = [ MahjongTile('seasons', tile) for tile in self.seasons ]
        all_flowers = [ MahjongTile('flowers', tile) for tile in self.flowers ]        

        
        self._tiles = all_suits + all_winds  + all_dragons  \
                     + all_seasons + all_flowers


    def __len__(self):
        return len(self._tiles)
            
        
    def __getitem__(self, position):
        return self._tiles[position]
             


if __name__ == '__main__':


    mt = MahjongTiles()
    
    # Defining the __len__() specical method, allows len() to be called on MahjongTiles.      
    length = len(mt)
    print("len(mt) returns %s" % length)


    # Defining __getitems__(), allows the elements to be access via index
    t = mt[100]
    print("The 100th element is %s" % str(t))

    # With the above special methods, it is easy to make use of the standard python
    # libraries and modules on it.

    # Picking a ranndom tile.:
    
    # >>> from random import choice
    # >>> choice(mt)
    # MahjongTile(group='dots', tile=8)
    # >>> choice(mt)
    # MahjongTile(group='dragon', tile='blank')


    # Slicing is possible because of __getitem__()
    # >>> mt[50:55]
    # [MahjongTile(group='bamboo', tile=4), MahjongTile(group='bamboo', tile=4), MahjongTile(group='b   # amboo', tile=5), MahjongTile(group='bamboo', tile=5), MahjongTile(group='bamboo', tile=5)]

    # Because of __getitems__(), it is possible to iterable over the tiles
    for t in mt:
        print(str(t))

    #Also easy to iterate in reverse
    for t in reversed(mt):
        print(str(t))


    # The "in" operator will work too because of __getitems__() if inefficient.
    # It will use sequence scanning.

    if MahjongTile('bamboo', 1) in mt:
        print("Yes , bamboo 1 is there.")
