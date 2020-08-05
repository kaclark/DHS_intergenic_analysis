import pickle

files = ["1", "2", "4", "8"]
for file in files:
    import_path = './data/jar/domains_with_DHSs_' + file + '.pickle'
    with open(import_path, 'rb') as pickle_in:
        domains = pickle.load(pickle_in)
    max = 0
    for domain in domains.keys():
        if len(domains[domain]) > max:
            max = len(domains[domain])
    print(file + " cell max number of enhancers in same TAD: " + str(max))
