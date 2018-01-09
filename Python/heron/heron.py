def heron(x):
    "Berechnet die Wurzel einer Zahl mittels Heronsche Naeherungsverfahren"
    TEILER = float(2.0)
    ABBRUCH = float(1e-7)
    w = float(0.0)
    res = float(0.0)
    diff = float(0.0)

    w = ((1.0+x)/TEILER)
    diff = x-w

    while diff > ABBRUCH:
        wOld = w
        w = (w+(x/w))/TEILER
        diff = wOld - w

        print(w)


x = int(input("Wurzel folgender Zahl berechnen (input>0!):"))

while x < 1:
    x = int(input("input groesser E I N S!!!!!"))

heron(x)

