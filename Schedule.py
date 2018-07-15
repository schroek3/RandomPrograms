#Schedule.py
#A schedule creator
import numpy as np


class Schedule:
	def __init__(self,listOfTeams):
		teams = listOfTeams

	def createScheduleList(self):
		np.random.shuffle(listOfTeams)
		returnSched = []
		for i in range(len(listOfTeams)-1):
			mid = len(listOfTeams) / 2
			l1 = listOfTeams[:mid]
			l2 = listOfTeams[mid:]
			l2.reverse()
			if i % 2 == 1:
				returnSched = returnSched + [zip(l1,l2)]
			else:
				returnSched = returnSched + [zip(l2,l1)]
			listOfTeams.insert(1,listOfTeams.pop())


	def createGroupSchedule(self,seeded):
		




'''

def createScheduleList(division):
	s = []
	for i in range(len(division)-1):
		mid = len(division) / 2
		l1 = division[:mid]
		l2 = division[mid:]
		l2.reverse()

		if(i%2 == 1):
			s = s + [zip(l1,l2)]
		else:
			s = s + [zip (l2,l1)]
		division.insert(1,division.pop())

	return s

def createSchedule(division,sched,homenhome):
	for round in createScheduleList(division):
		for match in round:
			away = match[0]
			home = match[1]
			newGame = Game(0,0,away,home,0,0)
			sched.append(newGame)
	if homenhome:
		returnGames(sched)
	fixGameIDs(division,sched)



	for round in createScheduleList(division):
		for match in round:
			away = match[0]
			home = match[1]
			newGame = Game(0,0,away,home,0,0)
			sched.append(newGame)
	if homenhome:
		returnGames(sched)
	fixGameIDs(division,sched)
'''


if __name__=='__main__':
	pass
