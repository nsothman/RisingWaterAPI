from itertools import islice
def getDictionaries(i, j):
    with open('C:\\Python Projects\\LearningFlask\\output_srtmOUT.asc') as f:
        line = next(islice(f, i, i+1))
        item = line.split('&')
        return item[j]
