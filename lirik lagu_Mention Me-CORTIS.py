import time
import sys

lirik = [("Ain't got benefits, I made it by myself straight from the jump", 0.03, 0.9),
("Ain't got benefits, I came up with the crew, and made the cut", 0.03, 0.9),
("Nobody mess with me, yeah, uh.", 0.06, 0.9),
("Nobody mess with me, and matter of fact 'cause I be cleanin' it up, phew.", 0.04, 0.9),
("I can't be a stranger, like, Who's in the mirror?", 0.04, 2),
("Top class, ballin', ready sold out big arena (Yee, yee)", 0.03, 1),
("They call me legit, but I've been killing like misdemeanors", 0.04, 1.2),
("And I pull up in food coma, shame you missed me eat up", 0.03, 1),
("So I'm back, I pulled up way faster than a Bimmer (Yeah)", 0.03, 2),
("Only first place 'cause I'm a leader (Yeah)", 0.03, 2),
("Only top class, I might need a (Oh, yeah)", 0.03, 2),
("Little more space next time we meet up", 0.03, 1)]

def lagu_berjalan():
    for kalimat, speed_huruf, jeda_baris in lirik:
        for huruf in kalimat:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(speed_huruf)
        print()
        time.sleep(jeda_baris)

lagu_berjalan()
