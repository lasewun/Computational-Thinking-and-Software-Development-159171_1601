#Tutorial 7 Part 3

mispellings= """abberration:aberration
accomodation:accommodation
acheive:achieve
adress:address
alot:a lot
alterior:ulterior
athiest:atheist
beggining:beginning
beleive:believe
Caucasion:Caucasian
cemetary:cemetery
committment:commitment
concieve:conceive
copywrite:copyright
Dalmation:Dalmatian
decaffinated:decaffeinated
decathalon:decathlon
definately:definitely
dependance:dependence
dessicate:desiccate
desireable:desirable
diarhea:diarrhoea
dissapoint:disappoint
dispell:dispel
embarass:embarrass
enviroment:environment
expresso:espresso
facist:fascist
Febuary:February
fivety:fifty
fluoroscent:fluorescent
flouride:fluoride
forteen:fourteen
fourty:forty
freind:friend
geneology:genealogy
goverment:government
grammer:grammar
hampster:hamster
harrass:harass
hemorage:haemorrhage
heros:heroes
hight:height
hygeine:hygiene
hypocracy:hypocricy
independance:independence
inate:innate
innoculate:inoculate
intresting:interesting
juge:judge
knowlege:knowledge
lazer:laser
libary:library
lightening:lightning
managable:manageable
millenium:millennium
mischievious:mischievous
mispell:misspell
missle:missile
monestary:monastery
monkies:monkeys
morgage:mortgage
mountian:mountain
neccessary:necessary
neice:niece
nickle:nickel
nineth:ninth
ninty:ninety
noone:no one
noticable:noticeable
occured:occurred
occurence:occurrence
oppurtunity:opportunity
opthamologist:ophthalmologist
paralell:parallel
pasttime:pastime
pavillion:pavilion
peice:piece
percieve:perceive
perserverance:perseverance
persue:pursue
posession:possession
potatoe:potato
preceeding:preceding
pronounciation:pronunciation
privelige:privilege
publically:publicly
quew:queue
rasberry:raspberry
recieve:receive
reccomend:recommend
rediculous:ridiculous
reguardless:regardless
rythm:rhythm
shedule:schedule
seige:siege
sentance:sentence
seperate:separate
sieze:seize
sincerly:sincerely
speach:speech
stragedy:strategy
supercede:supersede
suprise:surprise
thier:their
tommorrow:tomorrow
tounge:tongue
uneform:uniform
vaccuum:vacuum
vegeterian:vegetarian
Wendesday:Wednesday
wierd:weird
writen:written
writting:writing"""
def listFunct():
    origList = mispellings.split('\n')
    print(origList)
    correctionList =[]
    for l in origList:
        correctionList.append(l.split(':'))
    print(correctionList)
    return correctionList


def checkWord(word, correctionList):
    for (wrong, correct) in correctionList:
        if word.lower() == wrong:
            return correct
        elif word.lower() == correct:
            return correct
    if word != correct:
        return word

def main(correctionList):
    # word = input('test input')
    # correct_word = checkword(word, correctionList)
    # print(correct_word)

    sentence = input('Please enter sentence here to be processed')
    correctSentence = []
    sentenceWord = sentence.split()
    for word in sentenceWord:
        correct_word = checkWord(word, correctionList)
        correctSentence.append(correct_word)
    print(" ".join(correctSentence))


correctionList = listFunct()
main(correctionList)
