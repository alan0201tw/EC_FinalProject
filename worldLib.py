import chromosomeLib
import random

class World :
    def __init__(self , WordManager):
        self.wordManager = WordManager

        self.currentGeneration = 0   # generation index > int
        self.chromosomes = [chromosomeLib.Chromosome(self.wordManager) for i in range(100)]        # chromosomes > list of chromosome
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
            nextGenerationchromosomes.append(chromosomeLib.Chromosome(self.wordManager , self.chromosomes[parentA] , self.chromosomes[parentB]))
        
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
        if self.CompareFitness(self.chromosomes[tmpParentList[0]].getFitness() , self.chromosomes[tmpParentList[1]].getFitness() ) :
            parentA = tmpParentList[0]
        else :
            parentA = tmpParentList[1]

        # decide parentB
        tmpParentList = random.sample(indexList , 2)
        # if index 0 is better
        if self.CompareFitness(self.chromosomes[tmpParentList[0]].getFitness() , self.chromosomes[tmpParentList[1]].getFitness() ) :
            parentB = tmpParentList[0]
        else :
            parentB = tmpParentList[1]

        return parentA , parentB
