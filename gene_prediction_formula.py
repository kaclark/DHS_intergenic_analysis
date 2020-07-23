import numpy as np
import sys

input = int(sys.argv[1])

def prediction(gene_distance):
    w_1 = -8.15392002*pow(10, -7)
    b = 0.1874616
    w_2 = -0.6294551
    w_3 = 0.3701174
    first_layer = np.tanh(gene_distance*w_1)
    pred_1 = first_layer*w_2 + b
    pred_0 = first_layer*w_3 + b
    return(pred_1, pred_0)

print(prediction(input))

