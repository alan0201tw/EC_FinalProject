import sys
sys.path.append("../chromosomeLib.py")
sys.path.append("../worldLib.py")
sys.path.append("../wordManagerLib.py")

import chromosomeLib
import worldLib
import wordManagerLib

# do unit tests
def main() :
    wordManager = wordManagerLib.WordManager()
    world = worldLib.World(wordManager)

    generationIndex = 0
    while generationIndex < 100 :
        print( "--------GENERATION " , generationIndex , "--------" )
        print( "Best fitness is :" , world.GetBestFitness() )
        print( "Best chromosome is :" , world.GetBestFitnesschromosome().toString() )
        #print( "------------------------------------------------" )
        world.ToNextGeneration()
        generationIndex += 1

    # TODO : input the result ( the last best fitness chromosome ) to a text file

if __name__ == "__main__" :
    main()