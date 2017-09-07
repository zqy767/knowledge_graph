#!/usr/bin/python
# coding=utf-8

file_set=["activity.txt","animal.txt","area.txt","artist.txt","author.txt","bird.txt","business.txt","city.txt","company.txt","enterprise.txt"
,"environment.txt","equipment.txt","fish.txt","food.txt","fruit.txt","game.txt","herb.txt","illness.txt","instrument.txt","job.txt"
,"local business.txt","man.txt","medicine.txt","musician.txt","plant.txt","professional service.txt","recipe.txt","service.txt"
,"skill.txt","specie.txt","species.txt","sport.txt","symptom.txt","tree.txt","vegetable.txt","vehicle.txt","woman.txt"]


data = []

class simhash:
   
    #构造函数
    def __init__(self, name='', tokens=[],frequency=[], hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens,frequency)
        self.name = name
   
    #toString函数
    def __str__(self):
        return str(self.hash)
   
    #生成simhash值   
    def simhash(self, tokens, frequency):
        v = [0] * self.hashbits
        for i in xrange(0,len(tokens)): #t为token的普通hash值          
            t=self._string_hash(tokens[i])
            f=frequency[i];
            #print(tokens[i]+" "+str(f))
            for j in range(self.hashbits):
                bitmask = 1 << j
                if t & bitmask :
                    v[j] += f #查看当前bit位是否为1,是的话将该位+1
                else:
                    v[j] -= f #否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint #整个文档的fingerprint为最终各个位>=0的和
   
    #求海明距离
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0;
        while x :
            tot += 1
            x &= x - 1
        return tot
   
    #求相似度
    def similarity (self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b : return b / a
        else: return a / b
   
    #针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):       
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x
            
'''
for name in file_set:
	tokens=[]
	frequency=[]
	input=open(name)
	while(1):
		text=input.readline()
		if not text :
			break;
		temp=text.split('\t')
		tokens.append(temp[0])
		frequency.append(int(temp[1]))
	hash=simhash(name.split('.')[0],tokens,frequency)
	data.append(hash)
	input.close()

result=''
for i in data:
	result=result+i.name+"\n"
	for j in data:
		if(i.name!=j.name):
			result=result+j.name+" "+str(i.hamming_distance(j)) +'\n'
	result=result+'\n'

output=open('simhash.txt','w')
output.write(result);
output.close();
'''


