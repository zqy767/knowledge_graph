# -*- coding: utf-8 -*-
import numpy as np
from sklearn import svm

def read_data (filename) :
    x = [];
    y = [];
    for line in open(filename) :
        seq = line.split('\t');
        if (len(seq) == 2) :
            y.append(int(seq[0]));
            dis = seq[1].split(" ")[-1]
            x.append([int(dis)])
    return (x,y)


def count_threshold (x,y) :
    clf = svm.SVC(kernel = 'linear')
    clf.fit(x,y)
    print (-clf.intercept_[0]) / clf.coef_[0][0]






(x,y) = read_data("sample.txt");
count_threshold(x,y)
