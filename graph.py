#graph O(V+E)
from collections import deque

def person_is_seller(name):
	return name[-1] == 'm'

def search(name):
	search_queue = deque()
	search_queue += graph["you"]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print("{} is a mango seller".format(person))
			else:
				search_queue += graph[person]
				searched.append(person)

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

search("you")
