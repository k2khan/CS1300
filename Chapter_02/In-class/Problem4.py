# Calculate BPM

beatsObserved = int(input("How many beats were observed? "))
secondsObserved = int(input("How many seconds were observed? "))

pulse = beatsObserved * (1 / (secondsObserved/60))
print("The pulse is", int(pulse), "beats per minute.")
