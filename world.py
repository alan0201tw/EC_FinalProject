import sys
sys.path.append("../chromosome.py")

import chromosome

class World :
    def __init__(self):
        self.currentGeneration = 0   # generation index > int
        self.chromosomes = [chromosome.Chromosome for i in range(10)]        # chromosomes > list of chromosome
        # use this to access best fitness chromosome
        self.bestFitnessIndex = 0

        for i in range(len(self.chromosomes)):
            if self.CompareFitness(self.chromosomes[i].getFitness() , self.chromosomes[self.bestFitnessIndex].getFitness()):
                self.bestFitnessIndex = i

    # determine whether A or B has better fitness
    def CompareFitness(self , fitnessA , fitnessB) :
        # TODO
        return True

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
            nextGenerationchromosomes[i] = chromosome.Chromosome(self.chromosomes[parentA] , self.chromosomes[parentB])
        
        self.chromosomes = nextGenerationchromosomes
        self.currentGeneration += 1
    
    # return 2 index representing two parents
    def ParentSelection(self):
        # TODO
        return 0 , 1


# do unit tests
def main() :
    world = World()

    generationIndex = 0
    while generationIndex < 100 :
        print( "Best fitness is :" , world.GetBestFitness() )
        print( "Best chromosome is :" , world.GetBestFitnesschromosome().toString() )
        world.ToNextGeneration()

    # TODO : input the result ( the last best fitness chromosome ) to a text file

if __name__ == "__main__" :
    main()