#!/usr/bin/env python3
#
#
# date:     Sun 15 Oct 2017 02:16:26 PM CEST
#
# descr:    Praktikum Programmieren 1 - Aufgabenblatt 2

import math





# Aufgabe 2.0

# A
# Implementieren Sie einen Konstruktor, der Name, Vorname, Alter
# und Größe einer Person erhält und eine Instanz der Klasse Person erzeugt.

#class Person:
#
#
#    def __init__(self, name, vorname, alter,gros):
#        self.name = name
#        self.vorname = vorname
#        self.alter = alter
#        self.gros = gros
#        self.aelterCount = 0
#        self.freundListe = []
#
#    def werdeAelter(self):
#        self.aelterCount += 1
#        self.alter += 1
#
#        if self.aelterCount == 10:
#            self.gros -= 1
#            self.aelterCount = 0
#
#
#    def isBaby(self):
#        if self.alter in [0,1]:
#            print(self.vorname, 'ist noch ein Baby')
#            return True
#
#        print(self.vorname, 'ist kein Baby')
#        return False
#
#
#
#    def neuerFreund(self,x):
#        self.freundListe.append(x)
#
#
#    # return list of friend names
#    def freunde(self):
#        freundNamen = []
#        for x in self.freundListe:
#            freundNamen += [x.vorname]
#        return freundNamen
#
#
#
#    def aelteserFreund(self):
#        alterFreund = []
#        for x in self.freundListe:
#            alterFreund.append((x.alter, x.name))
#        return max(alterFreund, key=lambda item: item[0])
#
#def main():
#
#
#
#
#    # A
#    hans = Person('muller','hans',53,182)
#    elias = Person('muller','elias',1 ,82)
#
#    # B
#    for i in range(25):
#        hans.werdeAelter()
#        if i % 5 == 0:
#            print(hans.alter)
#            print(hans.gros)
#
#   # C
#    hans.isBaby()
#    elias.isBaby()
#
#
#    hans.neuerFreund(Person('reimus','kamil',35,188))
#    hans.neuerFreund(Person('müller','johannes',42,182))
#    hans.neuerFreund(Person('potter','harry',72,160))
#    hans.neuerFreund(Person('stanis','baratheon',72,160))
#
#
#    print(hans.aelteserFreund())
#
#main() # Aufgabe 2.0 started at line: 20 """m0"""


# Aufgabe 2.1
#
# TO-DO:    Getter Setter
#           Verwaltung erleichtern. Bswp. update von ects eines Studentens

#class Person:
#
#    def __init__(self,vorname,nachname,alter,geburtstag):
#        self.vorname = vorname
#        self.nachname = nachname
#        self.alter = alter
#        self.geburtstag = geburtstag
#
#
#class Student(Person):
#
#    def __init__(self,matr,semester,ects):
#        super().__init__()
#        self.matrikelnummer = matr
#        self.semester = semester
#        self.ects = ects
#
#class Professor(Person):
#
#    def __init__(self,vorname,nachname,alter,geburtstag,berufung):
#        super().__init__(vorname,nachname,alter,geburtstag)
#        self.berufungsgebiet = berufung
#
#class Uni:
#
#    def __init__(self, name, ort):
#        self.name = name
#        self.ort = ort
#        self.studiganList = []
#
#
#    def addStudigang(self,x):
#        self.studiganList.append(x)
#
#class Studiengang:
#
#    def __init__(self, studname,typ):
#        self.studname = studname
#        self.typ = typ
#        self.profList = []
#
#    def addProf(self,x):
#        self.profList.append(x)
#
#
#
#
#
#
#def main():
#
#    # create a university
#    hs_albsig = Uni('Hochshule Albstadt Sigmaringen','Albstadt-Ebingen')
#
#    # create some courses
#    hs_albsig.addStudigang(Studiengang('WIN','BA'))
#    hs_albsig.addStudigang(Studiengang('ITSec','BA'))
#
#    # print(hs_albsig.studiganList[0].studname) # WIN
#
#    # create some professors too
#    haberlein = Professor('Tobias','Haeberlein',40,'13-11-1994',
#                          'Algorithmik')
#
#    hs_albsig.studiganList[0].addProf(haberlein)
#    print(hs_albsig.studiganList[0].profList[0].nachname) # Haeberlein
#
#main() # Aufgabe 2.1 started at line: 101 """m1"""


# Aufgabe 2.2 +2.3
# https://stackoverflow.com/questions/12486828/python-making-a-class-to-use-complex-numbers

