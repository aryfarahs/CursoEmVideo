n = input('Digite algo: ').strip().upper()
a = n.count('A')
p1 = n.find('A')+1
p2 = n.rfind('A')+1
print(f'A letra "A" aparece {a} vezes.')
print(f'Ela aparece por primeiro na letra {p1}.')
print(f'E aparece por ultimo na {p2}° letra.')