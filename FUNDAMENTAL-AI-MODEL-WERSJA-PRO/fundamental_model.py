# FUNDAMENTAL AI MODEL — WERSJA PRO
# Autor: Jacek Kielich
# Model koncepcyjny Λ–τ–ρ (Topologia, Transformacja, Rezonans)
# MIT License

from tm_concept import ConceptLayer
from tm_information import InformationLayer
from tm_emergent import EmergentLayer
from tm_or import OrientationLayer
from tm_topo_generator_double_mobius import TopoGenerator
from tm_tetra_earth import TetraEarthOperator


class FundamentalAIModel:
    """
    Model bazowy dla architektury Λ–τ–ρ.
    Opisuje przepływ informacji przez warstwy:
    T → I → M → It → R → E
    """

    def __init__(self):
        # Inicjalizacja warstw
        self.orientation = OrientationLayer()
        self.concept = ConceptLayer()
        self.info = InformationLayer()
        self.mobius = TetraEarthOperator()   # NOWA WARSTWA M
        self.emergent = EmergentLayer()
        self.generator = TopoGenerator()

    def process(self, signal):
        """
        Główny pipeline modelu.
        Przetwarza sygnał przez kolejne warstwy TIMDR.
        """
        # T — Topologia (określenie struktury)
        t = self.concept.embed(signal)

        # I — Informacja (wydobycie treści)
        i = self.info.extract(t)

        # M — Modalność (tetraeder z rotacją jak Ziemia)
        m = self.mobius.transform(i, direction="E")

        # It — Informacja czasowa (rozszerzenie w czasie)
        it = self.orientation.expand(m)

        # R — Rezonans (stabilizacja i filtracja)
        r = self.generator.resonate(it)

        # E — Emergentja (stabilizacja struktury)
        e = self.emergent.stabilize(r)

        return e


if __name__ == "__main__":
    model = FundamentalAIModel()
    test_signal = "Λ–τ–ρ test"
    output = model.process(test_signal)
    print("Wynik modelu:", output)
