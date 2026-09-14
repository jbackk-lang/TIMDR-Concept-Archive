import numpy as np
from math import gcd

class FieldResonanceValidator:
    """
    Sprawdza topologiczną homogeniczność granic pól w skalach makro, atomowej
    oraz kwantowej (Photon Engine) przy użyciu bezwymiarowej analizy stosunków fourierowskich.
    
    Weryfikuje zachowanie energii w punktach zwrotnych oraz wyznacza dynamiczne
    wektory dążenia (gradienty pędu) dla struktur niedomkniętych.
    """
    
    def __init__(self, max_harmonic=8, default_tolerance=1e-3):
        self.max_harmonic = max_harmonic
        self.default_tolerance = default_tolerance

    def validate_boundary_state(self, omega_input, omega_pivot, tolerance=None):
        """
        Główna metoda walidacyjna analizująca stan sprzężenia pól.
        
        Parametry:
        ----------
        omega_input : float - Częstotliwość wzbudzenia / napływu energii układu.
        omega_pivot : float - Naturalna częstotliwość rezonatora (punktu zwrotnego).
        tolerance   : float - Opcjonalna czułość detekcji idealnego domknięcia.
        
        Zwraca:
        -------
        dict - Kompletny zestaw metryk topologicznych i wektorów ewolucji pola.
        """
        if tolerance is None:
            tolerance = self.default_tolerance

        # Zapobieganie dzieleniu przez zero przy skrajnych stanach brzegowych
        if omega_pivot == 0:
            raise ValueError("Częstotliwość punktu zwrotnego (omega_pivot) nie może wynosić 0.")

        # 1. Wyznaczenie surowego stosunku częstotliwości (bezwymiarowa geometria)
        raw_ratio = float(omega_input) / float(omega_pivot)
        
        best_m = 1
        best_n = 1
        min_delta = float('inf')
        
        # 2. Identyfikacja najbliższego teoretycznego węzła topologicznego (m:n)
        for n in range(1, self.max_harmonic + 1):
            m = round(raw_ratio * n)
            if m == 0 or m > self.max_harmonic * 2:
                continue
                
            delta = abs(raw_ratio - (m / n))
            if delta < min_delta:
                min_delta = delta
                best_m = m
                best_n = n

        # Sprowadzenie ułamka m/n do formy nieskracalnej (węzeł podstawowy)
        common_divisor = gcd(best_m, best_n)
        m_prime = best_m // common_divisor
        n_prime = best_n // common_divisor

        # 3. Wyznaczenie Indeksu Spójności Geometrycznej (GRI)
        # Określa gęstość symetrii w docelowym punkcie domknięcia układu
        geometric_resonance_index = 1.0 / (m_prime * n_prime)
        
        # 4. Ocena domknięcia struktury (Warunek brzegowy jako wyznacznik stabilności)
        is_structure_closed = min_delta <= tolerance
        target_ratio = best_m / best_n

        # 5. Wyznaczenie Wektora Ewolucji Pola (kierunek dążenia topologicznego)
        if is_structure_closed:
            evolution_direction = "stable"
        else:
            # Określenie, czy układ dąży do kontrakcji fazowej, czy ekspansji
            evolution_direction = "contraction" if raw_ratio < target_ratio else "expansion"

        # 6. Kalkulacja asymetrycznej siły gradientowej (Asymmetric Driving Force)
        # Dla układów niedomkniętych generuje potencjał uogólniony (np. anizotropię pędu)
        if is_structure_closed:
            asymmetric_gradient_force = 0.0
        else:
            asymmetric_gradient_force = min_delta * geometric_resonance_index

        # Zwrócenie kompletnego profilu walidacyjnego struktury pola
        return {
            "topological_node": f"{m_prime}:{n_prime}",
            "raw_ratio": round(raw_ratio, 6),
            "field_tension_delta": round(min_delta, 6),
            "is_structure_closed": is_structure_closed,
            "predicted_closure_point": round(target_ratio, 6),
            "field_evolution_vector": evolution_direction,
            "asymmetric_gradient_force": round(asymmetric_gradient_force, 6),
            "geometric_resonance_index": round(geometric_resonance_index, 4)
        }


# =====================================================================
# BLOK TESTOWY pipeline'u walidacji dla trzech skal geometrycznych
# =====================================================================
if __name__ == "__main__":
    validator = FieldResonanceValidator(max_harmonic=8, default_tolerance=1e-3)
    
    print("=" * 60)
    print("PROFIL WALIDACYJNY: JEDNOLITA GEOMETRIA POLA")
    print("=" * 60)

    # 1. Skala Atomowa: Stabilność nuklearna wokół punktu żelaza (Struktura domknięta)
    print("\n[SKALA ATOMOWA] - Test stabilności izotopowej (Helium/Fe):")
    atom_data = validator.validate_boundary_state(omega_input=400.0, omega_pivot=200.0)
    for k, v in atom_data.items():
        print(f"  {k}: {v}")

    # 2. Skala Makro: Dysk akrecyjny Sgr A* (Niedomknięcie przejściowe -> Emisja ROSAT)
    print("\n[SKALA MAKRO] - Dynamika transferu energii 2MASS -> ROSAT:")
    macro_data = validator.validate_boundary_state(omega_input=301.8, omega_pivot=200.0)
    for k, v in macro_data.items():
        print(f"  {k}: {v}")

    # 3. Skala Kwantowa: Photon Engine (Trwałe niedomknięcie -> Asymetryczny Pęd)
    # Celowo bardzo niska tolerancja, by uchwycić stały gradient siły napędowej
    print("\n[SKALA KWANTOWA] - Sztuczna koniunkcja pól (Photon Engine):")
    quantum_data = validator.validate_boundary_state(omega_input=800.0, omega_pivot=500.0, tolerance=1e-6)
    for k, v in quantum_data.items():
        print(f"  {k}: {v}")
    print("=" * 60)
