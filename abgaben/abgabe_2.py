#!/usr/bin/env python3
#
#
# date:     Sun 15 Oct 2017 02:16:26 PM CEST
#
# descr:    Praktikum Programmieren 1 - Aufgabenblatt 2

import math
from sys import exit




# Aufgabe 2.0

# A
# README:In dieser Aufgabe musste der Klassename durch Freund ersetzt werden, um
# Konflikte zu vermeiden

class Freund:


    def __init__(self, name, vorname, alter,gros):
        self.name = name
        self.vorname = vorname
        self.alter = alter
        self.gros = gros
        self.aelterCount = 0
        self.freundListe = []

    def werdeAelter(self):
        self.aelterCount += 1
        self.alter += 1

        if self.aelterCount == 10:
            self.gros -= 1
            self.aelterCount = 0


    def isBaby(self):
        if self.alter in [0,1]:
            print(self.vorname, 'ist noch ein Baby')
            return True

        print(self.vorname, 'ist kein Baby')
        return False



    def neuerFreund(self,x):
        self.freundListe.append(x)


    # return list of friend names
    def freunde(self):
        freundNamen = []
        for x in self.freundListe:
            freundNamen += [x.vorname]
        return freundNamen



    def aelteserFreund(self):
        alterFreund = []
        for x in self.freundListe:
            alterFreund.append((x.alter, x.name))
        return max(alterFreund, key=lambda item: item[0])








# Aufgabe 2.1
#
# TO-DO:    Getter Setter
#           Verwaltung erleichtern. Bswp. update von ects eines Studentens

class Person:

    def __init__(self,vorname,nachname,alter,geburtstag):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.geburtstag = geburtstag


class Student(Person):

    def __init__(self,matr,semester,ects):
        super().__init__()
        self.matrikelnummer = matr
        self.semester = semester
        self.ects = ects

class Professor(Person):

    def __init__(self,vorname,nachname,alter,geburtstag,berufung):
        super().__init__(vorname,nachname,alter,geburtstag)
        self.berufungsgebiet = berufung

class Uni:

    def __init__(self, name, ort):
        self.name = name
        self.ort = ort
        self.studiganList = []


    def addStudigang(self,x):
        self.studiganList.append(x)

class Studiengang:

    def __init__(self, studname,typ):
        self.studname = studname
        self.typ = typ
        self.profList = []

    def addProf(self,x):
        self.profList.append(x)







# Aufgabe 2.2 +2.3
class Complex():

    def __init__(self, a, b):
        '''Creates Complex Number'''
        self.a = a
        self.b = b

    def __str__(self):
        '''Returns complex number as a string'''
        return '{} + {}i'.format(self.a, self.b)

    def __add__(self, rhs):
        '''Adds complex numbers'''
        return Complex(self.a + rhs.a, self.b + rhs.b)

    def __mul__(self, rhs):
        '''multiplies complex numbers'''
        return Complex(self.a * rhs.a, self.b * rhs.b)


# Aufgabe 2.4
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def toList(self):
         return self.items

    def multPop(self, n):
        for i in range(n):
            self.pop()
            self.toList()



##########################
#
#    Aufgabe 2.5
#
#   To-Do: Implement a dictionary to store the values
##########################


class AufgabenManager:

    def __init__(self):
        self.aufgaben = {}
        self.urgentJobs = {}

    def neueAufgabe(self,job,priority):
        if type(job) != str:
            print("First argument of kind {}, expected string".format(type(job)))
        elif type(priority) != int:
            print("Second argument of kind {}, expected integer".format(type(priority)))
        else:
            self.aufgaben[job] = priority

    def hoechstePrio(self):
        highestPrio = min(self.aufgaben.values())
        for key, value in self.aufgaben.items():
            if value == highestPrio:
                self.urgentJobs[key] = value
        return self.urgentJobs


    def erledigeNaechsteAufgabe(self):
        self.hoechstePrio()
        lastUrgentKey = list(self.urgentJobs)[-1]
        self.aufgaben.pop(lastUrgentKey, None)
        return self.aufgaben

    def alleAufgabenMitPrio(self,v):
        aufgabenListe = []
        for a in list(self.aufgaben.items()):
            if a[1] == v:
                aufgabenListe += [a[0]]
        return aufgabenListe


    def allePrios(self):
        prioList = []
        for a in list(self.aufgaben.items()):
            prioList += [a[1]]
        return sorted(set(prioList))


    def anzahlAufgabenPrio(self,prio):
        return len(self.alleAufgabenMitPrio(prio))

    def anzahlAufgaben(self):
        return len(list(self.info()))


    def info(self):
        return self.aufgaben

# Aufgabe 2.6

