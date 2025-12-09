from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Simulator (updated backend)
sim = AerSimulator()

# Run the circuit
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement counts:", counts)

# Show histogram
plot_histogram(counts)
plt.show()
