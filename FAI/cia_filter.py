"""
CIA TIMDER FILTER LAYER — Psychology Integration
=================================================

CIA = Compression-Interpretation-Analysis

Zastosowanie CIA filtru do warstwy psychologicznej:
  - C (Compression) = redukcja szumu, ekstraktowanie esencji
  - I (Interpretation) = modal shift, zmiana perspektywy
  - A (Analysis) = ocena, diagnostyka, predykcja

CIA filtruje psychiczne obiekty TIMDR, wyodrębniając istotne struktury
i eliminując zamieszanie sensoryczno-poznawcze.
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum


class CompressionLevel(Enum):
    """Poziomy kompresji informacji"""
    RAW = 0.0          # surowe dane
    FILTERED = 0.3     # filtrowanie szumu
    COMPRESSED = 0.6   # kompresja struktur
    ESSENTIAL = 0.85   # tylko esencja
    CRYSTALLINE = 1.0  # czysty skręt


class InterpretationScheme(Enum):
    """Schematy interpretacji (perspektywy)"""
    LITERAL = "literal"          # dosłownie
    EMOTIONAL = "emotional"      # przez emocje
    COGNITIVE = "cognitive"      # przez myśl
    SOCIAL = "social"            # przez relacje
    SURVIVAL = "survival"        # przez przetrwanie
    GROWTH = "growth"            # przez rozwój


class AnalysisMode(Enum):
    """Tryby analizy"""
    DIAGNOSTIC = "diagnostic"    # co jest nie tak?
    PREDICTIVE = "predictive"    # co będzie?
    PRESCRIPTIVE = "prescriptive"  # co robić?
    PROGNOSTIC = "prognostic"    # jaki jest prognoza?


@dataclass
class CompressedSignal:
    """
    Sygnał po kompresji CIA.
    
    Zawiera tylko istotne komponenty:
    - core_intensity: główna intensywność
    - direction: kierunek skrętu (modalność)
    - coherence: spójność sygnału
    - noise_level: ile szumu pozostało
    """
    name: str
    core_intensity: float      # 0-1, zmniejszone szumy
    direction: str             # skręt: "threat", "opportunity", itp.
    coherence: float          # jak czysta jest struktura
    noise_level: float        # ile szumu przefiltrowano
    original_intensity: float # dla porównania
    compression_ratio: float  # ile zmniejszyliśmy (0.0 - 1.0)


@dataclass
class InterpretedSignal:
    """
    Sygnał po interpretacji.
    
    Ta sama kompresja widziana z różnych perspektyw:
    - scheme: schemat interpretacji
    - meaning: co to oznacza w tym schemacie
    - valence: wartościowanie (+/-, =/ambiguous)
    - action_bias: do jakiego działania skłania
    """
    compressed: CompressedSignal
    scheme: InterpretationScheme
    meaning: str
    valence: float             # -1.0 (bad) do +1.0 (good)
    action_bias: str          # "approach", "avoid", "pause", "engage"
    confidence: float         # jak pewni jesteśmy (0-1)


@dataclass
class AnalysisResult:
    """
    Rezultat analizy CIA.
    
    Pełny raport diagnostyczno-predykcyjny:
    - mode: jaki tryb analizy
    - findings: główne odkrycia
    - risk_level: ocena ryzyka (0-1)
    - recommendation: co robić
    - probability: prawdopodobieństwo prognozy
    """
    interpreted: InterpretedSignal
    mode: AnalysisMode
    findings: Dict[str, Any]
    risk_level: float          # 0.0 (safe) do 1.0 (critical)
    recommendation: str
    probability: float
    timestamp: float


class CIAFilter:
    """
    Filtr CIA — Compression-Interpretation-Analysis.
    
    Przetwarzanie psychicznych sygnałów poprzez trzy etapy:
      1. COMPRESSION (C): Reduce noise, extract essence
      2. INTERPRETATION (I): Shift perspective, find meaning
      3. ANALYSIS (A): Diagnose, predict, prescribe
    """
    
    def __init__(self, compression_level: CompressionLevel = CompressionLevel.COMPRESSED):
        """
        compression_level: jak agresywnie kompresować (domyślnie balans)
        """
        self.compression_level = compression_level
        self.processing_history = []
    
    # ============ COMPRESSION (C) ============
    
    def compress(self, signal_name: str, intensity: float, modalité: str,
                 noise_estimate: float = 0.2) -> CompressedSignal:
        """
        C(signal) = kompresja sygnału psychicznego.
        
        Usuwamy szum, redukujemy wymiary, wyodrębniamy esencję.
        
        Args:
            signal_name: nazwa sygnału (np. "anger", "fear")
            intensity: surowa intensywność (0-1)
            modalité: modalność (kierunek skrętu)
            noise_estimate: szacunek szumu w sygnale
        
        Returns:
            CompressedSignal: oczyszczony sygnał
        """
        
        # Estymacja szumu (może pochodzić z wielopoziomowych fluktuacji)
        estimated_noise = np.random.normal(noise_estimate, 0.1)
        estimated_noise = max(0.0, min(1.0, estimated_noise))
        
        # Kompresja: usunięcie szumu
        compressed_intensity = max(0.0, intensity - estimated_noise)
        
        # Normalizacja do rozmiaru kompresji
        compression_factor = self.compression_level.value
        
        # Gdy compression_level wyższy → więcej zagęszczenia
        core_intensity = compressed_intensity * (1.0 + compression_factor * 0.5)
        core_intensity = max(0.0, min(1.0, core_intensity))
        
        # Coherence = jak dobrze sygnał zaostrzył się po kompresji
        coherence = 1.0 - estimated_noise + (compression_factor * 0.3)
        coherence = max(0.0, min(1.0, coherence))
        
        # Compression ratio = co zostało zmniejszone
        compression_ratio = estimated_noise / (intensity + 0.001)
        compression_ratio = max(0.0, min(1.0, compression_ratio))
        
        return CompressedSignal(
            name=signal_name,
            core_intensity=core_intensity,
            direction=modalité,
            coherence=coherence,
            noise_level=estimated_noise,
            original_intensity=intensity,
            compression_ratio=compression_ratio
        )
    
    # ============ INTERPRETATION (I) ============
    
    def interpret(self, compressed: CompressedSignal,
                  scheme: InterpretationScheme = InterpretationScheme.EMOTIONAL
                  ) -> InterpretedSignal:
        """
        I(compressed) = interpretacja sygnału z danej perspektywy.
        
        Ta sama kompresja ma różne znaczenia w różnych schematach.
        
        Args:
            compressed: sygnał po kompresji
            scheme: schemat interpretacji (perspektywa)
        
        Returns:
            InterpretedSignal: interpretowany sygnał
        """
        
        # Mapowanie: (kompresja + kierunek + schemat) → znaczenie + valence
        meaning_map = {
            ("threat", InterpretationScheme.EMOTIONAL): ("opasność", -0.9, "avoid"),
            ("threat", InterpretationScheme.COGNITIVE): ("challenge", -0.3, "analyze"),
            ("threat", InterpretationScheme.SURVIVAL): ("must_act", -0.8, "fight"),
            ("threat", InterpretationScheme.GROWTH): ("opportunity", 0.2, "engage"),
            
            ("opportunity", InterpretationScheme.EMOTIONAL): ("joy", 0.8, "approach"),
            ("opportunity", InterpretationScheme.COGNITIVE): ("possibility", 0.4, "explore"),
            ("opportunity", InterpretationScheme.SURVIVAL): ("resource", 0.6, "acquire"),
            ("opportunity", InterpretationScheme.GROWTH): ("potential", 0.9, "develop"),
            
            ("uncertainty", InterpretationScheme.EMOTIONAL): ("anxiety", -0.6, "pause"),
            ("uncertainty", InterpretationScheme.COGNITIVE): ("question", -0.2, "investigate"),
            ("uncertainty", InterpretationScheme.SOCIAL): ("ambiguity", -0.4, "clarify"),
            ("uncertainty", InterpretationScheme.GROWTH): ("discovery", 0.5, "explore"),
            
            ("loss", InterpretationScheme.EMOTIONAL): ("sadness", -0.8, "withdraw"),
            ("loss", InterpretationScheme.COGNITIVE): ("deficit", -0.5, "problem-solve"),
            ("loss", InterpretationScheme.GROWTH): ("lesson", -0.1, "learn"),
            
            ("gain", InterpretationScheme.EMOTIONAL): ("pride", 0.7, "engage"),
            ("gain", InterpretationScheme.COGNITIVE): ("achievement", 0.6, "consolidate"),
            ("gain", InterpretationScheme.GROWTH): ("growth", 0.9, "expand"),
            
            ("certainty", InterpretationScheme.COGNITIVE): ("clarity", 0.7, "execute"),
            ("certainty", InterpretationScheme.SURVIVAL): ("safety", 0.8, "settle"),
            ("certainty", InterpretationScheme.GROWTH): ("mastery", 0.9, "integrate"),
        }
        
        # Wyznacz znaczenie
        key = (compressed.direction, scheme)
        meaning, valence, action_bias = meaning_map.get(
            key,
            ("unknown", 0.0, "pause")
        )
        
        # Confidence = jak dobrze schemat pasuje do sygnału
        # Wysoka coherence sygnału + dobry matching = wysoka confidence
        scheme_match = 0.7 if key in meaning_map else 0.3
        confidence = compressed.coherence * scheme_match
        
        return InterpretedSignal(
            compressed=compressed,
            scheme=scheme,
            meaning=meaning,
            valence=valence,
            action_bias=action_bias,
            confidence=confidence
        )
    
    # ============ ANALYSIS (A) ============
    
    def analyze(self, interpreted: InterpretedSignal,
                mode: AnalysisMode = AnalysisMode.DIAGNOSTIC,
                context: Optional[Dict] = None) -> AnalysisResult:
        """
        A(interpreted) = analiza — diagnoza, predykcja, rekomendacja.
        
        Args:
            interpreted: sygnał po interpretacji
            mode: tryb analizy (diagnostic, predictive, etc.)
            context: kontekst dodatkowy
        
        Returns:
            AnalysisResult: pełny raport analizy
        """
        
        context = context or {}
        
        # Risk assessment
        risk_level = self._assess_risk(interpreted, context)
        
        # Findings
        findings = self._extract_findings(interpreted)
        
        # Recommendation
        recommendation = self._formulate_recommendation(
            interpreted, mode, risk_level
        )
        
        # Probability (dla trybu predictive)
        probability = self._estimate_probability(interpreted, mode)
        
        return AnalysisResult(
            interpreted=interpreted,
            mode=mode,
            findings=findings,
            risk_level=risk_level,
            recommendation=recommendation,
            probability=probability,
            timestamp=0.0  # będzie ustawione przez system
        )
    
    def _assess_risk(self, interpreted: InterpretedSignal,
                     context: Dict) -> float:
        """Ocena poziomu ryzyka sygnału"""
        base_risk = -interpreted.valence  # negatywna valence = wyższe ryzyko
        
        # Intensywność wzmacnia ryzyko
        intensity_factor = interpreted.compressed.core_intensity * 0.5
        
        # Niska coherence = wyższe ryzyko (sygnał chaotyczny)
        coherence_penalty = (1.0 - interpreted.compressed.coherence) * 0.3
        
        risk = (base_risk + intensity_factor + coherence_penalty) / 2.0
        risk = max(0.0, min(1.0, risk))
        
        return risk
    
    def _extract_findings(self, interpreted: InterpretedSignal) -> Dict:
        """Wyodrębnienie głównych odkryć"""
        return {
            "signal_name": interpreted.compressed.name,
            "core_meaning": interpreted.meaning,
            "valence": interpreted.valence,
            "action_bias": interpreted.action_bias,
            "compression_ratio": interpreted.compressed.compression_ratio,
            "coherence": interpreted.compressed.coherence,
            "confidence": interpreted.confidence,
            "scheme": interpreted.scheme.value,
        }
    
    def _formulate_recommendation(self, interpreted: InterpretedSignal,
                                  mode: AnalysisMode,
                                  risk_level: float) -> str:
        """Sformułowanie rekomendacji"""
        
        if mode == AnalysisMode.DIAGNOSTIC:
            if risk_level > 0.7:
                return f"⚠️  DIAGNOZA: Wysoki {interpreted.compressed.name} ({risk_level:.1%}). Wymaga natychmiastowej interwencji."
            elif risk_level > 0.4:
                return f"⚠️  DIAGNOZA: Umiarkowany {interpreted.meaning}. Monitoruj sytuację."
            else:
                return f"✓ DIAGNOZA: {interpreted.meaning.capitalize()} w normie."
        
        elif mode == AnalysisMode.PREDICTIVE:
            action = interpreted.action_bias
            if risk_level > 0.6:
                return f"📊 PROGNOZA: Prawdopodobnie {action} (z ryzykiem). Przygotuj się na zmianę."
            else:
                return f"📊 PROGNOZA: Stabilny trend {action}."
        
        elif mode == AnalysisMode.PRESCRIPTIVE:
            return f"💊 PRZEPIS: Wykonaj '{interpreted.action_bias}' zamiast '{self._opposite_action(interpreted.action_bias)}'. Confidence: {interpreted.confidence:.1%}"
        
        elif mode == AnalysisMode.PROGNOSTIC:
            outlook = "polepszająca się" if interpreted.valence > 0 else "pogarszająca się"
            return f"🔮 PROGNOZA: Perspektywa {outlook}. Ryzyko długoterminowe: {risk_level:.1%}"
        
        return "❓ REKOMENDACJA: Wymaga ręcznej analizy"
    
    def _estimate_probability(self, interpreted: InterpretedSignal,
                              mode: AnalysisMode) -> float:
        """Estymacja prawdopodobieństwa prognozy"""
        # Bazuj na confidence i coherence
        base_prob = interpreted.confidence * interpreted.compressed.coherence
        
        # Dla trybu predictive, dodaj korektę intensywności
        if mode == AnalysisMode.PREDICTIVE:
            intensity_factor = interpreted.compressed.core_intensity * 0.2
            return base_prob + intensity_factor
        
        return base_prob
    
    def _opposite_action(self, action: str) -> str:
        """Znaj przeciwny kierunek działania"""
        opposites = {
            "approach": "avoid",
            "avoid": "approach",
            "engage": "withdraw",
            "withdraw": "engage",
            "explore": "settle",
            "settle": "explore",
            "execute": "pause",
            "pause": "execute",
        }
        return opposites.get(action, "nothing")
    
    # ============ PEŁNY PRZEPŁYW CIA ============
    
    def process(self, signal_name: str, intensity: float, modality: str,
                noise_estimate: float = 0.2,
                interpretation_scheme: InterpretationScheme = InterpretationScheme.EMOTIONAL,
                analysis_mode: AnalysisMode = AnalysisMode.DIAGNOSTIC,
                context: Optional[Dict] = None) -> AnalysisResult:
        """
        Pełny przepływ CIA: Compression → Interpretation → Analysis
        
        Returns:
            AnalysisResult: gotowy raport z rekomendacją
        """
        
        # C: Kompresja
        compressed = self.compress(signal_name, intensity, modality, noise_estimate)
        
        # I: Interpretacja
        interpreted = self.interpret(compressed, interpretation_scheme)
        
        # A: Analiza
        result = self.analyze(interpreted, analysis_mode, context)
        
        # Zapisz w historii
        self.processing_history.append(result)
        
        return result


# ============ PRAKTYCZNE PRZYKŁADY ============

def example_anxiety_filter():
    """Przykład: filtrowanie sygnału lęku przez CIA"""
    print("\n" + "="*70)
    print("EXAMPLE 1: ANXIETY THROUGH CIA FILTER")
    print("="*70)
    
    filter_cia = CIAFilter(compression_level=CompressionLevel.COMPRESSED)
    
    # Surowy sygnał lęku z dużo szumem
    print("\n1️⃣  RAW SIGNAL:")
    print("   Name: 'anxiety'")
    print("   Intensity: 0.75 (wysoki lęk z zamieszaniem)")
    print("   Modality: 'uncertainty'")
    print("   Noise estimate: 0.35 (dużo szumu sensoryczno-poznawczego)")
    
    # Przetwarzanie przez CIA
    result_diagnostic = filter_cia.process(
        signal_name="anxiety",
        intensity=0.75,
        modality="uncertainty",
        noise_estimate=0.35,
        interpretation_scheme=InterpretationScheme.COGNITIVE,
        analysis_mode=AnalysisMode.DIAGNOSTIC
    )
    
    print("\n2️⃣  COMPRESSED:")
    c = result_diagnostic.interpreted.compressed
    print(f"   Core intensity: {c.core_intensity:.2f} (oczyszczony)")
    print(f"   Coherence: {c.coherence:.2f} (czystość struktury)")
    print(f"   Noise removed: {c.compression_ratio:.1%}")
    
    print("\n3️⃣  INTERPRETED:")
    i = result_diagnostic.interpreted
    print(f"   Meaning: {i.meaning}")
    print(f"   Valence: {i.valence:+.2f} (ujemna = zagrażająca)")
    print(f"   Action bias: {i.action_bias}")
    print(f"   Confidence: {i.confidence:.1%}")
    
    print("\n4️⃣  ANALYSIS (Diagnostic):")
    print(f"   Risk level: {result_diagnostic.risk_level:.1%}")
    print(f"   Recommendation: {result_diagnostic.recommendation}")
    
    # Teraz spróbuj innego schematu (growth perspective)
    print("\n" + "-"*70)
    print("Zmiana perspektywy: GROWTH SCHEME")
    print("-"*70)
    
    result_growth = filter_cia.process(
        signal_name="anxiety",
        intensity=0.75,
        modality="uncertainty",
        noise_estimate=0.35,
        interpretation_scheme=InterpretationScheme.GROWTH,
        analysis_mode=AnalysisMode.PRESCRIPTIVE
    )
    
    print(f"\n   Same signal, different meaning:")
    print(f"   Meaning: {result_growth.interpreted.meaning}")
    print(f"   Valence: {result_growth.interpreted.valence:+.2f} (pozytywna = szansa)")
    print(f"   Action: {result_growth.interpreted.action_bias}")
    print(f"\n   Recommendation: {result_growth.recommendation}")


def example_mixed_signals():
    """Przykład: filtrowanie wielowarstwowych sygnałów"""
    print("\n" + "="*70)
    print("EXAMPLE 2: MIXED SIGNALS THROUGH CIA")
    print("="*70)
    
    filter_cia = CIAFilter(compression_level=CompressionLevel.ESSENTIAL)
    
    signals = [
        ("anger", 0.85, "threat", 0.2),
        ("curiosity", 0.60, "opportunity", 0.15),
        ("confusion", 0.70, "uncertainty", 0.40),
    ]
    
    print("\nPrzetwarzanie sygnałów przez CIA z maximalna kompresją:\n")
    
    for name, intensity, modality, noise in signals:
        result = filter_cia.process(
            signal_name=name,
            intensity=intensity,
            modality=modality,
            noise_estimate=noise,
            interpretation_scheme=InterpretationScheme.EMOTIONAL,
            analysis_mode=AnalysisMode.DIAGNOSTIC
        )
        
        c = result.interpreted.compressed
        i = result.interpreted
        
        print(f"📍 {name.upper()}:")
        print(f"   Raw: {intensity:.2f} → Compressed: {c.core_intensity:.2f} "
              f"(removed {c.compression_ratio:.1%})")
        print(f"   Meaning: {i.meaning} | Valence: {i.valence:+.2f}")
        print(f"   Risk: {result.risk_level:.1%} | Confidence: {i.confidence:.1%}")
        print()


def example_predictive_analysis():
    """Przykład: analiza predykcyjna"""
    print("\n" + "="*70)
    print("EXAMPLE 3: PREDICTIVE ANALYSIS")
    print("="*70)
    
    filter_cia = CIAFilter()
    
    print("\nPrognozowanie behawiorów na podstawie sygnałów:\n")
    
    # Scenariusz 1: Zagrożenie (threat)
    result_threat = filter_cia.process(
        signal_name="threat_detection",
        intensity=0.9,
        modality="threat",
        noise_estimate=0.1,
        interpretation_scheme=InterpretationScheme.SURVIVAL,
        analysis_mode=AnalysisMode.PREDICTIVE
    )
    
    print("1️⃣  SCENARIO: Zagrożenie Fizyczne")
    print(f"   {result_threat.recommendation}")
    print(f"   Probability: {result_threat.probability:.1%}")
    
    # Scenariusz 2: Oportunizm (opportunity)
    result_opportunity = filter_cia.process(
        signal_name="opportunity_detection",
        intensity=0.8,
        modality="opportunity",
        noise_estimate=0.1,
        interpretation_scheme=InterpretationScheme.GROWTH,
        analysis_mode=AnalysisMode.PREDICTIVE
    )
    
    print("\n2️⃣  SCENARIO: Okazja do Wzrostu")
    print(f"   {result_opportunity.recommendation}")
    print(f"   Probability: {result_opportunity.probability:.1%}")


if __name__ == "__main__":
    example_anxiety_filter()
    example_mixed_signals()
    example_predictive_analysis()
