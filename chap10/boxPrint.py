def spam():
    bacon()
def bacon():
    raise Exception('thisnotgood')

spam()
