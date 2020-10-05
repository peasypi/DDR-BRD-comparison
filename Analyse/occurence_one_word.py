with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt') as f:
    contents = f.read()
    count = contents.count('Liebe')

print(count)
