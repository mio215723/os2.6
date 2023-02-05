import glob
import os

def main():
    # print(glob.glob("/Users/mio/subject/prog1/temp/*"))
    returnTotal = searchDirectory(glob.glob("/Users/mio/src/go/hello*"))
    print(str(returnTotal[0]) + " " + str(returnTotal[1]) + " " + str(returnTotal[2]) + "   total")

def searchDirectory(files):
    allSumWord = 0
    allSumRow = 0
    allSumByte = 0
    for i in files:
        fileType = os.path.isdir(i)
        if(fileType != True):
            if(i[-3:] == ".go"):
                returnWC = wordCount(i)
                # 単語数とファイル名の出力
                print(str(returnWC[0]) + " " + str(returnWC[1]) + " " + str(returnWC[2]) + "  " + i)
                allSumRow += returnWC[0]
                allSumWord += returnWC[1]
                allSumByte += returnWC[2]
        else:        
            returnSum = searchDirectory(glob.glob(i + "/*"))
            allSumRow += returnSum[0]
            allSumWord += returnSum[1]
            allSumByte += returnSum[2]
    return allSumRow,allSumWord,allSumByte

        
def wordCount(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    sumByte = os.path.getsize(fileName)
    sumWord = 0
    sumRow=len(lines)#行数取得
    for c in lines:
        # sumByte += len(c)
        sumWord += len(c.split())
    f.close()
    return sumRow,sumWord,sumByte
    
    
if __name__ == "__main__":
    main()
