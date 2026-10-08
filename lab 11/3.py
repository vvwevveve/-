found = False
for e in range(1, 151):
    if found:
        break
    e5 = e ** 5
    for a in range(1, e):
        if found:
            break
        a5 = a ** 5
        for b in range(a, e):
            if found:
                break
            b5 = b ** 5
            for c in range(b, e):
                if found:
                    break
                c5 = c ** 5
                for d in range(c, e):
                    if a5 + b5 + c5 + d ** 5 == e5:
                        print(a + b + c + d + e)
                        found = True
                        break