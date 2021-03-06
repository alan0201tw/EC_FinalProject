class WordManager:
    def __init__(self, textBaseDirName):
        self.subjectiveList = []
        self.verbList = []
        self.objectiveList = []
        self.connectionList = []
        self.terminationList = []

        self.verbVal = []
        self.objectiveVal = []

        self.textBaseDirName = textBaseDirName+"/"

        self.initializeManager()

    def GetTerminationStringByIndex(self, terminationIndex):
        return self.terminationList[terminationIndex]

    def GetSubjectiveStringByIndex(self, subjectiveIndex):
        return self.subjectiveList[subjectiveIndex]

    def GetVerbStringByIndex(self, verbIndex):
        return self.verbList[verbIndex]

    def GetObjectiveStringByIndex(self, objectiveIndex):
        return self.objectiveList[objectiveIndex]

    def GetConnectionStringByIndex(self, connectionIndex):
        return self.connectionList[connectionIndex]

    def GetSubjectiveListLength(self):
        return len(self.subjectiveList)

    def GetVerbListLength(self):
        return len(self.verbList)

    def GetObjectiveListLength(self):
        return len(self.objectiveList)

    def GetconnectionListLength(self):
        return len(self.connectionList)

    def GetterminationListLength(self):
        return len(self.terminationList)

    def VectorMultiplication(self , vector , floatV):

        #print("type(vector) = " , type(vector))	
        #print("type(floatV) = " , type(floatV))	
        
        return [i * floatV for i in vector]

    def EvaluateChromesomeEmotion(self, sentences):
        # TODO : implementation

        # edit this to test!
        vectorLength = len(self.objectiveVal[0])
        targetEmotion = [0.0 for i in range(vectorLength)]
        chromosomeEmotion = [0.0 for i in range(vectorLength)]
        # default set second element of vector as the target emotion
        targetEmotion[1] = 1.0
        phraseCount = 0.0

        for sentenceIndex in range(len(sentences)) :
            # deal with start phrase and each follow up phrase
            t_emotionVector = self.VectorMultiplication(self.objectiveVal[sentences[sentenceIndex].startPhrase.objectiveIndex], self.verbVal[sentences[sentenceIndex].startPhrase.verbIndex])
            chromosomeEmotion = [x + y for x, y in zip(t_emotionVector, chromosomeEmotion)]
            phraseCount += 1.0

            for followUpIndex in range(len(sentences[sentenceIndex].followUpPhrases)) :
                t_emotionVector = self.VectorMultiplication(
                    self.objectiveVal[sentences[sentenceIndex].followUpPhrases[followUpIndex].objectiveIndex],
                    self.verbVal[sentences[sentenceIndex].followUpPhrases[followUpIndex].verbIndex])
                chromosomeEmotion = [x + y for x, y in zip(t_emotionVector, chromosomeEmotion)]
                phraseCount += 1.0

        #chromosomeEmotion = [i / phraseCount for i in chromosomeEmotion]

        difference = 0.0
        
        for index in range( len(targetEmotion) ) :
            difference += abs(targetEmotion[index] - chromosomeEmotion[index])
        #print("chromosomeEmotion = " , chromosomeEmotion)
        return difference

    def initializeManager(self):
        # TODO : Read from file, rather than hard coded in script
        #lines = [line.rstrip('\n') for line in open("TextBase/Subjective.txt")]

        #self.subjectiveList = ["I", "You", "We", "They", "He", "She", "It"]
        self.subjectiveList = [line.rstrip('\n') for line in open(self.textBaseDirName+"Subjective.txt")]

        #self.verbList = ["be", "have", "do", "say", "go", "get", "make", "know", "think", "take",\
        #"see", "come", "want", "look", "use", "find", "give", "tell", "work", "call"]
        self.verbList = [line.rstrip('\n') for line in open(self.textBaseDirName+"Verb.txt")]

        #self.objectiveList = ["time", "people", "way", "thing", "life", "school", "state", \
        #"problem", "questions", "home", "friend"]
        self.objectiveList = [line.rstrip('\n') for line in open(self.textBaseDirName+"Objective.txt")]

        self.connectionList = [" and", " ,"]

        self.terminationList = [".","!"]

        self.verbVal = [line.rstrip('\n') for line in open(self.textBaseDirName+"VerbValue.txt")]
        for index in range( len(self.verbVal) ) :
            self.verbVal[index] = float(self.verbVal[index])

        self.objectiveVal = [line.rstrip('\n') for line in open(self.textBaseDirName+"ObjectiveValue.txt")]
        for index in range( len(self.objectiveVal) ) :
            self.objectiveVal[index] = self.objectiveVal[index].split()
            self.objectiveVal[index] = [float(i) for i in self.objectiveVal[index]]
