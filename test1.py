from dwave.system import DWaveSampler, EmbeddingComposite
import dimod

# Define a simple QUBO problem
Q = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

# Set up the sampler
sampler = EmbeddingComposite(DWaveSampler())

# Sample the problem
response = sampler.sample_qubo(Q)

# Print the results
for sample in response.samples():
    print(sample)

