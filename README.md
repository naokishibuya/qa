# Quantum Annealing with D-Wave

You'll need to sign up for a D-Wave Leap account at [Leap](https://cloud.dwavesys.com/leap/) if you want to run some examples (that use the actual D-Wave quantum annealing machine) in this repository.

```
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the D-Wave Ocean SDK and Jupyter (if you want to run the Jupyter notebooks)
pip install dwave-ocean-sdk jupyter

# Configure the D-Wave Ocean SDK to use your Leap account
dwave config create
```