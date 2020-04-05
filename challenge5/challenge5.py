import pickle

infile = open("banner.p",'rb')
new_dict = pickle.load(infile)
infile.close()

for l in new_dict:
    print("".join([i * j for i, j in l]))
