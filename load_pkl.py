import pandas as pd

pickleFile = open("SMPL_MALE.pkl","rb")

obj = pd.read_pickle(pickleFile)
print (obj)