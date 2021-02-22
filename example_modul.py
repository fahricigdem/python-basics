def add (*numbers):
    ergebnis=0
    for i in numbers:
        ergebnis+=i
    return ergebnis

def multi (*numbers):
    ergebnis=1
    for i in numbers:
            
        ergebnis *=i
        print(i)
    return ergebnis
