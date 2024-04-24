import os 
import argparse
import soundfile as sf 
import numpy as np 
from pathlib import Path
import tqdm 
import pickle
import csv
import pandas as pd 
import torch
import torchvision
from torch.utils.data import Dataset
import os
import os.path as osp
import numpy as np 
import torchaudio
import scipy 
import pickle
import csv
import pandas as pd
import soundfile as sf

def load_pickle(filenmae, encoding='utf8'):
    with open(filenmae, mode="rb") as fp:
        data = pickle.load(fp, encoding=encoding)
    return data

split = ['train', 'test']
data_list_dir = "./data/TIMIT/speaker"
# get speaker id set
test_data = pd.read_csv('/root/data2/SRS/learning-to-fool-the-speaker-recognition-master/data/TIMIT/TIMIT_lower/test_data.csv')
train_data= pd.read_csv('/root/data2/SRS/learning-to-fool-the-speaker-recognition-master/data/TIMIT/TIMIT_lower/train_data.csv')


speaker_id_file = "/root/data2/SRS/learning-to-fool-the-speaker-recognition-master/data/TIMIT/TIMIT_lower/processed/speaker_id.pickle"
print("load speaker id from: ", speaker_id_file)
speaker_idtop = load_pickle(speaker_id_file)
print(speaker_idtop)

timit_labels={}
for fr in test_data['path_from_data_dir']:
    if pd.isna(fr):
        break
    fr=str(fr)
    fr=fr.lower()
    print(fr)
    if fr.split('/')[-2] in speaker_idtop:data2/SRS/learning-to-fool-the-speaker-recognition-master/TIMIT_labels.npy
        timit_labels[fr]=speaker_idtop[fr.split('/')[-2]]

for fr in train_data['path_from_data_dir']:
    if pd.isna(fr):
        break
    fr=str(fr)
    fr=fr.lower()
    print(fr)
    if fr.split('/')[-2] in speaker_idtop:
        timit_labels[fr]=speaker_idtop[fr.split('/')[-2]] 

np.save(os.path.join("/root/data2/SRS/learning-to-fool-the-speaker-recognition-master", "TIMIT_labels.npy"), timit_labels)