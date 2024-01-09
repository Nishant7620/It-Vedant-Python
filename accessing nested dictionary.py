nested_di = {"a":1,"b":2,"c":3,"d":4,"e":{"peter":"spiderman","tony":"ironman"}}

for i in nested_di:
    if type(nested_di[i]) is dict:
        for j in nested_di[i]:
            print(j,nested_di[i][j])

    else :
        print(i,nested_di[i])        