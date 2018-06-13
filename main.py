import chromosomeLib
import worldLib
import wordManagerLib
import plotly
from plotly.graph_objs import Scatter, Layout, Data

def draw_plot_graph(data, graph_title, textBaseDirName):
    plotly.offline.plot(
        {
            "data": data,
            "layout": Layout(title=graph_title)
        },
        filename=textBaseDirName+"_plot.html"
    )
# do unit tests
def main(textBaseDirName) :
    run_num = 3
    data = []
    # test for 10 run
    for i_run in range(run_num):
        try:
            wordManager = wordManagerLib.WordManager(textBaseDirName)
        except FileNotFoundError as e_file:
            print("no textbase: ", textBaseDirName)
            return
        world = worldLib.World(wordManager)

        generationIndex = 0
        bestFitness = []
        bestChromosome = []
        while generationIndex < 100 :
            if i_run == 0:
                print( "--------GENERATION " , generationIndex , "--------" )
                print( "Best fitness is :" , world.GetBestFitness() )
                print( "Best chromosome is :" , world.GetBestFitnesschromosome().toString() )
            #print( "------------------------------------------------" )
            bestFitness.append(world.GetBestFitness())
            bestChromosome.append(world.GetBestFitnesschromosome().toString())
            world.ToNextGeneration()
            generationIndex += 1

        scatter_data = Scatter(
            x = [x for x in range(101)], #generation
            y = bestFitness,
            text = bestChromosome,
            name = "result #"+str(i_run+1))
        data.append(scatter_data)
        print("finish run #",str(i_run+1))

    #output plot
    graph_title = "Best Fitness of every generation in "+textBaseDirName
    draw_plot_graph(data, graph_title, textBaseDirName)
    # TODO : input the result ( the last best fitness chromosome ) to a text file

if __name__ == "__main__" :
    main("TextBase_Drinks")
    #main("TextBase")
    #main("TextBase_Animal")
    main("TextBase_Food")