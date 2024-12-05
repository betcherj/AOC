
with open("data.txt", "r+") as f:
    data = f.read()


i = 0
solution = 0
while i < len(data):
    if data[i:i+4] == "mul(":
        i += 4
        if data[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            continue
        start = i
        while i < start+3:
            i += 1
            if data[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
        num1 = int(data[start:i])
        if data[i] != ",":
            continue
        i += 1

        if data[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            continue
        start = i
        while i < start+3:
            i += 1
            if data[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
        num2 = int(data[start:i])
        if data[i] != ")":
            continue
        i += 1
        solution += (num1*num2)
    else:
        i += 1

print(solution)