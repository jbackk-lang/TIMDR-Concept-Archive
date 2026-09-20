"""
WARSTWA PSYCHOLOGICZNA — FAI Psychology Layer
============================================

Psychologia jako obiekty TIMDR.
Każdy proces psychiczny (emocja, myśl, schemat, impuls) jest obiektem
spełniającym warunki FUNDAMENTAL:
  - T: pole (somatyczno-poznawcze, sytuacyjne, społeczne)
  - I: informacja (sygnał, dane, percepcja)
  - M: modalność (interpretacja, skręt perspektywy)
  - I(t): dynamika czasowa (narastanie, wygasanie, cykl)
  - R: rezonans (spójność z polem i sobą)
  - E: emergencja (działanie, decyzja, behawior)

"""

import numpy as np
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum


class FieldType(Enum):
    """Typy pól, na których operuje psychika"""
    SOMATIC = "somatic"          # ciało, emocje somatyczne
    COGNITIVE = "cognitive"      # myśli, schematy, reprezentacje
    SOCIAL = "social"            # relacje, percepcja społeczna
    TEMPORAL = "temporal"        # czas, przyszłość, przeszłość
    ENVIRONMENT = "environment"  # kontekst, sytuacja


class PsychologicalModalityType(Enum):
    """Typy skrętów modalności (M) — interpretacje"""
    THREAT = "threat"            # zagrożenie
    OPPORTUNITY = "opportunity"  # szansa
    LOSS = "loss"                # strata
    GAIN = "gain"                # zysk
    UNCERTAINTY = "uncertainty"  # niepewność
    CERTAINTY = "certainty"      # pewność


@dataclass
class PsychologicalObject:
    """
    Podstawowy obiekt psychiczny w modelu TIMDR.
    
    Atrybuty:
    - name: nazwa (np. "złość", "strach", "ciekawość")
    - T: pole (typ pola, na którym obiekt istnieje)
    - I: surowa informacja (sygnał, wartość)
    - M: modalność (interpretacja)
    - t_onset: moment pojawienia się
    - t_duration: jak długo trwa
    - R: rezonans (0.0 - 1.0, spójność z polem)
    - E_state: stan emergencji (co to generuje)
    """
    
    name: str
    field: FieldType
    signal_intensity: float  # I — intensywność sygnału (0.0 - 1.0)
    modality: PsychologicalModalityType  # M — jak to się interpretuje
    resonance: float = 0.5  # R — spójność (0.0 - 1.0)
    t_current: float = 0.0  # I(t) — czas obecny
    t_duration: float = 1.0  # jak długo żyje obiekt
    decay_rate: float = 0.01  # jak szybko się rozpada
    
    def __post_init__(self):
        self.history = []  # ślad czasowy
        self.emergence_value = None  # E — co wyłania się
        
    def evaluate_resonance(self, field_strength: float) -> float:
        """
        R(X) = rezonans X z polem.
        Obiekt ma wysokie R, jeśli jego modalność pasuje do pola.
        """
        # Przykład: jeśli pole mówi THREAT a modalność też THREAT → R wysoki
        # R = R_base * field_alignment * (1 - noise)
        
        alignment = 0.8 if self._modality_field_match(field_strength) else 0.2
        internal_coherence = 1.0 - abs(self.signal_intensity - 0.5) * 0.2
        
        self.resonance = 0.6 * alignment + 0.4 * internal_coherence
        return self.resonance
    
    def _modality_field_match(self, field_strength: float) -> bool:
        """Czy modalność pasuje do pola?"""
        # Uproszczona heurystyka
        if field_strength > 0.6:
            return self.modality in [
                PsychologicalModalityType.THREAT,
                PsychologicalModalityType.LOSS,
                PsychologicalModalityType.UNCERTAINTY
            ]
        else:
            return self.modality in [
                PsychologicalModalityType.OPPORTUNITY,
                PsychologicalModalityType.GAIN,
                PsychologicalModalityType.CERTAINTY
            ]
    
    def update_intensity(self, delta_time: float):
        """
        ΔI(X) = zmiana intensywności w czasie
        Sygnał zanika z prędkością decay_rate
        """
        self.signal_intensity *= (1.0 - self.decay_rate * delta_time)
        self.t_current += delta_time
        self.history.append(self.signal_intensity)
        
        if self.signal_intensity < 0.01:
            self.signal_intensity = 0.0
    
    def compute_emergence(self) -> Optional[str]:
        """
        E(S) = emergencja: co wyłania się z konfiguracji?
        Jeśli R > R_min i I > 0: generujemy behawior
        """
        R_min = 0.3
        
        if self.resonance > R_min and self.signal_intensity > 0.1:
            # Emergencja = odpowiedź behawioralna
            if self.modality == PsychologicalModalityType.THREAT:
                self.emergence_value = "flight_or_fight"
            elif self.modality == PsychologicalModalityType.OPPORTUNITY:
                self.emergence_value = "approach"
            elif self.modality == PsychologicalModalityType.LOSS:
                self.emergence_value = "withdrawal"
            elif self.modality == PsychologicalModalityType.GAIN:
                self.emergence_value = "engagement"
            elif self.modality == PsychologicalModalityType.UNCERTAINTY:
                self.emergence_value = "exploration"
            elif self.modality == PsychologicalModalityType.CERTAINTY:
                self.emergence_value = "execution"
            
            return self.emergence_value
        
        return None


