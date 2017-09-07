def read_data (file_name) :
    d = dict();
    for line in open(file_name) :
        concept = line.split('\t')[0]
        if concept in d :
            d[concept] += 1
        else :
            d[concept] = 1;
    return sorted(d.iteritems(),key = lambda x : x[1],reverse = True);

def write_data (filename,dict) :
    f = open(filename,'w')
    for key in dict:
        f.write(key[0])
        f.write("\t")
        f.write(str(key[1]));
        f.write("\n")
    f.close();



d = read_data("data-concept-instance-relations.txt")
write_data("count_number.txt",d)
