found_alexandra = False
count = 0

while True:
    name = input()
    if name == "":
        break
    
    if name == "Александра":
        found_alexandra = True
        continue
        
    if name == "Левон":
        break
        
    if found_alexandra:
        count += 1

print(count)