@dataclass
class Emotion(PsychologicalObject):
    """
    Emocja = obiekt psychiczny o szybkiej dynamice i wysokiej modalności.
    
    Emocje zapalają się szybko (narastanie), trwają średnio,
    i zanikają szybko (wygasanie).
    """
    
    def __init__(self, name: str, field: FieldType, signal: float, 
                 modality: PsychologicalModalityType):
        super().__init__(
            name=name,
            field=field,
            signal_intensity=signal,
            modality=modality,
            t_duration=2.0,  # emocje trwają krótko
            decay_rate=0.05  # ale szybko zanikają
        )


@dataclass
class Thought(PsychologicalObject):
    """
    Myśl = gest semantyczny + konfiguracja znaczeń.
    
    Myśli są mediumem dla schematów i impulsu.
    Operują na poziomie reprezentacji (nie ciała).
    """
    
    def __init__(self, name: str, content: str, field: FieldType,
                 modality: PsychologicalModalityType):
        super().__init__(
            name=name,
            field=field,
            signal_intensity=0.6,  # myśli startują z średnią intensywnością
            modality=modality,
            t_duration=5.0,  # myśli żyją dłużej
            decay_rate=0.01  # i zanikają powoli
        )
        self.content = content  # reprezentacja myśli
        self.semantic_links = []  # powiązania z innymi myślami


@dataclass
class Schema(PsychologicalObject):
    """
    Schemat = trwały obiekt o wysokim R, powtarzalny w czasie.
    
    Schematy to szablony, heurystyki, nawykowości.
    Stabilne, autonomiczne, działają w tle.
    """
    
    def __init__(self, name: str, pattern: str, field: FieldType):
        super().__init__(
            name=name,
            field=field,
            signal_intensity=0.3,  # schematy działają w tle
            modality=PsychologicalModalityType.CERTAINTY,  # są "pewne"
            t_duration=np.inf,  # trwają bardzo długo
            decay_rate=0.0001  # prawie się nie zmieniają
        )
        self.pattern = pattern  # wzorzec behawioralny
        self.activation_count = 0  # ile razy został aktywowany


@dataclass
class Impulse(PsychologicalObject):
    """
    Impuls = konfiguracja o niskim R, szybka, nietrwała.
    
    Impulsy to przecinające się bodźce, fluktuacje,
    krótkie akumulacje energii.
    """
    
    def __init__(self, name: str, field: FieldType, 
                 modality: PsychologicalModalityType, intensity: float):
        super().__init__(
            name=name,
            field=field,
            signal_intensity=intensity,  # może być wysoki
            modality=modality,
            t_duration=0.5,  # bardzo krótki
            decay_rate=0.2  # szybkie zanikanie
        )


