## player name, score
# Mary Please, 72
# Max Walker, 64
# Col Klomp, 78
# Belle McKay, 67

import lxml.etree
import lxml.builder
import io

E = lxml.builder.ElementMaker()
COMPETITION = E.root
PLAYER = E.competition
GIVEN = E.givenName
LAST = E.lastName
SCORE = E.score

the_doc = COMPETITION(
    PLAYER(
        GIVEN("Mary"),
        LAST("Lamb"),
        SCORE("72")
    ),
    PLAYER(
        GIVEN("Eileen"),
        LAST("Dover"),
        SCORE("64")
    ),
    PLAYER(
        GIVEN("Robin"),
        LAST("Banks"),
        SCORE("78")
    ),
    PLAYER(
        GIVEN("Jacques"),
        LAST("d'Carre"),
        SCORE("67")
    )
)

print(the_doc)
#with open('Golf-000.xml', 'w') as f:
    #f.write(the_doc)
