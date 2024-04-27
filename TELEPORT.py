import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

qr = QuantumRegister(3, name="q")
crz = ClassicalRegister(1, name="crz")
crx = ClassicalRegister(1, name="crx")
teleportation_circuit = QuantumCircuit(qr, crz, crx)

# Tüm durumları ışınlamak için
# teleportation_circuit.h(0)

# |1> ışınlamak için
# teleportation_circuit.x(0)

# |0> ışınlamak için
# teleportation_circuit.id(0)

teleportation_circuit.x(0)
teleportation_circuit.h(1)
teleportation_circuit.cx(1,2)
teleportation_circuit.draw()

teleportation_circuit.barrier()
teleportation_circuit.cx(0, 1)
teleportation_circuit.h(0)
teleportation_circuit.draw()


teleportation_circuit.barrier()
teleportation_circuit.measure(0,0) #crz
teleportation_circuit.measure(1,1) #crx
teleportation_circuit.draw()



teleportation_circuit.barrier()
teleportation_circuit.x(2).c_if(crx, 1)
teleportation_circuit.z(2).c_if(crz, 1)
teleportation_circuit.draw()

cr_result = ClassicalRegister(1)
teleportation_circuit.add_register(cr_result)
teleportation_circuit.measure(2,2)
teleportation_circuit.draw()

from qiskit.ignis.verification import marginal_counts
sim = QasmSimulator()
t_qc = transpile(teleportation_circuit, sim)
counts = sim.run(t_qc).result().get_counts()
plot_histogram(counts)

