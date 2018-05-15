






class WordManager:
	def __init__(self):
		self.subjectiveList = []
		self.verbList = []
		self.objectiveList = []
		self.connectionList = []
		self.terminationList = []

		self.subjectiveVal = []
		self.verbVal = []
		self.connectionVal = []
		self.terminationVal = []
		self.objectiveVal = []

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

	def EvaluateChromesomeEmotion(self, chromosome):
    	# TODO : implementation
		return True

	def initializeManager(self):
		self.subjectiveList = ["I", "You", "We", "They", "He", "She", "It"]

		self.verbList = ["be", "have", "do", "say", "go", "get", "make", "know", "think", "take",\
		"see", "come", "want", "look", "use", "find", "give", "tell", "work", "call"]

		self.objective = ["time", "people", "way", "thing", "life", "school", "state", \
		"problem", "questions", "home", "friend"]

		self.connectionList = ["and", "or"]

		self.terminationList = [".", "?", "!"]


		self.subjectiveVal = [-0.37, 0.16, 0.54, 0.96, 0.93, 0.95, 0.62]
		self.verbVal = [-0.13, -0.49, -0.37,  0.99, -0.49, \
						-0.77,  0.30,  0.32, -0.94,  0.82, \
						 0.42, -0.54, -0.26,  0.51,  0.85, \
						-0.27, -0.46, -0.07, -0.05, -0.90]
		self.connectionVal = [1.0, 1.0]
		self.terminationVal = [1.0, 1.0, 1.0]
		self.objectiveVal = [-0.56, -0.50, 0.28, -0.86, 0.43, \
							  0.20, -0.27, 0.94, -0.37, 0.59, -0.29]
