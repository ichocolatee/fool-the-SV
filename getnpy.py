import numpy as np
file_path=r'/root/data2/SRS/learning-to-fool-the-speaker-recognition-master/data/TIMIT/TIMIT_lower/processed/TIMIT_labels.npy'
data=np.load(file_path,allow_pickle=True)
data=data.item()
print(type(data))
for key,v in  data.items():
    print(key+'    '+str(v))