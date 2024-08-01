from dwave.samplers import SimulatedAnnealingSampler


# Define a QUBO problem with only the upper triangle specified
Q = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

# Create an instance of SimulatedAnnealingSampler
sampler = SimulatedAnnealingSampler()

# Apply the sampling algorithm (solver) to solve the problem
response = sampler.sample_qubo(Q, num_reads=10)

# Print the samples with their counts
for sample, energy, occurences in response.aggregate().data(['sample', 'energy', 'num_occurrences']):
    print(f"Sample: {sample}, Energy: {energy}, Occurrences: {occurences}")
