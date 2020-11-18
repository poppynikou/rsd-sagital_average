import numpy as np

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample_2.csv", data_input, fmt='%d', delimiter=',')