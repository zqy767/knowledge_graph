from datasketch import MinHash,MinHashLSH

MAX_NUMBER = 1000
MIN_NUMBER = 1

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

def find_interaction(ans,fs,name1,name2,token1,token2,frq1,frq2) :
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
            result = "";
            if (dict1[element] <= MIN_NUMBER) :
                result = element + '\t' + name1 + '\n'
            else :
                result = element + '\t' + name2 + '\n'
            if (result not in ans_set) :
                ans_set.add(result)
                ans.write(result)
                ans.flush()

filter_list = [];
ans_set=set()
for line in open("filter.txt") :
    filter_list.append(line.split("\t")[0]);
filter_list = filter_list[0:70000];
filter_set = set(filter_list)
token = dict();
frq = dict();
(token,frq) = find_all_instances("data-concept-instance-relations.txt",filter_list);


hash_data = dict();
lsh = MinHashLSH(threshold=0);
inac = open("minhash_interaction.txt",'w')
ansfile = open("wrong_point.txt",'w')

num = 0
for name in filter_list :
    if num % 1000 == 0 :
        print num
    num+=1
    m = MinHash();
    for d in token[name] :
        m.update(d);
    lsh.insert(name,m);
    hash_data[name] = m;


print "test started"
n = 0
for name in hash_data :
    n+=1
    if n % 200 == 0  :
        print n
    for i in filter_set - set(lsh.query(hash_data[name])) :
        find_interaction(ansfile,inac,name,i,token[name],token[i],frq[name],frq[i])
