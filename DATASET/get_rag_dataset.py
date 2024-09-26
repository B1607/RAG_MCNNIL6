#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-in","--path_input", type=str, help="the path of input file(.prottrans)")
parser.add_argument("-out","--path_output", type=str, help="the path of output file(.npy)")
parser.add_argument("-db","--database_path", type=str, help="the path of database(.npy)")
parser.add_argument("-maxseq","--max_sequence", type=int, default=1000,help="the maxseq of feature")
parser.add_argument("-nf","--num_feature", type=int, default=1024,help="the num_feature of feature")


args = parser.parse_args()
target_folder=args.path_input
database_dataset=args.database_path
path_output=args.path_output
maxseq=args.max_sequence
num_feature=args.num_feature


database=np.load(database_dataset)


def cal_length(embeddinng, maxseq ,num_feature):
    data = np.zeros((maxseq, num_feature), dtype=np.float64)
    data_len = len(embeddinng)
    if data_len < maxseq:
        data[:data_len, :] = embeddinng
    else:
        data[:, :] = embeddinng[:maxseq, :]
    #print(data.shape)
    data = data.reshape((1, 1, maxseq, num_feature))    
    return data


def vector_distance(target,dataset,maxseq,num_feature):
    target_len=cal_length(target,maxseq,num_feature)
    dist_tmp=[]
    new_embedding=[]
    for i in dataset:
        dist = np.linalg.norm(target_len - i)
        if len(dist_tmp) < 5:
            dist_tmp.append(dist)
            new_embedding.append(i)
            if len(dist_tmp) == 5:
                sorted_indices = np.argsort(dist_tmp)
                dist_tmp = [dist_tmp[j] for j in sorted_indices]
                new_embedding = [new_embedding[j] for j in sorted_indices]
        elif dist < dist_tmp[-1]:
            dist_tmp[-1] = dist
            new_embedding[-1] = i
            sorted_indices = np.argsort(dist_tmp)
            dist_tmp = [dist_tmp[j] for j in sorted_indices]
            new_embedding = [new_embedding[j] for j in sorted_indices]
    avg_embedding = np.mean(new_embedding, axis=0)
    combined_embedding = (target_len + avg_embedding) / 2
    return combined_embedding




def saveData(path,data):
    print(data.shape)
    np.save(path, data)


input_dir=os.listdir(target_folder)
result=[]

for i in input_dir:
    print(i)
    if i.endswith(".prottrans"):
        data = np.loadtxt(target_folder+"/"+i)
        #print(data)
        combine=vector_distance(data,database,maxseq,num_feature)
        result.append(combine)
        #print(combine)
data = np.concatenate(result, axis=0)
saveData(path_output, data)





