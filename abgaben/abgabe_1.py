#!/usr/bin/env python3
#
#
# date:     Tue 03 Oct 2017 04:03:02 PM CEST
#
# descr:    Aufgabenblatt 1 - Prog1
#
# fehlt:    A1.3 - nur das erste A im String soll ersetzt werden
#
#

# import python libraries
from math import sqrt
import cmath
from random import randint
import matplotlib.pyplot as plt
import copy

############
#
# AUFGABE 1
#
# Python als ”Taschenrechner“.
# Geben Sie einen Python-Ausdruck an, der Folgendes berechnet:
############

# A
# print(1000*12)

# B
# print(2*(8921-2348+123)-400) #12992

# C
# print(123**456)

# D
# print(sqrt(12**3+13**4)/sqrt(2)) # 123.06299200003224

# E
# print(2**(2**17)) # very long num

# F
# bigNum = str(2**(2**17))
# digits = len(bigNum)
# print(digits) # 39457


# G
bigNum  =   2**10000
bigStr  =   str(bigNum)
# print(bigStr[42])       # 6

# H: uncomment G for this
# print(bigStr.count('4'))    # 292
#
#
# # I
# if int(bigStr[1000]) in [1,3]:
#     print('is 1 or 3')
# else:
#     print('not in [1,3]')

# J: uncomment G

#if int(bigStr[1000]) and int(bigStr[2000]) in [1,3]:
#    print('ok')
#else:
#    print('not ok')


# K
# print((2+5j)**(-1+2j)) # i statt j wegen python sytanx

# L
# print((1j)**(1j))

# M
# def isSquare(q):
#    w   =   sqrt(q)
#    if w**2 == q:
#        print('{}, ist eine Quadratzahl'.format(q))
#    else:
#        print('{}, ist keine Quadratzahl'.format(q))
#
#isSquare(345612)    # keine Quadratzahl
#isSquare(9)         # ist Quadratzahl



############
#
# AUFGABE 1.2
#
# Schreiben Sie eine Funktion,
# die drei Zahlen übergeben bekommt und als Ergebnis
# die Summe der beiden größeren Zahlen zur¨uckliefert.
#
#
#
# def sumOfBiggestTwo(a,b,c):
#     l = sorted([a,b,c])
#     return l[-1] +l[-2]
#
# print(sumOfBiggestTwo(3,4,6))



############
#
# AUFGABE 1.3
#
# Ersetze von einer Benutzereingabe:
# Alle 'A' (uppercase) mit 'a' (lowercase)
#
#
#  Tipp: replace() hat nen dritten Parameter
#
#def lowerA():
#     userInput   =   input('Tipp einen Satz: ')
#     if userInput[0] == 'A':
#         print(userInput.replace('A','a', 1))
#
#     else:
#         print(userInput)
#lowerA()


############
#
# AUFGABE 1.4
#
# Ratespiel: Eine zufällig generierte Zahl soll vom Benutzer erraten werden.
#
# Ist die Zahl geringer, soll   -> "zu klein" ausgegeben werden
# Ist die Zahl größer, soll     -> "zu groß"  ausgegeben werden
# Ist die Zahl korrekt, soll    -> "richtig"  ausgegeben werden
#
# am Ende soll die Anzahl der Versuche als zurückgeliefert werden

# A
# def ratespiel(limit):
#     randNum =   randint(1,limit)
#     times   =   0

#     while True:
#         userInput   = int(input('Welche Zahl habe ich im Sinn? '))
#         if userInput < randNum:
#             print('Deine Eingabe war leider zu klein')
#         elif userInput > randNum:
#             print('Tut mir leid, zu gros')
#         else:
#             print('wow, richtig')
#             break
#         times += 1

#     print('Du hast {}, Versuche gebraucht'.format(times))

#     return times

# ratespiel(10)


#     myNum   =   randint(1,n)
#     guess   =   randint(1,n)

#     limit  = [1,n]
#     print('Gesuchte Zahl ist {}\n'.format(myNum))

#     while guess != myNum:
#         print('Geraten wurde: {}'.format(guess))
#         if guess < myNum:
#             limit[0] = guess #lower limit
#             guess = randint(limit[0],limit[1])
#         elif guess > myNum:
#             limit[1] = guess
#             guess = randint(limit[0],limit[1])


#     print('Geraten wurde: {}'.format(guess))
# rate(20)


# B: Abgabe



