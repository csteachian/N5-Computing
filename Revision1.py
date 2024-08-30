pi = ["192.168.87.119", "192.168.87.90"]
pi.append("192.168.87.2")

print(pi)

for index in range(len(pi)):
    if pi[index] == "192.168.87.90":
        print(pi[index])
        print("Found it")
