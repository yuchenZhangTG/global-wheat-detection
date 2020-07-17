import os
import pandas as pd
from sklearn.model_selection import train_test_split
import ast
from shutil import copyfile

phases = ['train', 'val']
for f in ['images', 'labels']:
    if not os.path.isdir(f): os.mkdir(f)
    for p in phases:
        if not os.path.isdir(os.path.join(f,p)): os.mkdir(os.path.join(f,p))

image_folder = 'images'
dfa = pd.read_csv('train.csv',index_col=0)
box_count = dfa.groupby(level=0).count().width
#all_id = list(box_count.index)
all_id = list(set([i[:-4] for i in os.listdir('all_images')]))
idsets = train_test_split(all_id, test_size=0.1, random_state=7)
    

for p, ids in zip(phases, idsets):
    i=0
    for iid in ids:
        imagefile1 = os.path.join('all_images',iid+'.jpg')
        imagefile2 = os.path.join('images',p,iid+'.jpg')
        copyfile(imagefile1,imagefile2)
        
        if iid not in df.index: continue
        idf = dfa.loc[iid]
        if isinstance(idf, pd.Series):  dfa.loc[[iid]]
        with open(os.path.join('labels',p,iid+'.txt'),'w') as fw:
            for _,row in idf.iterrows():
                wi,hi, bbox = row.width, row.height, row.bbox
                xb,yb,wb,hb =ast.literal_eval(bbox)      
                yolo_row = [0,(xb+wb/2)/wi,(yb+hb/2)/hi,wb/wi,hb/hi]
                fw.write(' '.join([str(c) for c in yolo_row])+'\n')
        #i+=1
        #if i>10: break

