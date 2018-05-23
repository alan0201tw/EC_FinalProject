import sys
sys.path.append("../chromosomeLib.py")

import chromosomeLib
import random

class World :
    def __init__(self):
        self.currentGeneration = 0   # generation index > int
        self.chromosomes = [chromosomeLib.Chromosome for i in range(10)]        # chromosomes > list of chromosome
        # use this to access best fitness chromosome
        self.bestFitnessIndex = 0

        for i in range(len(self.chromosomes)):
            if self.CompareFitness(self.chromosomes[i].getFitness() , self.chromosomes[self.bestFitnessIndex].getFitness()):
                self.bestFitnessIndex = i

    # determine whether A or B has better fitness, return True if fitnessA is better than fitnessB
    def CompareFitness(self , fitnessA , fitnessB) :
        # TODO
        return fitnessA < fitnessB
        #return True

    # return fitness only
    def GetBestFitness(self) :
        return self.chromosomes[self.bestFitnessIndex].getFitness()

    # return object
    def GetBestFitnesschromosome(self) :
        return self.chromosomes[self.bestFitnessIndex]

    def ToNextGeneration(self):
        nextGenerationchromosomes = []
        for i in range(len(self.chromosomes)):
            parentA , parentB = self.ParentSelection()
            nextGenerationchromosomes[i] = chromosomeLib.Chromosome(self.chromosomes[parentA] , self.chromosomes[parentB])
        
        self.chromosomes = nextGenerationchromosomes
        self.currentGeneration += 1
    
    # return 2 index representing two parents
    def ParentSelection(self):
        # TODO
        parentA , parentB = -1,-1

        # decide parentA
        indexList = range(0,len(self.chromosomes))
        tmpParentList = random.sample(indexList , 2)
        # if index 0 is better
        if self.CompareFitness(self.chromosomes[tmpParentList[0]].getGitness() , self.chromosomes[tmpParentList[1]].getGitness() ) :
            parentA = tmpParentList[0]
        else :
            parentA = tmpParentList[1]

        # decide parentB
        tmpParentList = random.sample(indexList , 2)
        # if index 0 is better
        if self.CompareFitness(self.chromosomes[tmpParentList[0]].getGitness() , self.chromosomes[tmpParentList[1]].getGitness() ) :
            parentB = tmpParentList[0]
        else :
            parentB = tmpParentList[1]

        return parentA , parentB