class PsychologicalField:
    """
    Pole psychologiczne = konfiguracja wszystkich aktywnych obiektów psychicznych
    w danym momencie.
    """
    
    def __init__(self):
        self.objects: Dict[str, PsychologicalObject] = {}
        self.field_strength: float = 0.5  # ogólna "temperatura" pola
        self.time: float = 0.0
        
    def add_object(self, obj: PsychologicalObject):
        """Dodaj obiekt psychiczny do pola"""
        self.objects[obj.name] = obj
        
    def remove_object(self, name: str):
        """Usuń obiekt (gdy zanika)"""
        if name in self.objects:
            del self.objects[name]
    
    def update(self, delta_time: float):
        """
        Aktualizuj całe pole psychologiczne.
        - aktualizuj intensywności każdego obiektu
        - policz rezonanse
        - usuń martwe obiekty
        """
        self.time += delta_time
        
        # Aktualizuj każdy obiekt
        dead_objects = []
        for name, obj in self.objects.items():
            obj.update_intensity(delta_time)
            obj.evaluate_resonance(self.field_strength)
            
            if obj.signal_intensity == 0.0:
                dead_objects.append(name)
        
        # Usuń martwe obiekty
        for name in dead_objects:
            self.remove_object(name)
        
        # Policz ogólną „temperaturę" pola
        if self.objects:
            avg_intensity = np.mean([
                obj.signal_intensity for obj in self.objects.values()
            ])
            avg_resonance = np.mean([
                obj.resonance for obj in self.objects.values()
            ])
            self.field_strength = 0.5 * avg_intensity + 0.5 * avg_resonance
        else:
            self.field_strength *= 0.95  # rozpada się, gdy puste
    
    def get_emergences(self) -> Dict[str, str]:
        """
        Zbierz wszystkie emergencje z pola.
        E(S) = co się wyłania z całej konfiguracji?
        """
        emergences = {}
        for name, obj in self.objects.items():
            e = obj.compute_emergence()
            if e:
                emergences[name] = e
        return emergences
    
    def state_summary(self) -> Dict:
        """Podsumowanie stanu całego pola"""
        return {
            "time": self.time,
            "field_strength": self.field_strength,
            "active_objects": len(self.objects),
            "objects_detail": {
                name: {
                    "intensity": obj.signal_intensity,
                    "resonance": obj.resonance,
                    "modality": obj.modality.value,
                    "emergence": obj.compute_emergence()
                }
                for name, obj in self.objects.items()
            }
        }


# ============= PRZYKŁADY =============

def example_anger():
    """
    Przykład: złość
    T → ciało + sytuacja
    I → pobudzenie + kierunek (zagrożenie granic)
    M → interpretacja: agresja / obrona
    I(t) → narastanie w ciągu 1-2 sekund
    R → jak adekwatna do sytuacji?
    E → działanie: walka / komunikat / impuls agresji
    """
    anger = Emotion(
        name="anger",
        field=FieldType.SOMATIC,
        signal=0.8,  # wysoka intensywność
        modality=PsychologicalModalityType.THREAT  # interpretacja: zagrożenie
    )
    
    field = PsychologicalField()
    field.add_object(anger)
    
    print("=== ANGER (złość) ===")
    for t in np.linspace(0, 5, 50):
        field.update(0.1)
        if t % 1.0 < 0.1:
            print(f"t={t:.1f}: {field.state_summary()}")
    
    print(f"\nEmergence: {field.get_emergences()}\n")


def example_curiosity():
    """
    Przykład: ciekawość
    T → pole poznawcze
    I → brak wiedzy (informacja o braku informacji)
    M → interpretacja: oportunizm / odkrycie
    I(t) → podtrzymywane przez eksplorację
    R → rezonans z polem wiedzy
    E → eksploracja / pytania / badanie
    """
    curiosity = Thought(
        name="curiosity",
        content="co to jest?",
        field=FieldType.COGNITIVE,
        modality=PsychologicalModalityType.UNCERTAINTY
    )
    
    field = PsychologicalField()
    field.add_object(curiosity)
    
    print("=== CURIOSITY (ciekawość) ===")
    for t in np.linspace(0, 5, 50):
        field.update(0.1)
        if t % 1.0 < 0.1:
            print(f"t={t:.1f}: {field.state_summary()}")
    
    print(f"\nEmergence: {field.get_emergences()}\n")


def example_fear():
    """
    Przykład: strach
    T → pole zagrożenia
    I → sygnał niebezpieczeństwa
    M → interpretacja: zagrożenie egzystencjalne
    I(t) → szybkie narastanie, długa utrzymywanie
    R → wysoki rezonans w polu zagrożenia
    E → ucieczka / paraliż / agresja defensywna
    """
    fear = Emotion(
        name="fear",
        field=FieldType.SOMATIC,
        signal=0.9,
        modality=PsychologicalModalityType.THREAT
    )
    
    field = PsychologicalField()
    field.add_object(fear)
    
    print("=== FEAR (strach) ===")
    for t in np.linspace(0, 8, 80):
        field.update(0.1)
        if t % 1.0 < 0.1:
            print(f"t={t:.1f}: {field.state_summary()}")
    
    print(f"\nEmergence: {field.get_emergences()}\n")


if __name__ == "__main__":
    example_anger()
    example_curiosity()
    example_fear()
