
# Code from Chapter 12 of Machine Learning: An Algorithmic Perspective
# by Stephen Marsland (http://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html)

# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.

# Stephen Marsland, 2008

# A runner for the Genetic Algorithm
import ga
import numpy as np

stringLength = 20
fitnessFunction = 'fP.fourpeaks'
nEpochs = 101.0
populationSize = 100
mutationProb = -1
crossover = 'un'
nElite = 4
tournament = False

max = []
for MstringLength in range(10):
    print("String Length: ", stringLength * (MstringLength+1))
    for MnEpochs in range(3):
        print("nEpochs: ", nEpochs * (MnEpochs+1))
        for MpopulationSize in range(3):
            print("Population Size: ", populationSize * (MpopulationSize+1))
            for MnElite in range(1):
                for Mcrossover in range(2):

                    if Mcrossover == 0:
                        crossover = 'un'
                    else:
                        crossover = 'sp'

                    for Mtournalent in range(2):

                        if Mtournalent == 0:
                            tournament = True
                        else:
                            tournament = False

                        for MmutationProb in range(2):

                            if MmutationProb == 0:
                                mutationProb = -1.0
                            else:
                                mutationProb = MmutationProb / 10.0

                            success = []
                            fail = []

                            for testI in range(20):

                                ga1 = ga.ga(stringLength * (MstringLength+1),
                                            fitnessFunction,
                                            nEpochs * (MnEpochs+1),
                                            populationSize * (MpopulationSize+1),
                                            mutationProb,
                                            crossover,
                                            nElite * (MnElite+1),
                                            tournament)
                                Fitness = ga1.runGA()

                                dict = {}
                                #dict["iteration"] =
                                f = list(filter(lambda x: x > 100, Fitness))
                                localFail = list(filter(lambda x: x <= 100, Fitness))
                                success.extend(f)
                                fail.extend(localFail)

                                #print("\ni = ", i)
                                #print("Fitness", Fitness)

                                #print(type(f))
                            if len(success) > 0:
                                print("\nStringLength: ", stringLength * (MstringLength+1))
                                print("nEpochs:",nEpochs * (MnEpochs+1))
                                print("PopulationSize:", populationSize * (MpopulationSize+1))
                                print("MutationProb:", mutationProb)
                                print("CrossOver:", crossover)
                                print("NElite:", nElite * (MnElite+1))
                                print("Tournament:",tournament)
                                print("Percentage reaching bonus: ", len(success) / (len(success) + len(fail)))




