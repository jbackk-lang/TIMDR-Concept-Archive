"""
FUNDAMENTAL EXECUTOR — FAI Core Execution Engine
================================================

execute(X) — rdzeń przetwarzania dla obiektów TIMDR/GIA/FUNDAMENTAL.

Implementacja operatorów:
  - T(X)     = topologia, pole
  - I(X)     = surowa informacja
  - M_p(X)   = modalność (perspektywa p)
  - I_t(X)   = X w chwili t
  - ΔI(X)    = zmiana w czasie
  - R(X)     = rezonans z polem
  - FUND(X)  = filtr (szum vs emergencja)
  - E(S)     = emergencja stabilna
"""

import numpy as np
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple
from enum import Enum


class ExecutionStatus(Enum):
    """Status wykonania obiektu"""
    NOISE = "noise"            # poniżej progu
    EMERGING = "emerging"      # przebudzenie się
    STABLE = "stable"          # stabilna emergencja
    DISSOLVING = "dissolving"  # zanikanie
    DEAD = "dead"              # poza byciem


@dataclass
class TimdrObject:
    """
    Uniwersalny obiekt TIMDR — może być:
    - fizycznym (cząstka, pole, fala)
    - psychicznym (emocja, myśl, schemat)
    - semantycznym (znacznik, pojęcie)
    - informatycznym (data, kod)
    """
    
    name: str
    
    # Operatory TIMDR
    T: str              # topologia / pole (np. "somatic", "quantum", "semantic")
    I: float            # intensywność informacji (0.0 - 1.0)
    M: str              # modalność / interpretacja (np. "threat", "opportunity")
    
    # Dynamika czasowa
    t_create: float = 0.0
    t_current: float = 0.0
    I_history: list = None  # ślad czasowy intensywności
    
    # Rezonans i spójność
    R: float = 0.5     # rezonans (0.0 - 1.0)
    
    # Stany wewnętrzne
    status: ExecutionStatus = ExecutionStatus.NOISE
    emergence_value: Optional[Any] = None
    
    def __post_init__(self):
        if self.I_history is None:
            self.I_history = []
    
    def __repr__(self):
        return (
            f"TimdrObject({self.name} | "
            f"T={self.T} I={self.I:.2f} M={self.M} "
            f"R={self.R:.2f} status={self.status.value})"
        )


