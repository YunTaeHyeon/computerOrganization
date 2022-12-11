#사용한 파이썬 버전 3.9.6

class LRUCache:
    def __init__(self, maxSize):
        self.newCache = {} #파이썬 최근 버전부터는 딕셔너리에서 순서성을 보장함 
        self.maxSize = maxSize

    def read(self, address): #캐시에서 읽어오는 함수
        if address in self.newCache: 
            value = self.newCache.pop(address)
            self.newCache[address] = value # pop 이후 다시 write하면 가장 최근으로 등록
            return self.newCache[address]
        else: 
            return -1 #캐시에서 읽어오기 실패했을 경우 

    def write(self, address, value): #캐시에다가 쓰는 함수
        if address in self.newCache: 
            self.newCache.pop(address)
        elif len(self.newCache) == self.maxSize:
            self.newCache.pop(next(iter(self.newCache))) # 쓴 지 오래된 값 삭제
        self.newCache[address] = value

hit=0 #히트했을 경우
hitOrNot=0 #전체 경우

cacheSize=int(input("cache size: "))
blockSize=int(input("block size: "))
associative=int(input("associate: "))

setSize=cacheSize/blockSize/associative #setSize 구하는 공식

cache=LRUCache(cacheSize) 

fileName=input("fileName: ")
file=open(fileName,'r') #read 권한으로 파일 열기

data=file.readlines()
datalist=''.join(data).split() #문자열로 변환 후 split

for i in range(0,len(datalist)-3,3):
    if datalist[i]=="l":
        if cache.read(datalist[i+1]) != -1:
            hit+=1
            hitOrNot+=1
        else:
            cache.write(datalist[i+1],datalist[i+2])
            hitOrNot+=1

print("hit rate : ",hit/hitOrNot)