#def rate(n):
#    myNum   =   randint(1,n)
#    guess   =   randint(1,n)
#
#    limit  = [1,n]
#    print('Gesuchte Zahl ist {}\n'.format(myNum))
#
#    while guess != myNum:
#        print('Geraten wurde: {}'.format(guess))
#        userInput = input()
#        if userInput == "zu klein":
#            limit[0] = guess #lower limit
#            guess = randint(limit[0],limit[1])
#        elif userInput == "zu groß":
#            limit[1] = guess
#            guess = randint(limit[0],limit[1])
#
#    print('Geraten wurde: {}'.format(guess))
#
#rate(20)


# Aufgabe 1.5

# def argsList(*x):
#     return [x]
#
#
# print(argsList(4,123,26))



# Aufgabe 1.6
#
# A AND B
#
# statt 1/i**3 rechnet approxer() i**3 solange bis die Zahl 10 stellig ist
# approxDivOne dividiert diese Zahl mit 1.


#def kek(x):
#    n = 0
#
#    for i in range(1,x):
#        n += 1/(i**3)
#    return n
#
#print(kek(10000000))


#class Approxer:
#
#    def __init__(self,a,b,c):
#        self.prev   = a
#        self.next   = b
#        self.count  = c # Iteration
#
#
#
#    def approx(self,r):
#
#        while True:
#
#            self.next += 1/self.count**r # equals 1 for the first iterat.
#            if self.count >= 2: # necessary cause of line 248
#                self.prev = self.next - (1/(self.count-1)**r)
#            self.count +=1
#
#            if(self.next - self.prev) < 10**(-10):
#                return self.next
#
#
#
#def main():
#
#    number = Approxer(0,0,1)
#    print(number.approx(3))
#
#    piObj = Approxer(0,0,1)
#    pi  =   sqrt(piObj.approx(2)*6)
#    print(pi)
#
#
#
#main()


 # Aufgabe 1.7
#def lol():
#
#    userInput = input('Write a nice sentence, and i will make it a list: ')
#    listOfInput =   userInput.split()
#
#    fourWordsOnly = []
#    finalList = []
#
#    vowelCount = 0
#
#    for i in listOfInput:
#        if len(i) == 4 and i.islower():
#            fourWordsOnly.append(i)
#
#    for w in fourWordsOnly:
#        for b in w:
#            if b not in 'aeiou':
#                vowelCount += 1
#            else:
#                vowelCount = 0
#
#            if vowelCount == 3:
#                fourWordsOnly.remove(w)
#
#    print(fourWordsOnly)
#
#
#
#lol()



# Aufgabe 1.8
#
# Primzahlen: Eine natürliche Zahl, die größer als 1 und
# ausschließlich durch sich selbst und durch 1 teilbar ist.
#
#def isPrime(x):
#
#    if x < 2:
#        print('Primzahlen sind typischweise größer 1')
#    else:
#        for i in range (2,x):
#            if x % i == 0:
#                return False
#
#    return True
#
#print(isPrime(18))
#
##
## Aufgabe 1.9: uncomment 1.8 for this
##
##
#def listOfTwinPrimes():
#
#    primList    =   []
#    for i in range(2,10000):
#        if isPrime(i) and isPrime(i+2):
#            primList.append(i)
#            primList.append(i+2)
#
#    primList = sorted(list(set(primList)))
#    return  primList # set() entfernt alle dupliactes in einer Liste
#
#print(listOfTwinPrimes())


# Aufgabe 1.10

# A
# plt.plot([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9], 'bo')
# plt.ylabel('y-Achse')
# plt.xlabel('x-Achse')
# plt.show()


# B

#def plotB():
#
#    xlist = []
#    ylist = []
#    for i in range(21):
#        xlist.append(i)
#        ylist.append(i)
#
#    plt.plot(xlist,ylist[::-1], 'bo') # here ylist is reversed
#    plt.ylabel('y-Achse')
#    plt.xlabel('x-Achse')
#    plt.show()
#
#plotB()


# C
#def plotC():
#    sideValues, xlist, ylist = [],[],[]
#    for i in range(-5,6): sideValues.append(i)
#    for i in range(-10,11): xlist.append(i)
#    for i in xlist:
#        if i in [-10,10]:
#            ylist.append(sideValues)
#        else:
#            ylist.append(i)
#    plt.plot(xlist,ylist,'bo')
#    plt.show()
#plotC()


def plotC():

    #side values left
    x = [-10]*11
    y = [y for y in range(-5,6)]

    # values i between
    for i in range(-9,10): x += 2*[i]
    for i in range(19): y += [-5] + [5]

    # side values right
    x += [10]*11
    y += [y for y in range(-5,6)]

    plt.plot(x,y,'bo')
    plt.show()




plotC()
