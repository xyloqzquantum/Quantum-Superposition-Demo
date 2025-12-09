# Xyloqz Quantum – Superposition Demo (Qiskit)

This project demonstrates a basic quantum computing concept: **superposition**.  
Using Qiskit, we create a 1-qubit quantum circuit, apply a Hadamard gate, and measure the output over 1024 shots.

The result shows an approximately **50/50 split between |0⟩ and |1⟩**, proving that the qubit enters a perfect superposition state before measurement.

---

## What This Demo Shows

- How to create a quantum circuit in Qiskit  
- How the **Hadamard gate** creates superposition  
- How measurement collapses the qubit into classical outcomes  
- How to visualise quantum measurement results using a histogram  

---

##  Code Example

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Create superposition
qc.h(0)

# Measure
qc.measure(0, 0)

# Run the simulation
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement counts:", counts)

# Plot histogram
plot_histogram(counts)
plt.show()
