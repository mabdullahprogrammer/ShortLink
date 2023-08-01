def replace(one, two):
    file = open('intents.py', "r")
    data = file.read()
    rdata = data.replace(one, two)
    file.close()
    fin = open('intents.py', "w")
    fin.write(rdata)
    fin.close()
