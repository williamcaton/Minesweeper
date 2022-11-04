import random
gamesize = 10
numberofmines = 15
game=1
uncovered = 0
hiddenmap = [['0' for a in range(gamesize)]for b in range(gamesize)]
for i in range(numberofmines):
    hiddenmap[random.randint(0,gamesize-1)][random.randint(0,gamesize-1)] = '#'

for x in range(gamesize):
    for y in range(gamesize):
        if hiddenmap[x][y] != '#':
            if x >= 1:
                if hiddenmap[x-1][y] == '#':
                    hiddenmap[x][y] = str(int(hiddenmap[x][y])+1)
            if x <= gamesize-2:
                if hiddenmap[x+1][y] == '#':
                    hiddenmap[x][y] = str(int(hiddenmap[x][y])+1)
            if y >= 1:
                if hiddenmap[x][y-1] == '#':
                    hiddenmap[x][y] = str(int(hiddenmap[x][y])+1)
            if y <= gamesize-2:
                if hiddenmap[x][y+1] == '#':
                    hiddenmap[x][y] = str(int(hiddenmap[x][y])+1)

for i in range(gamesize):
    print(hiddenmap[i])

visiblemap = [['-' for a in range(gamesize)]for b in range(gamesize)]

while game == 1:

    print('pick an x coordinate:')
    xcoordinate = int(input())
    print('pick a y coordinate:')
    ycoordinate = int(input())

    if hiddenmap[ycoordinate][xcoordinate] == '#':
        print('kaboom! mine explodes')
        game = 0
        visiblemap[ycoordinate][xcoordinate] = hiddenmap[ycoordinate][xcoordinate]

    if hiddenmap[ycoordinate][xcoordinate] == '0':
        if visiblemap[ycoordinate][xcoordinate] == '-':
            visiblemap[ycoordinate][xcoordinate] = '0'
            uncovered +=1
        
    for a in range(gamesize):
        for i in range(gamesize):
            for j in range(gamesize):
                if visiblemap[i][j] == '0':
                    for x in range(3):
                        for y in range(3):
                            if not((x==0 and y==0) or (x==0 and y==2) or (x==2 and y==0) or (x==2 and y==2)):
                                if ((i+x-1)>=0) and ((j+y-1)>=0) and ((i+x-1)<gamesize) and ((j+y-1)<gamesize):
                                    if (hiddenmap[i+x-1][j+y-1] != '#'):
                                        if visiblemap[i+x-1][j+y-1] == '-':
                                            visiblemap[i+x-1][j+y-1] = hiddenmap[i+x-1][j+y-1]
                                            uncovered +=1
    if uncovered >= (gamesize*gamesize)-numberofmines:
        print('you win!')
        game = 0

                    
    for i in range(gamesize):
        print(visiblemap[i])
                

