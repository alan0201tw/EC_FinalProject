from random import randint, randrange

class Sentence:
    def __init__(self, startPhrase, followUpPhrases, terminationIndex):
        self.startPhrase = startPhrase # phrase
        self.followUpPhrases = followUpPhrases # phrase list
        self.terminationIndex = terminationIndex # int
    
    def toString(self, WordManager):
        startPhraseString = self.startPhrase.toString(WordManager)
        if len(self.followUpPhrases) > 0:
            followUpPhrasesStringList = [i.toString(WordManager) for i in self.followUpPhrases]
            followUpPhrasesString = "".join(followUpPhrasesStringList)
        else:
            followUpPhrasesString = ""
        sentenceString = startPhraseString + followUpPhrasesString
        sentenceString += WordManager.GetTerminationStringByIndex(self.terminationIndex)

        return sentenceString
    
    #getter
    """
    def get_startPhrase(self):
        return self.startPhrase
    
    def get_followUpPhrases(self):
        return self.followUpPhrases
    
    def get_terminationIndex(self):
        return self.terminationIndex
    """

class Phrase:
    def __init__(self, subjectiveIndex, verbIndex, objectiveIndex):
        self.subjectiveIndex = subjectiveIndex
        self.verbIndex = verbIndex
        self.objectiveIndex = objectiveIndex

    def toString(self, WordManager):
        subjectString = WordManager.GetSubjectiveStringByIndex(self.subjectiveIndex)
        verbString = WordManager.GetVerbStringByIndex(self.verbIndex)
        objectString = WordManager.GetObjectiveStringByIndex(self.objectiveIndex)

        phraseString = "{s} {v} {o}".format(s=subjectString, v=verbString,\
        o=objectString)
        return phraseString
    
    #getter
    """
    def get_subjectiveIndex(self):
        return self.subjectiveIndex
    
    def get_verbIndex(self):
        return self.verbIndex
    
    def get_objectiveIndex(self):
        return self.objectiveIndex
    """

class FollowUpPhrase(Phrase):
    def __init__(self, connectionIndex, subjectiveIndex, verbIndex, objectiveIndex):
        self.connectionIndex = connectionIndex
        super().__init__(subjectiveIndex, verbIndex, objectiveIndex)
    
    def toString(self, WordManager):
        connectionString = WordManager.GetConnectionStringByIndex(self.connectionIndex)
        phraseString = super().toString(WordManager)
        followUpPhraseString = "{connect} {phrase}".format(connect=connectionString, \
        phrase=phraseString)

        return followUpPhraseString
    
    #getter
    """
    def get_connectionIndex(self):
        return self.connectionIndex
    """
    
    # other getters are inheriented from phrase

class Chromosome:
    # instance variable:
    # generation, int
    # sentences, list
    # fitness, int
    # siblingSentence, list
    # sibling, choromesome
    def __init__(self, 
                 WordManager, 
                 parentA = None, 
                 parentB = None, 
                 siblingSentence = None ,
                 maxSentenceNum = 15, 
                 maxPhraseInASentenceNum = 3,
                 minSentenceNum = 3,
                 minPhraseInASentenceNum = 1):
        # record wordmanager
        self.wordmanager = WordManager

        # generate child using crossover
        if parentA is not None and parentB is not None:
            # generate sibling
            if siblingSentence != None:
                self.generation = parentA.getGeneration()+1
                self.sentences = siblingSentence
                self.fitness = self.wordmanager.EvaluateChromesomeEmotion(self.sentences)
                self.siblingSentence = None
                self.sibling = None
            # doing crossover
            else:
                self.generation = parentA.getGeneration()+1
                cutPoint = randrange(parentA.getSentencesListLength()+1)

                if cutPoint == 0:
                    self.sentences = parentB.sentences
                    self.siblingSentence = parentA.sentences
                elif cutPoint < parentA.getSentencesListLength():
                    if cutPoint < parentB.getSentencesListLength():
                        self.sentences = parentA.sentences
                        self.siblingSentence = parentB.sentences                    
                    else:
                        self.sentences = \
                            parentA.sentences[:cutPoint] + parentB.sentences[cutPoint:]
                        self.siblingSentence = \
                            parentB.sentences[:cutPoint] + parentA.sentences[cutPoint:]
                else:
                    self.sentences = parentA.sentences
                    self.siblingSentence = parentB.sentences
                
                self.fitness = self.wordmanager.EvaluateChromesomeEmotion(self.sentences)
                # do crossover will generate two childern, store it to sibling
                self.sibling = Chromosome(\
                    WordManager=self.wordmanager, parentA=parentA, parentB=parentB,\
                    siblingSentence = self.siblingSentence)

        # 0th generation, generate sentence randomely
        else:
            self.generation = 0
            self.sentences = []
            self.siblingSentence = None
            self.sibling = None
            
            sentenceNum = randint(minSentenceNum, maxSentenceNum)
            # get length of list in the WordManager
            subjectiveListLength = self.wordmanager.GetSubjectiveListLength()
            verbListLength = self.wordmanager.GetVerbListLength()
            objectiveListLength = self.wordmanager.GetObjectiveListLength()
            connectionListLength = self.wordmanager.GetconnectionListLength()
            terminationListLength = self.wordmanager.GetterminationListLength()
            for i_s in range(sentenceNum):
                phraseNum = randint(minPhraseInASentenceNum, maxPhraseInASentenceNum)

                # start phrase
                subjectiveIndex = randrange(subjectiveListLength)
                verbIndex = randrange(verbListLength)
                objectiveIndex = randrange(objectiveListLength+1)
                if objectiveIndex == objectiveListLength:
                    objectiveIndex = -1
                startPhrase = Phrase(subjectiveIndex, verbIndex, objectiveIndex)

                # follow up phrase
                followUpPhraseList = []
                for i_p in range(phraseNum-1):
                    connectionIndex = randrange(connectionListLength)
                    subjectiveIndex = randrange(subjectiveListLength)
                    verbIndex = randrange(verbListLength)
                    objectiveIndex = randrange(objectiveListLength)
                    followUpPhrase = FollowUpPhrase(connectionIndex, subjectiveIndex,\
                        verbIndex, objectiveIndex)
                    followUpPhraseList.append(followUpPhrase)
                
                # combine to a sentence
                terminationIndex = randrange(terminationListLength)
                self.sentences.append(Sentence(startPhrase, followUpPhraseList,\
                    terminationIndex))

            # update fitness value
            self.fitness = self.wordmanager.EvaluateChromesomeEmotion(self.sentences)
    """
    def compareTo(self, other):
        myFitness = self.fitness
        otherFitness = other.getFitness()

        if myFitness == otherFitness:
            return 0
        elif myFitness < otherFitness:
            return 1
        else:
            return -1
    """
    def toString(self):
        sentencesList = [i.toString(self.wordmanager) for i in self.sentences]
        return "".join(sentencesList)
    
    # return sibling
    def getSibling(self):
        return self.sibling

    #getter
    def getGeneration(self):
        return self.generation

    def getFitness(self):
        return self.fitness
    
    def getSentencesListLength(self):
        return len(self.sentences)
