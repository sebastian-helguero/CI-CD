def maximo_basico(a, b):
   
    if a > b:
        return a
    return b

def test_maximo_basico():
    assert maximo_basico(1, 2) == 2
    assert maximo_basico(10, 5) == 10
    assert maximo_basico(9, 18) == 18
