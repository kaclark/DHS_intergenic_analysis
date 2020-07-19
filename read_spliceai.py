import h5py
file = h5py.File("data/spliceAI/spliceai1.h5", "r")
key = 'model_weights'
dset = file[key]
for data_entry in dset:
    print(dset[data_entry])
