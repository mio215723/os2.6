import glob

def main():
    # print(glob.glob("/Users/mio/subject/prog1/temp/*"))
    totalWord = searchDirectory(glob.glob("/Users/mio/subject/*"))
    print(str(totalWord) + "   total")

def searchDirectory(files):
    allSumWord = 0
    for i in files:
        fileName = i.split("/")
        if("." in fileName[-1]):
            if(i[-3:] == ".py"):
                sumWord = wordCount(i)
                # 単語数とファイル名の出力
                print(str(sumWord) + "  " + i)
                allSumWord += sumWord
        else:        
            allSumWord += searchDirectory(glob.glob(i + "/*"))
    return allSumWord

        
def wordCount(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    sumWord=0
    for c in lines:
        sumWord += len(c)
    f.close()
    return sumWord
    
    
if __name__ == "__main__":
    main()
