class TIMDERLayers:
    """
    Warstwy Λ–τ–ρ (nazwy wzięte z szerszego słownika projektów TIMDR:
    struktura / transformacja / defekt).

    UCZCIWA UWAGA (dodana po audycie): to są trzy proste, celowo odwracalne
    operacje arytmetyczne (+1, *2, +i mod 3) - NIE jest to żadna realna
    struktura geometryczna, operator torsji czy detektor defektu w
    znaczeniu, jakim te słowa mają w innych repozytoriach z rodziny TIMDR
    (np. rzeczywista geometria skrętu Boerdijk-Coxeter, albo operator
    Freneta-Serreta). Nazwy Λ/τ/ρ zostały tu zachowane dla ciągłości
    słownika projektu i czytelności kroków w README, ale świadomie NIE
    twierdzimy, że te trzy metody realizują jakąkolwiek głębszą strukturę
    matematyczną poza własną odwracalnością (którą testy w
    `tests/test_timdera_roundtrip.py` faktycznie sprawdzają). Jeśli w
    przyszłości ktoś chce nadać tym warstwom realną geometryczną treść,
    trzeba dopisać właściwe definicje, a nie tylko dopasować nazwę.
    """

    def apply_structure(self, data):
        return [x + 1 for x in data]

    def reverse_structure(self, data):
        return [x - 1 for x in data]

    def apply_transform(self, data):
        return [x * 2 for x in data]

    def reverse_transform(self, data):
        return [x // 2 for x in data]

    def apply_defect(self, data):
        return [x + (i % 3) for i, x in enumerate(data)]

    def reverse_defect(self, data):
        return [x - (i % 3) for i, x in enumerate(data)]
