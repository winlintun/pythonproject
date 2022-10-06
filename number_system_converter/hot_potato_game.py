from PQueue import Queue

def hotPatato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPatato(["Aung Aung", "Mg Mg", "Thiha", "Thin Tin", "Ko Ko", "Hla Hal"], 8))

