from dwave.system import DWaveSampler, EmbeddingComposite


# Define a QUBO problem with only the upper triangle specified
Q = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

# Set up the sampler
sampler = EmbeddingComposite(DWaveSampler())

# Note: EmbeddingComposite automates the mapping of problem variables to the solver's qubits on the QPU,
#       optimizing the use of the QPU's limited physical qubit connectivity.

# Apply the sampling algorithm (solver) to solve the problem
response = sampler.sample_qubo(Q, num_reads=10)

# Print the samples with their counts (response is aggregated by default)
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    print(f"Sample: {sample}, Energy: {energy}, Occurrences: {occurences}")

