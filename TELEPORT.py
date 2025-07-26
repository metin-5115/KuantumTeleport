# Adım 1: Bu sihirli komutu kodun en başına ekleyin.
%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt # plt'nin import edildiğinden emin olalım
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.result import marginal_counts
from qiskit.visualization import plot_histogram

# --- Devre Kurulumu (Bu kısım zaten doğru) ---
qr = QuantumRegister(3, name="q")
cr = ClassicalRegister(3, name="c")
teleportation_circuit = QuantumCircuit(qr, cr)

teleportation_circuit.x(qr[0])
teleportation_circuit.barrier()
teleportation_circuit.h(qr[1])
teleportation_circuit.cx(qr[1], qr[2])
teleportation_circuit.barrier()
teleportation_circuit.cx(qr[0], qr[1])
teleportation_circuit.h(qr[0])
teleportation_circuit.barrier()
teleportation_circuit.measure(qr[0], cr[0])
teleportation_circuit.measure(qr[1], cr[1])
teleportation_circuit.barrier()
with teleportation_circuit.if_test((cr[1], 1)):
    teleportation_circuit.x(qr[2])
with teleportation_circuit.if_test((cr[0], 1)):
    teleportation_circuit.z(qr[2])
teleportation_circuit.measure(qr[2], cr[2])

# Devre şeması sorunsuz çiziliyor
print("Güncellenmiş Teleportasyon Devresi:")
print(teleportation_circuit.draw())

# --- Simülasyon ---
print("\nSimülasyon başlatılıyor...")
sim = AerSimulator()
t_qc = transpile(teleportation_circuit, sim)
result = sim.run(t_qc).result()
counts = result.get_counts()
print("Simülasyon tamamlandı. Grafikler çizdiriliyor...")

# --- SONUÇLARI GÖSTERME (ÇÖZÜM BURADA) ---

# 1. Histogram
print("\nBaşlık 1: Tüm Ölçüm Sonuçları")
plot_histogram(counts)
plt.show()  # <-- Bu komut, ilk grafiğin gösterilmesini sağlar.

# 2. Histogram
final_qubit_counts = marginal_counts(counts, [2])
print("\nBaşlık 2: Sadece Işınlanan Kübitin (q2) Sonucu")
plot_histogram(final_qubit_counts)
plt.show()  # <-- Bu komut, ikinci grafiğin gösterilmesini sağlar.

