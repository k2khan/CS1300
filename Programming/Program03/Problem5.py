import itertools

sentenceList = []
word = ''
sentence = input('')
while sentence != 'Done':
    sentenceList.append(sentence)
    sentence = input('')

horizontalPrint = ''

sortedSentences = list(itertools.zip_longest(*sentenceList))

for i in range(len(sortedSentences)):
    for y in range(len(sortedSentences[i])):
        if sortedSentences[i][y] == None:
            sortedSentences[i] = list(sortedSentences[i])
            sortedSentences[i][y] = ' '
        horizontalPrint += sortedSentences[i][y]
    print(horizontalPrint)
    horizontalPrint = ''

    
