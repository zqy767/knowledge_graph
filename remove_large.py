def read_data (filename) :
    d=dict()
    for line in open(filename) :
        concept = line.split("\t")[0];
        count = int(line.split("\t")[1]);
        d[concept] = count;
    return d;

def remove_large (dict,small,large) :
    return {k:v for k,v in dict.items() if (v < large and v>small) }

def write_data (filename,dict) :
    f = open(filename,'w')
    for key in dict:
        f.write(key)
        f.write("\t")
        f.write(str(dict[key]));
        f.write("\n")
    f.close();

d = read_data("count_number.txt");
write_data("filter.txt",remove_large(d,8,10000))
