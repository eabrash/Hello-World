## MyDogsRNA.py program copy

matureFile = open("C:\Users\Emily\Documents\Insight Fellows Related\Python\Python Files\mature.fa", mode = "rU")
myDogsRNAFile = open("C:\Users\Emily\Documents\Insight Fellows Related\Python\Python Files\myDogsRNA.txt", mode = "rU")
myOutputFile = open("C:\\Users\\Emily\\Documents\\Insight Fellows Related\\Python\\Python Files\\myOutput.txt", mode = "w")

matureRNANames = []
matureRNASeqs = []

for currentLine in matureFile:
    if currentLine[0] == ">":
        matureRNANames.append(currentLine[1:-1])
    else:
        matureRNASeqs.append(currentLine[0:-1])

#print matureRNANames[0:3]
#print matureRNASeqs[0:3]

matureRNAHits = []

for i in range(0,len(matureRNANames)):
    matureRNAHits.append(0)

#print matureRNAHits[0:3]


for currentLine1 in myDogsRNAFile:
    #trim the linker TCGT before putting the sequences into the list
    linkerStart = currentLine1.rfind("TCGT")
    trimmedLine = currentLine1[0:linkerStart]
    trimmedLineRNA = trimmedLine.replace("T","U")

    for j in range(0,len(matureRNANames)):
        if trimmedLineRNA == matureRNASeqs[j]:
            matureRNAHits[j] = matureRNAHits[j] + 1

for k in range(0,len(matureRNANames)):
    myOutputFile.write(matureRNANames[k] + "\t" + matureRNASeqs[k] + "\t" + str(matureRNAHits[k])+ "\n")

matureFile.close()
myDogsRNAFile.close()
myOutputFile.close()
