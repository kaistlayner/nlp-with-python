#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy
import csv
from sklearn.svm import SVC


# In[86]:


def normalizer(des):
    """
    Normalize the features all values from -1 to 1

    :param des: Length f features from n unique actors
    :type des: numpy.ndarray. shape: [num_features, dim_feature]
    return: Normalized features
    rtype: numpy.ndarray. shape: [num_features, dim_feature]
    """

    des = des - ((np.max(des, axis=0) + np.min(des, axis=0)) / 2)
    des = des / ((np.max(des, axis=0) - np.min(des, axis=0)) / 2)

    return des

def get_cluster(des, k, thres):
    """
    Make clusters from given features

    :param des: length f features from n unique actors
    :type des: numpy.ndarray. shape: [num_features, dim_feature]
    :param k: number of clusters
    :type k: int
    :param thres: threshold for K-MEAN clustering algorithm
    :type thres: int
    :return: k centroids with f features
    :rtype: numpy.ndarray. shape: [num_centorids, dim_feature]
    """

    des = normalizer(des)
    
    print(des)

    np.random.seed(0)

    f = np.shape(des)[1]

    centroids = np.array([np.random.rand(f) for i in range(k)])
#     centroids = np.array([des[i] for i in range(k)])

    while(1):
        print("updated centroids: \n", centroids)
        
        prev_centroids = centroids
        centroids = np.zeros((k, f))
        data_length = [0] * k

        for feat in des:
            idx = 0
            min = -1

            for cent, i in zip(prev_centroids, range(len(prev_centroids))):
                if (np.linalg.norm(feat-cent) < min or min == -1):
                    idx = i
                    min = np.linalg.norm(feat-cent)

            data_length[idx] += 1
            centroids[idx] += feat

        for i in range(len(centroids)):
            if (data_length[i] != 0):
                centroids[i] = centroids[i] / data_length[i]
            else:
                centroids[i] = np.random.rand(f)

        if (np.linalg.norm(centroids - prev_centroids) < thres):
            break

    return centroids

def get_labels(des, cent):
    """
    Make training dataset from centroids and descriptors

    :param des: length f features from n unique actors
    :type des: numpy.ndarray. shape: [num_features, dim_feature]
    :param cent: list of k centroids
    :type cent: numpy.ndarray. shape: [num_centorids, dim_feature]
    :return: Labels
    :rtype: numpy.ndarray. shape: [num_features, 1]
    """

    labels = []

    for feat in des:
        labels.append(np.argmin(np.linalg.norm(cent - feat, axis = 1)))

    labels = np.array(labels)

    return labels

def filter_db(db):
    """
    Filter the database based on some criteria
    e.g., exclude person who said no more than 5 sentenses throughout the movie

    :param db: Database
    :type db: dict
    ['name'](str): Name of actor to sentenses one said in the movie
    :return: Modified Database
    :rtype: dict
    ['name'](str): Name of actor to sentenses one said in the movie

    """


def extract_des(db):
    """
    Extract the feature for the PREPROCESSING from the database

    :param db: Database
    :type db: dict
    ['name'](str): Name of actor to sentenses one said in the movie
    :return: Modified Database
    :rtype: numpy.ndarray. shape: [num_features, dim_feature]
    """
    print('extract_des')
    # print(db)
    # return np.array(db)

    return None

def extract_feat(feats):
    """
    Extract the feature for the TRAINING DATA SET

    :param feats: List of sentences to extract feature
    :type feats: list. size: [num_sentences, 1 (string)]
    :return: Extracted feature
    :rtype: list. shape: [dim_feature2]
    """

def make_train_set(db, k, thres, num_sents):
    """
    Make training data set from database and features

    :param db: Database
    :type db: dict
    ['name'](str): Name of actor to sentenses one said in the movie
    :param k: Number of clusters for K-MEANS algorithm
    :type: int
    :param thres: Threshold for K_MEANS algorithm
    :type: int
    :param num_sents: Number of sentences for one training sample
    :type: int
    :return: None
    :rtype: None
    """
    if not os.path.isdir("train_data"):
        os.mkdir("train_data")

    db = filter_db(db)
    des = extract_des(db)

    centroids = get_cluster(des, k, thres)
    labels = get_labels(des, cent)

    f = open('train_data/train_set.csv','w', newline='')
    wr = csv.writer(f)

    for i in db:
        sents = db[i]
        label = labels[i]

        # 한 인물당 몇개의 데이터를 뽑을 건지 아직 specifiy 되지 않음
        feature = random.sample(sents, num_sents)
        feature = extract_feat(feature)

        wr.writerow(feature + [label])

    return None
