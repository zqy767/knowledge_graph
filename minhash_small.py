from datasketch import MinHash, MinHashLSH

dataset = dict();


def read_concept (namelist) :
    for name in namelist :
        name = name.replace("\n","");
        for line in open("./concepts/" + name + ".txt") :
            if name in dataset :
                dataset[name].append(line.split("\t")[0])
            else :
                dataset[name] = [line.split("\t")[0]];


name_list = []
for name in open("concept_list.txt") :
    name_list.append(name.replace("\n",""))

read_concept (name_list)
f = open("minhash_small.txt",'w')

for i in range(0,len(name_list)-1) :
    m1 = MinHash();
    for d in dataset[name_list[i]] :
        m1.update(d)
    for j in range(i+1,len(name_list)) :
        m2 = MinHash();
        for d in dataset[name_list[j]] :
            m2.update(d)
        result = name_list[i] + "\t" + name_list[j] + '\t' + str(m1.jaccard(m2))+'\n';
        f.writelines(result);
    f.write("\n");