class FundamentalExecutor:
    """
    Rdzeń wykonawczy dla TIMDR/GIA/FUNDAMENTAL.
    
    Przeprowadza pełny execute(X):
      S1 = T(X)   # topologia
      S2 = I(S1)  # ekstrakcja informacji
      S3 = M_p(S2)  # transformacja modalności
      S4 = I_t(S3)  # ewolucja czasowa
      S5 = R(S4)  # policz rezonans
      return FUND(S5)  # filtr + emergencja
    """
    
    def __init__(self, R_min: float = 0.3, dt: float = 0.1):
        """
        R_min: próg rezonansu (poniżej = szum)
        dt: krok czasowy symulacji
        """
        self.R_min = R_min
        self.dt = dt
        self.time = 0.0
        self.objects: Dict[str, TimdrObject] = {}
        self.field_strength = 0.5  # ogólna "temperatura" wszechświata
    
    # ============ OPERATORY TIMDR ============
    
    def T(self, obj: TimdrObject) -> Dict:
        """
        T(X) = topologia, wybór planszy (kontekstu).
        
        Zwraca opis topologicznego pola, na którym obiekt żyje.
        """
        topology = {
            "field_type": obj.T,
            "field_reference": self.field_strength,
            "dimensionality": self._get_field_dimensionality(obj.T),
            "boundary_conditions": self._get_boundary_conditions(obj.T),
        }
        return topology
    
    def I(self, topology_dict: Dict) -> float:
        """
        I(X) = ekstrakcja surowej informacji z topologii.
        
        W praktyce: musimy znać intensywność obiektu w polu.
        """
        # W tym modelu I jest już w obiekcie
        # ale moglibyśmy go policzyć z topologii
        return topology_dict.get("field_reference", 0.5)
    
    def M(self, obj: TimdrObject, perspective: str = "default") -> Tuple[str, float]:
        """
        M_p(X) = modalność z perspektywy p.
        
        Zwraca (interpretacja, siła_interpretacji).
        Ta sama informacja może być widziana inaczej z różnych perspektyw.
        """
        base_modality = obj.M
        
        # Skręt modalności w zależności od perspektywy
        perspective_twist = {
            "default": (base_modality, 1.0),
            "opposite": (self._flip_modality(base_modality), 0.7),
            "uncertain": ("uncertain", 0.5),
            "inverted": (self._flip_modality(base_modality), 0.9),
        }
        
        return perspective_twist.get(perspective, (base_modality, 1.0))
    
    def I_t(self, obj: TimdrObject) -> Tuple[float, float]:
        """
        I_t(X) = informacja w chwili t.
        ΔI(X) = zmiana w czasie.
        
        Zwraca (intensywność_teraz, delta_intensywność).
        """
        intensity_now = obj.I
        
        if len(obj.I_history) > 0:
            intensity_prev = obj.I_history[-1]
            delta_I = intensity_now - intensity_prev
        else:
            delta_I = 0.0
        
        obj.I_history.append(intensity_now)
        
        return (intensity_now, delta_I)
    
    def R(self, obj: TimdrObject, field_strength: Optional[float] = None) -> float:
        """
        R(X) = rezonans (spójność) obiektu z polem i sobą.
        
        R zależy od:
        - czy modalność M pasuje do pola?
        - czy intensywność I jest w rozumnym zakresie?
        - czy I(t) jest stabilne czy chaotyczne?
        """
        if field_strength is None:
            field_strength = self.field_strength
        
        # Komponenty rezonansu
        modal_alignment = self._modal_field_alignment(obj.M, field_strength)
        intensity_stability = self._intensity_stability(obj.I_history)
        internal_coherence = 1.0 - abs(obj.I - 0.5)
        
        R = (
            0.4 * modal_alignment +
            0.35 * intensity_stability +
            0.25 * internal_coherence
        )
        
        obj.R = max(0.0, min(1.0, R))
        return obj.R
    
    def FUND(self, obj: TimdrObject) -> ExecutionStatus:
        """
        FUND(S) = filtr fundamentalny.
        
        Czy obiekt jest szumem czy emergencją?
        - R < R_min → szum (noise)
        - R_min ≤ R < 0.6 → przebudzenie (emerging)
        - 0.6 ≤ R < 0.9 → stabilna emergencja (stable)
        - 0.9 ≤ R → rozpuszczanie się (dissolving) — za stały
        - I ≈ 0 → martwy (dead)
        """
        
        if obj.I < 0.01:
            obj.status = ExecutionStatus.DEAD
        elif obj.R < self.R_min:
            obj.status = ExecutionStatus.NOISE
        elif obj.R < 0.6:
            obj.status = ExecutionStatus.EMERGING
        elif obj.R < 0.9:
            obj.status = ExecutionStatus.STABLE
        else:
            obj.status = ExecutionStatus.DISSOLVING
        
        return obj.status
    
    def E(self, obj: TimdrObject) -> Optional[Any]:
        """
        E(S) = emergencja.
        
        Jeśli status != NOISE i != DEAD, to coś się wyłania.
        Emergencja zależy od kombinacji (T, I, M, R).
        """
        
        if obj.status in [ExecutionStatus.NOISE, ExecutionStatus.DEAD]:
            obj.emergence_value = None
            return None
        
        # Generowanie emergencji na bazie modalności i intensywności
        emergence_code = f"{obj.T}:{obj.M}:{obj.status.value}"
        
        # Mapa emergencji
        emergence_map = {
            # Somatyczne
            "somatic:threat:emerging": "alert",
            "somatic:threat:stable": "fight_or_flight",
            "somatic:threat:dissolving": "hypervigilance",
            
            # Poznawcze
            "cognitive:uncertainty:emerging": "exploration",
            "cognitive:uncertainty:stable": "investigation",
            "cognitive:opportunity:stable": "engagement",
            
            # Semantyczne
            "semantic:meaning:stable": "understanding",
            "semantic:meaning:dissolving": "crystallization",
            
            # Fizyczne
            "quantum:potential:emerging": "superposition_collapse",
            "quantum:certain:stable": "measurement_result",
        }
        
        obj.emergence_value = emergence_map.get(emergence_code, f"unknown:{emergence_code}")
        return obj.emergence_value
    
    # ============ GŁÓWNA PĘTLA WYKONAWCZA ============
    
    def execute(self, obj: TimdrObject) -> Dict:
        """
        execute(X): pełny cykl przetwarzania obiektu X.
        
        Pipeline:
          S1 = T(X)
          S2 = I(S1)
          S3 = M_p(S2)
          S4 = I_t(S3)
          S5 = R(S4)
          FUND(S5)
          E(S5) if not noise
        
        Zwraca raport wykonania.
        """
        
        report = {
            "object_name": obj.name,
            "t": self.time,
            "steps": {}
        }
        
        # S1: Topologia
        S1 = self.T(obj)
        report["steps"]["T"] = S1
        
        # S2: Informacja
        S2 = self.I(S1)
        report["steps"]["I"] = S2
        
        # S3: Modalność
        S3, modal_strength = self.M(obj)
        report["steps"]["M"] = (S3, modal_strength)
        
        # S4: Dynamika czasowa
        S4_I, S4_dI = self.I_t(obj)
        report["steps"]["I_t"] = (S4_I, S4_dI)
        
        # S5: Rezonans
        S5 = self.R(obj, self.field_strength)
        report["steps"]["R"] = S5
        
        # FUND: Filtr
        status = self.FUND(obj)
        report["steps"]["FUND"] = status.value
        
        # E: Emergencja
        emergence = self.E(obj)
        report["steps"]["E"] = emergence
        
        report["final_status"] = {
            "name": obj.name,
            "I": obj.I,
            "M": obj.M,
            "R": obj.R,
            "status": obj.status.value,
            "emergence": emergence
        }
        
        return report
    
    def add_object(self, obj: TimdrObject):
        """Dodaj obiekt do wszechświata"""
        self.objects[obj.name] = obj
    
    def step(self, delta_time: Optional[float] = None):
        """Wykonaj jeden krok symulacji dla całego wszechświata"""
        if delta_time is None:
            delta_time = self.dt
        
        self.time += delta_time
        
        # Aktualizuj pole
        avg_intensity = np.mean([
            obj.I for obj in self.objects.values()
        ]) if self.objects else 0.0
        
        avg_resonance = np.mean([
            obj.R for obj in self.objects.values()
        ]) if self.objects else 0.0
        
        self.field_strength = 0.6 * avg_intensity + 0.4 * avg_resonance
        
        # Wykonaj każdy obiekt
        reports = {}
        dead_objects = []
        
        for name, obj in self.objects.items():
            # Naturalny zanik
            obj.I *= (1.0 - 0.01 * delta_time)
            
            # Wykonaj
            report = self.execute(obj)
            reports[name] = report
            
            # Zbierz martwe obiekty
            if obj.I < 0.001:
                dead_objects.append(name)
        
        # Usuń martwe obiekty
        for name in dead_objects:
            del self.objects[name]
        
        return reports
    
    def run(self, steps: int = 100) -> list:
        """Uruchom symulację na N kroków"""
        history = []
        for _ in range(steps):
            reports = self.step()
            history.append({
                "time": self.time,
                "reports": reports,
                "field_strength": self.field_strength,
                "num_active": len(self.objects)
            })
        return history
    
    # ============ NARZĘDZIA POMOCNICZE ============
    
    def _get_field_dimensionality(self, field_type: str) -> int:
        """Ile wymiarów ma dane pole?"""
        dims = {
            "somatic": 3,        # ciało w 3D
            "cognitive": 5,      # myśli w wielowymiarze
            "social": 4,         # relacje 4D
            "quantum": 6,        # pole kwantowe
            "semantic": 7,       # znaczenia
        }
        return dims.get(field_type, 3)
    
    def _get_boundary_conditions(self, field_type: str) -> str:
        """Warunki brzegowe pola"""
        conditions = {
            "somatic": "periodic",       # ciało się powtarza cyklicznie
            "cognitive": "open",         # myśli są otwarte
            "social": "interactive",     # relacje interact
            "quantum": "reflective",     # falowanie
            "semantic": "dense",         # znaczenia się zagęszczają
        }
        return conditions.get(field_type, "unknown")
    
    def _modal_field_alignment(self, modality: str, field_strength: float) -> float:
        """Jak dobrze modalność M pasuje do pola?"""
        # Jeśli pole jest "gorące" (field_strength > 0.6):
        # threat i danger modalności mają wyższy alignment
        if field_strength > 0.6:
            threatening_modalities = ["threat", "danger", "fear", "loss"]
            return 0.9 if modality in threatening_modalities else 0.3
        else:
            opportunistic_modalities = ["opportunity", "gain", "curiosity", "joy"]
            return 0.9 if modality in opportunistic_modalities else 0.3
    
    def _intensity_stability(self, history: list) -> float:
        """Jak stabilna jest intensywność w historii?"""
        if len(history) < 2:
            return 0.5
        
        # Niskie wariancje = wysoka stabilność
        variance = np.var(history[-10:]) if len(history) >= 10 else np.var(history)
        stability = 1.0 / (1.0 + variance)
        return stability
    
    def _flip_modality(self, modality: str) -> str:
        """Odwróć modalność"""
        flip_map = {
            "threat": "safety",
            "opportunity": "constraint",
            "loss": "gain",
            "gain": "loss",
            "uncertainty": "certainty",
            "certainty": "uncertainty",
        }
        return flip_map.get(modality, modality)