#class Complex():
#
#    def __init__(self, a, b):
#        '''Creates Complex Number'''
#        self.a = a
#        self.b = b
#
#    def __str__(self):
#        '''Returns complex number as a string'''
#        return '{} + {}i'.format(self.a, self.b)
#
#    def __add__(self, rhs):
#        '''Adds complex numbers'''
#        return Complex(self.a + rhs.a, self.b + rhs.b)
#
#    def __mul__(self, rhs):
#        '''multiplies complex numbers'''
#        return Complex(self.a * rhs.a, self.b * rhs.b)
#
#def main():
#    x1 = Complex(1.0, 2.0)
#    x2 = Complex(2, 3)
#    x3 = x1.__add__(x2)
#
#
#
#    print(x1+x2)
#main() # Aufgabe 2.2-3 started at line: 179 """m2"""

# Aufgabe 2.4
#class Stack:
#    def __init__(self):
#        self.items = []
#
#    def isEmpty(self):
#        return self.items == []
#
#    def push(self, item):
#        self.items.append(item)
#
#    def pop(self):
#        return self.items.pop()
#
#    def __len__(self):
#        return len(self.items)
#
#    def toList(self):
#         return self.items
#
#    def multPop(self, n):
#        for i in range(n):
#            self.pop()
#            self.toList()
#
#def main():
#
#    s = Stack()
#    s.push(1) ; s.push("HallO") ; s.push(4.32) ; s.push(True)
#
#    print(len(s))           #   4
#    print(s.toList())       #   returns list of elements
#
#    s.multPop(2)            #   run multPop n times
#    print(s.toList())       #   check if multPop worked as intended
#
#main() # Aufgabe 2.4 started at line: 208 """m3"""



##########################
#
#    Aufgabe 2.5
#
#   To-Do: Implement a dictionary to store the values
##########################


#class AufgabenManager:
#
#    def __init__(self):
#        self.aufgaben = {}
#        self.urgentJobs = {}
#
#    def neueAufgabe(self,job,priority):
#        if type(job) != str:
#            print("First argument of kind {}, expected string".format(type(job)))
#        elif type(priority) != int:
#            print("Second argument of kind {}, expected integer".format(type(priority)))
#        else:
#            self.aufgaben[job] = priority
#
#    def hoechstePrio(self):
#        highestPrio = min(self.aufgaben.values())
#        for key, value in self.aufgaben.items():
#            if value == highestPrio:
#                self.urgentJobs[key] = value
#        return self.urgentJobs
#
#
#    def erledigeNaechsteAufgabe(self):
#        self.hoechstePrio()
#        lastUrgentKey = list(self.urgentJobs)[-1]
#        self.aufgaben.pop(lastUrgentKey, None)
#        return self.aufgaben
#
#    def alleAufgabenMitPrio(self,v):
#        aufgabenListe = []
#        for a in list(self.aufgaben.items()):
#            if a[1] == v:
#                aufgabenListe += [a[0]]
#        return aufgabenListe
#
#
#    def allePrios(self):
#        prioList = []
#        for a in list(self.aufgaben.items()):
#            prioList += [a[1]]
#        return sorted(set(prioList))
#
#
#    def anzahlAufgabenPrio(self,prio):
#        return len(self.alleAufgabenMitPrio(prio))
#
#    def anzahlAufgaben(self):
#        return len(list(self.info()))
#
#
#    def info(self):
#        return self.aufgaben
#
#def main():
#
#    manageR = AufgabenManager()
#
#    # create jobs
#    # manageR.neueAufgabe(5, 2) # this attempt will fail due to wrong argument
#    manageR.neueAufgabe('do the laundry', 2)
#    manageR.neueAufgabe('make food', 3)
#    manageR.neueAufgabe('read a book', 3)
#    manageR.neueAufgabe('play dota2', 1)
#    manageR.neueAufgabe('buy some croceries', 4)
#
#    # print(manageR.hoechstePrio())
#    # print('These are all your current jobs.\n',manageR.info())
#    # print(manageR.erledigeNaechsteAufgabe())
#    # print(manageR.alleAufgabenMitPrio(3))
#    # print(manageR.allePrios())
#
#    print(manageR.anzahlAufgaben())
#
#main() # started at line: 256 "m4"



########################
#
#    Aufgabe 2.7
#
#########################


class Cntr:

    def __init__(self,seq):
        self.seq = seq

    def __str__(self):
        someSeq = []
        noDuplicates = []
        theString = ""

        for i in self.seq:
            if i not in noDuplicates:
                someSeq.append("{} --> {}\n".format(i,
                                              list(self.seq).count(i)))
                noDuplicates.append(i)

        for x in someSeq:
            theString += x
        return theString

    def __add__(self, rhs):
        return Cntr(self.seq + rhs.seq)


    def most(self):
        return max(self.seq, key=self.seq.count)


def main():
    c = Cntr("Hello welt hello")
    d = Cntr("llloooX")

    print(c+d)

main()







