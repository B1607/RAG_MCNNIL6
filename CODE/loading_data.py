from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel="IL6"

def data_label():
    return datalabel

def MCNN_data_load():

    neo_train="../dataset/neoantigen/train.npy"
    neo_test="../dataset/neoantigen/test.npy"
    oth_train="../dataset/others/neg_train.npy"
    oth_test="../dataset/others/neg_test.npy"
    
    
    x_train,y_train=data_load(neo_train,oth_train)
    x_test,y_test=data_load(neo_test,oth_test)
    return(x_train,y_train,x_test,y_test)

def data_load(pos,neg):
    pos_file=np.load(pos)
    neg_file=np.load(neg)
    
    pos_label = np.ones(pos_file.shape[0])
    neg_label = np.zeros(neg_file.shape[0])
    
    x=np.concatenate([pos_file,neg_file], axis=0)
    y=np.concatenate([pos_label, neg_label], axis=0)
    y= tf.keras.utils.to_categorical(y,2)
    #y.dtype='float16'
    gc.collect()
    return x ,