# You are working on a project and need to cut films into scenes.
# to help streamline the creation of the final films, the team needs to
# develop an automated way of breaking up individual shots (short sequence from a particular camera angle)
# in a film into scenes (a sequence of shots). there is already an algorithm that breaks the film up into shots and
# labels them with a letter. Identical shots are labelled with the same letter. write a function to split the film
# into as many short scenes as possible without confusing viewers by having the same shot appear in different scenes.
# This will partition the sequence of shot labels into scenes so that no shot label appears in more than one scene
# and each scene is as short as possible.
# the output should be the length of each scene.
#
# Input
# the input to the function/method consists of a list of characters representing the sequence of shots.
#
# Output
# Return a list of integers representing the length of each scene,
# in the order in which it appears in the given sequence of shots.
#
# example 1:
#
# inputList = [a,b,a,b,c,b,a,c,a,
#               d,f,e,e,g,d,e,
#               h,i,j,h,k,l,i,j]
# output:
# [9,7,8]
import random


def main():
    i = 0
    shotSequence = []
    while i < random.randrange(5, 10):
        shotSequence += [chr(random.randrange(97, 102))]
        i += 1
    i = 0
    while i < random.randrange(5,10):
        shotSequence += [chr(random.randrange(103, 108))]
        i += 1
    i = 0
    while i < random.randrange(5, 10):
        shotSequence += [chr(random.randrange(109, 114))]
        i += 1
    i = 0
    while i < random.randrange(5, 10):
        shotSequence += [chr(random.randrange(115, 122))]
        i += 1
    shotSequencer(shotSequence)


def shotSequencer(shot):
    sequence = []
    limit = 0
    older_limit = 0
    check = True
    print(shot)
#############################################################################
    while check:
        i = older_limit
        j = older_limit
        while i < len(shot):
            while j < len(shot):
                if shot[i] == shot[j]:
                    limit = j
                j += 1
            i += 1
        i = older_limit
        j = older_limit
        while i < limit:
            while j < limit:
                if shot[i] != shot[j]:
                    k = 0
                    while k < len(shot):
                        if shot[j] == shot[k] and k > limit:
                            limit = k
                        k += 1
                j += 1
            i += 1
        sequence += [(limit - older_limit)+1]
        i = j = limit
        older_limit = limit + 1
        if limit >= len(shot)-1:
            check = False
    print(sequence)


main()
