independence_stages = ["inicio", "organizacion", "resistencia", "consumacion"]
print (independence_stages[0:4])
print(len(independence_stages))

#List methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
# leaders.extend(independence_stages) // mix together
leaders.insert(1,"jose Maria Morelos")
# leaders.remove("Vicente Guerrero") // Delete fist match
# leaders.pop(1)
leaders.append("Agustin de Iturbide")
# leaders.clear() // quita todo lo de la ista
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
# print(leaders.sort())
new_leaders = leaders.copy
#new_leaders.reverse()

print(leaders)
print(new_leaders)