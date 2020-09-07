def game(X, Y):
    if X >= 10 and Y==1:
        X=1
        return X
    elif (X-Y) <= 2:
        X = 2
        return X
    if Y > 10:
        X = 3
    return X
