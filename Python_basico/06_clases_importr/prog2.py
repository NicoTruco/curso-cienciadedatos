import rutinas as fn

totGerente = fn.sumar(7000,10000)
totGerHarrys = fn.sumar(7089,1000)
#print("Totales : ", tot," Total 2", tot1)
print(f"Totales : {totGerente} Total 2 {totGerHarrys}  Total 2 {totGerHarrys +700}")


run = []
nombres = []

run.append(10)  # Juanito
run.append(20)  # Maria
run.append(30)  # Pedrito

nombres.append('Juanito')
nombres.append('Maria')
nombres.append('Pedrito')

nombres.insert(2,'Harrys')
nombres.insert(2,'ZHarrys')
nombres.insert(2,'AHarrys')
nombres.insert(2,'BHarrys')
nombres.insert(2,'CHarrys')
run.insert(2,68)
run.insert(2,68)
run.insert(2,68)
"""
run.pop(1)
nombres.pop(1)

run.remove(68)
nombres.remove('Harrys')
"""

print(run)
print(nombres)
run.reverse()
nombres.reverse()
print("**********************************************")
print(run)
print(nombres)
print("count :" , run.count(10))
nombres.sort()
run.sort()
print("**********************************************")
print(run)
print(nombres)
