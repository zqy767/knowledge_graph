#!/usr/bin/python
# coding=utf-8

from simhash import simhash

LINE = 45
MAX_NUMBER = 500
MIN_NUMBER = 20

def find_all_instances (filename,filter_list) :
    token = dict()
    frq = dict()
    num = 0
    filter_set = set(filter_list);
    for line in open(filename) :
        concept = line.split("\t")[0];
        if num % 1000000 == 0 :
            print num;
        num+=1
        if (concept in filter_set) :
            if (concept in token) :
                token[concept].append(line.split("\t")[1])
                frq[concept].append(int(line.split("\t")[2]))
            else :
                token[concept] = [line.split("\t")[1]]
                frq[concept] = [int(line.split("\t")[2])]
    print "read finished"
    return (token,frq)

def find_interaction(fs,name1,name2,token1,token2,frq1,frq2) :
    set1 = set(token1)
    set2 = set(token2)
    dict1 = dict(zip(token1,frq1))
    dict2 = dict(zip(token2,frq2))
    interaction = set1 & set2
    for element in interaction :
        if (dict1[element] >= MAX_NUMBER and dict2[element] <= MIN_NUMBER or dict2[element] >= MAX_NUMBER and dict1[element] <= MIN_NUMBER) :
            res = element + '\t' + name1 + '\t' + str(dict1[element]) + '\t' + name2 + '\t' + str(dict2[element]) + '\n';
            fs.write(res)
            fs.flush()


filter_list = [];
for line in open("filter.txt") :
    filter_list.append(line.split("\t")[0]);


token = dict();
frq = dict();
(token,frq) = find_all_instances("data-concept-instance-relations.txt",filter_list);


hash_data = [];
simhash_output = open('simhash.txt','w');
answer = open('answer.txt','w');
inac = open("interaction.txt",'w')

for name in filter_list :
    sim = simhash(name,token[name],frq[name]);
    hash_data.append(sim);
    simhash_output.write(sim.name);
    simhash_output.write("\t");
    simhash_output.write(str(sim.hash));
    simhash_output.write('\n');


print len(hash_data)
for i in range(0,len(hash_data)-1) :
    if (i % 200 == 0) :
	print i;
    for j in (range(i+1,len(hash_data))) :
        if (hash_data[i].hamming_distance(hash_data[j]) >= LINE) :
              sent = hash_data[i].name + '\t' + hash_data[j].name + '\n';
              answer.write(sent)
              find_interaction(inac,hash_data[i].name,hash_data[j].name,token[hash_data[i].name], token[hash_data[j].name],frq[hash_data[i].name],frq[hash_data[j].name]);
