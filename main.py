import sys
sys.path.append("../chromosomeLib.py")
sys.path.append("../worldLib.py")

import chromosomeLib
import worldLib

# do unit tests
def main() :
    world = worldLib.World()

    generationIndex = 0
    while generationIndex < 100 :
        print( "Best fitness is :" , world.GetBestFitness() )
        print( "Best chromosome is :" , world.GetBestFitnesschromosome().toString() )
        world.ToNextGeneration()

    # TODO : input the result ( the last best fitness chromosome ) to a text file

if __name__ == "__main__" :
    main()