class Graph:

    def __init__(self):
        self.graph_dict = {}

    def V(self):     # knoten
        return list(self.graph_dict.keys())

    def E(self):
        return self.generate_kanten()

    def addNode(self, knoten):
        if knoten not in self.graph_dict:
            self.graph_dict[knoten] = []

    def addEdge(self, kante):
        if len(kante) != 2:
            print("Method 'addEdge' expects list of two elements - invalid number of elements")
            exit(0)
        else:
            (knoten1, knoten2) = tuple(kante)
            if knoten1 in self.graph_dict:
                self.graph_dict[knoten1].append(knoten2)
            else:
                self.graph_dict[knoten1] = [knoten2]

    def generate_kanten(self):
        kanten = []
        for knoten in self.graph_dict:  # keys
            for neighbour in self.graph_dict[knoten]: # values
                if {neighbour, knoten} not in kanten:
                    kanten.append((knoten, neighbour))
        return kanten


    def allSingles(self): # all nodes being isolated
        return [k for k in self.graph_dict if not self.graph_dict[k] ] # where k stands for nodes

    def mostEdges(self):
        allEdgesList = [t[0] for t in self.E()]
        return max(allEdgesList, key=allEdgesList.count)

    def neighbour(self, v):
        return list(self.graph_dict[v])


    def goFromTo(self,k,j):
        if j not in self.V():
            exit("Invalid! Node {} doesn't exist".format(j))
        previousNodesList = [key for key, value in self.graph_dict.items() if j in value] # those nodes...
        for x in previousNodesList: # ..that contain the endpoint
            if x == k:
                return [k,j] # end node is the neighbour of start point
            elif x in self.graph_dict[k]: # start node has neighbour that leads to end the point
                return [k,x,j]
            else:
                return self.goFromTo(k,x) + [j]









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






if __name__ == '__main__':
    ########################################
    # Aufgabe 2.0: Start Line 14
    #
    ########################################
    # A
#    hans = Freund('muller','hans',53,182)
#    elias = Freund('muller','elias',1 ,82)
#
#    # B
#    # for i in range(25):
#    #     hans.werdeAelter
#    #     if i % 5 == 0:
#    #         print(hans.alter)
#    #         print(hans.gros)
#
#    # C
#    hans.isBaby()
#    elias.isBaby()
#
#
#    hans.neuerFreund(Freund('reimus','kamil',35,188))
#    hans.neuerFreund(Freund('müller','johannes',42,182))
#    hans.neuerFreund(Freund('potter','harry',72,160))
#    hans.neuerFreund(Freund('stanis','baratheon',72,160))
#
#
#    print(hans.aelteserFreund())





    ########################################
    # Aufgabe 2.1: Start Line 101
    #
    ########################################

    # '''create a university'''
    # hs_albsig = Uni('Hochshule Albstadt Sigmaringen','Albstadt-Ebingen')

    # '''create some courses'''
    # hs_albsig.addStudigang(Studiengang('WIN','BA'))
    # hs_albsig.addStudigang(Studiengang('ITSec','BA'))

    # # print(hs_albsig.studiganList[0].studname) # WIN

    # '''create some professors too'''
    # haberlein = Professor('Tobias','Haeberlein',40,'13-11-1994',
    #                       'Algorithmik')

    # hs_albsig.studiganList[0].addProf(haberlein)
    # print(hs_albsig.studiganList[0].profList[0].nachname) # Haeberlein



    ########################################
    # Aufgabe 2.2+3: Start Line 177
    #
    ########################################

    # x1 = Complex(1.0, 2.0)
    # x2 = Complex(2, 3)
    # x3 = x1.__add__(x2)

    # print(x1+x2)

    ########################################
    # Aufgabe 2.4: Start Line 208
    #
    ########################################

    # s = Stack()
    # s.push(1) ; s.push("HallO") ; s.push(4.32) ; s.push(True)

    # print(len(s))           #   4
    # print(s.toList())       #   returns list of elements

    # s.multPop(2)            #   run multPop n times
    # print(s.toList())       #   check if multPop worked as intended

    ########################################
    # Aufgabe 2.5: Start Line 256
    #
    ########################################

    # manageR.neueAufgabe(5, 2) # leave as comment!!! Attempt will fail
    # manageR = AufgabenManager() # create instance of the class
    # manageR.neueAufgabe('do the laundry', 2)
    # manageR.neueAufgabe('make food', 3)
    # manageR.neueAufgabe('read a book', 3)
    # manageR.neueAufgabe('play dota2', 1)
    # manageR.neueAufgabe('buy some croceries', 4)

    # print(manageR.hoechstePrio())
    # print('These are all your current jobs.\n',manageR.info())
    # print(manageR.erledigeNaechsteAufgabe())
    # print(manageR.alleAufgabenMitPrio(3))
    # print(manageR.allePrios())
    # print(manageR.anzahlAufgaben())

    ########################################
    # Aufgabe 2.6: Start Line 240
    #
    ########################################

    graph = Graph()

    # graph.addNode(1) # add a node to the graph
    # graph.addNode(2) # add a node to the graph
    # graph.addNode(3) # add a node to the graph
    # graph.addNode(4) # add a node to the graph
    # graph.addNode(5) # add a node to the graph
    # graph.addNode(6) # add a node to the graph
    # graph.addNode(7) # add a node to the graph

    # Do it the 'smart' way
    for i in range(1,10):
        graph.addNode(i)


    # edges of node 1
    graph.addEdge([1,2])
    graph.addEdge([1,3])
    graph.addEdge([1,4])

    # edges of node 2
    graph.addEdge([2,3])

    # edges of node 3
    graph.addEdge([3,4])
    graph.addEdge([3,6])

    # edges of node 4
    graph.addEdge([4,5])
    graph.addEdge([4,7])

    # edges of node 5
    graph.addEdge([5,1])

    # edges of node 6
    graph.addEdge([6,5])
    graph.addEdge([6,8])

    # edges of node 7
    graph.addEdge([7,5])

    # edges of node 8
    graph.addEdge([8,9])



    # print(graph.mostEdges())
    # print(graph.neighbour(2))

    print(graph.goFromTo(2,7)) # error! May god be with me


    ########################################
    # Aufgabe 2.7: Start Line 319
    #
    ########################################

    # c = Cntr("Hello welt hello")
    # d = Cntr("llloooX")
    # print(c+d)

    # print(c.most())