# ============ PRZYKŁADY UŻYCIA ============

def example_anger_execution():
    """Przykład: wykonanie obiektu złości"""
    print("\n" + "="*60)
    print("EXAMPLE 1: ANGER EXECUTION")
    print("="*60)
    
    executor = FundamentalExecutor(R_min=0.3)
    
    anger = TimdrObject(
        name="anger_spike",
        T="somatic",
        I=0.85,  # wysoka intensywność
        M="threat"  # zagrożenie granicy
    )
    
    executor.add_object(anger)
    
    print(f"\nInitial: {anger}\n")
    
    for _ in range(20):
        reports = executor.step()
        if _ % 5 == 0:
            print(f"Step {_}: Field={executor.field_strength:.2f}, Anger={anger.I:.2f}, "
                  f"Status={anger.status.value}, E={anger.emergence_value}")


def example_mixed_field():
    """Przykład: wielowarstwowe pole z wieloma obiektami"""
    print("\n" + "="*60)
    print("EXAMPLE 2: MIXED FIELD (Psychology + Cognition)")
    print("="*60)
    
    executor = FundamentalExecutor()
    
    # Dodaj różne obiekty
    fear = TimdrObject("fear", T="somatic", I=0.7, M="threat")
    thought = TimdrObject("wondering", T="cognitive", I=0.6, M="uncertainty")
    curiosity = TimdrObject("curiosity", T="cognitive", I=0.5, M="opportunity")
    
    executor.add_object(fear)
    executor.add_object(thought)
    executor.add_object(curiosity)
    
    print(f"\nInitial states:")
    for name, obj in executor.objects.items():
        print(f"  {name}: I={obj.I:.2f}, M={obj.M}, R={obj.R:.2f}")
    
    print(f"\n--- Running 30 steps ---\n")
    
    for step_num in range(30):
        reports = executor.step()
        
        if step_num % 10 == 0:
            print(f"\nStep {step_num}:")
            print(f"  Field strength: {executor.field_strength:.2f}")
            print(f"  Active objects: {len(executor.objects)}")
            
            for name, obj in executor.objects.items():
                print(f"    {name}: I={obj.I:.3f}, R={obj.R:.3f}, "
                      f"status={obj.status.value}, E={obj.emergence_value}")


if __name__ == "__main__":
    example_anger_execution()
    example_mixed_field()
