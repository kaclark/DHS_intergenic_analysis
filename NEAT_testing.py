import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import random
import subprocess
import neat

subprocess.call(["generated_shuffled_DHSs.sh"], shell=True)
#import dataset
with open('./data/jar/DHSs_onehot.pickle', 'rb') as pickle_in:
    onehot_data = pickle.load(pickle_in)
with open('./data/jar/var_chart.pickle', 'rb') as pickle_in:
    var_chart_data = pickle.load(pickle_in)
with open('./data/jar/gc.pickle', 'rb') as pickle_in:
    gc_data = pickle.load(pickle_in)
with open('./data/jar/lengths.pickle', 'rb') as pickle_in:
    length_data = pickle.load(pickle_in)
with open('./data/jar/get_group_from_dhs.pickle', 'rb') as pickle_in:
    groups_by_DHS = pickle.load(pickle_in)
with open('./data/jar/groups_trunc.pickle', 'rb') as pickle_in:
    groups_trunc = pickle.load(pickle_in)
with open('./data/jar/ng.pickle', 'rb') as pickle_in:
    ng_data = pickle.load(pickle_in)
with open('./data/jar/H3K27ac_count.pickle', 'rb') as pickle_in:
    H3K27ac_count_data = pickle.load(pickle_in)
with open('./data/jar/H3K4me3_count.pickle', 'rb') as pickle_in:
    H3K4me3_count_data = pickle.load(pickle_in)
with open('./data/jar/Nanog_count.pickle', 'rb') as pickle_in:
    Nanog_count_data = pickle.load(pickle_in)
with open('./data/jar/Oct4_count.pickle', 'rb') as pickle_in:
    Oct4_count_data = pickle.load(pickle_in)
with open('./data/jar/Sox2_count.pickle', 'rb') as pickle_in:
    Sox2_count_data = pickle.load(pickle_in)
with open('./data/jar/in_SE.pickle', 'rb') as pickle_in:
    in_SE_data = pickle.load(pickle_in)    

sample_dataframe = pd.read_csv("data/mm10_data/DHSs/shuffled_DHSs.bed", header=None, index_col=False)
DHSs_samples = []
for row in sample_dataframe[0]:
    DHSs_samples.append(row)

#flatten seq data sequence and extend list to have rest of data
#extend lists, append single values
inputs = {}
get_DHSs = {}
dhs_index = 0
for dhs in DHSs_samples:
    #if dhs in DHSs_samples:
    input_data = []
    for row in onehot_data[dhs]:
        input_data.extend(row)
    input_data.append(gc_data[dhs])
    input_data.append(length_data[dhs])
    input_data.append(ng_data[dhs])
    input_data.append(H3K27ac_count_data[dhs])
    input_data.append(H3K4me3_count_data[dhs])
    input_data.append(Nanog_count_data[dhs])
    input_data.append(Oct4_count_data[dhs])
    input_data.append(Sox2_count_data[dhs])
    input_data.append(in_SE_data[dhs])
    #add new data above this
    inputs[dhs] = input_data
    get_DHSs[dhs_index] = dhs
    dhs_index += 1
matched_list = []

# group dhs with its label
for dhs in DHSs_samples:
    matched_list.append([inputs[dhs], var_chart_data[dhs]])

#generate random unique indexes to pull out data for testing
testing_indexes = []
tmp_indexes = []
dhs_count = len(DHSs_samples)
testing_size = int(dhs_count/10)
while(len(testing_indexes) < testing_size):
    tmp_indexes.append(random.randint(0, dhs_count - 1))
    testing_indexes = list(set(tmp_indexes))
training_indexes = []
for x in range(dhs_count - 1):
    if x not in testing_indexes:
        training_indexes.append(x)
training_data_list = []
training_labels_list = []

for ind in training_indexes:
    training_data_list.append(matched_list[ind][0])
    training_labels_list.append(matched_list[ind][1])

testing_data_list = []
testing_labels_list = []

for ind in testing_indexes:
    testing_data_list.append(matched_list[ind][0])
    testing_labels_list.append(matched_list[ind][1])


#model structure
number_generations = 100
fitness_for_saving = 0.9

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        for dhs in training_data_list:
            ind = training_data_list.index(dhs)
            label = training_labels_list[ind]

            nnInput =  dhs
            output = net.activate(nnInput)

            for index, prediction in enumerate(output):
                if prediction < 0:
                    prediction = 0
                genome.fitness += (0.25/dhs_count) * (1 - abs(prediction - label[index]))
        if genome.fitness > fitness_for_saving:
            with open("./data/jar/best_model.pickle", 'wb') as pickle_out:
                pickle.dump(net, pickle_out)
            with open("./data/jar/testing_data.pickle", 'wb') as pickle_out:
                pickle.dump([testing_data_list, testing_data_labels], pickle_out)

config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation, './data/DHS_NEAT')
population = neat.Population(config)
population.add_reporter(neat.StdOutReporter(False))
stats = neat.StatisticsReporter()
winner = population.run(eval_genomes, number_generations)


