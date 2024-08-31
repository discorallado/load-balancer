import itertools
import numpy as np
from statistics import mean

# Parámetros del problema
num_loads = 8 
num_phases = 3

# Valores en watts para cada carga
loads_watts = [8325, 3552, 3552, 3552, 4552, 4552, 3552, 3810]

# tolerancia =0.13950746694472396
tolerancia=0.14

def generate_phase_combinations(num_loads, num_phases):
  phases = range(1, num_phases + 1)  # Crea una lista de fases (1, 2, 3, ...)
  combinations = itertools.product(phases, repeat=num_loads)  # Genera todas las combinaciones
  return list(combinations)

def filter_empty_phases(combination):
  return all(phase in combination for phase in range(1, num_phases + 1))

# suma=[] 
def is_balanced(phase_totals, tolerance=tolerancia):
  phases =[phase_totals[1]/1000, phase_totals[2]/1000, phase_totals[3]/1000]
  varianza = np.var(phases, ddof = 1)
  desviacion_estandar = np.sqrt(varianza)
  return desviacion_estandar <= tolerance
#   return abs(diff_ab - diff_bc - diff_ca)  <= tolerance

# Generar y mostrar las combinaciones
combinations = generate_phase_combinations(num_loads, num_phases)

# Filtrar las combinaciones y mostrarlas
filtered_combinations = list(filter(filter_empty_phases, combinations))

# Mostrar el número total de combinaciones filtradas
total_filtered_combinations = len(filtered_combinations)

# Filtrar las combinaciones balanceadas y mostrarlas
balanced_combinations = []
for combination in filtered_combinations:
    phase_totals = {1: 0, 2: 0, 3: 0}
    for load_index, phase in enumerate(combination):
        phase_totals[phase] += loads_watts[load_index]
    if is_balanced(phase_totals):
        balanced_combinations.append((combination, phase_totals))

# Mostrar el número total de combinaciones perfectamente balanceadas
total_perfectly_balanced = len(balanced_combinations)
# Mostrar las combinaciones perfectamente balanceadas
for combination, phase_totals in balanced_combinations:
    # promedio = mean((phase_totals[1], phase_totals[2], phase_totals[3]))
    # print(f"Combinación: {combination}, Totales por fase: {phase_totals}, promedio: {promedio}")
    print(f"Combinación: {combination}, Totales por fase: {phase_totals}")
print(f"Número total de combinaciones perfectamente balanceadas: {total_perfectly_balanced}")
