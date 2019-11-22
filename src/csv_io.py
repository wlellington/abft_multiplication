# Wesley Layton Ellington
# Fault Tolerant Computing
# Fall 2019
# Term Project: ABFT Multiplication 

# A collection of functions for dealing with CSV input and output, generating random input files

import csv
import numpy as np

# Write matrix out to file as CSV
def write_csv(data_matrix, filename):
	np.savetxt(filename, data_matrix, delimiter=', ', newline='\n', fmt='%d')
	
# Read in CSV as file
def read_csv(filename):
	data_matrix = np.loadtxt(filename, delimiter=', ', dtype=int)
	return data_matrix

# Generate matrix of random values
def generate_random_matrix(num_rows, num_cols):
	#rand_matrix = np.random.rand(num_rows, num_cols)
	rand_matrix = np.random.randint(-1000, 1000, size=(num_rows, num_cols))
	return rand_matrix
