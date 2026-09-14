import numpy as np
import math

class AstroTIMDRConnector:
    def __init__(self):
        # Parametry tła i emisji z projektu astro-map (2MASS i ROSAT)
        self.base_galaxy_density_2mass = 1024.0  # Referencyjna gęstość tła (struktura Lambda)
        self.xray_bubble_energy_rosat = 256.0    # Emisja rentgenowska (projekcja Rho)

    def generate_astro_entropy_curve(self, steps=300):
        """Generuje profil entropii na podstawie interferencji 2MASS + ROSAT."""
        t_values = np.linspace(0, 4 * np.pi, steps)  # Cykl 720 stopni dla podwójnego domknięcia M^2
        
        angles = np.degrees(t_values)
        delta_S_profile = []
        
        # Logarytmiczny fundament entropii wejściowej z astrofizycznych map
        lambda_entropy = math.log2(self.base_galaxy_density_2mass)
        rho_entropy_base = math.log2(self.xray_bubble_energy_rosat)

        for t in t_values:
            # 1. Modelowanie interferencji toroidalnej (płaty energii North/South bubble)
            # Toroidalny skręt wokół centrum Galaktyki (charakter Möbiusa z astro-map)
            galaxy_twist_interference = np.cos(3 * t) * np.sin(2 * t)
            
            # 2. Dynamiczne wyliczenie zmiennej entropii końcowej pod wpływem skrętu tau
            dynamic_rho_entropy = rho_entropy_base + galaxy_twist_interference
            
            # 3. Klasyczne równanie dywergencji Delta S modelu TIMDR
            delta_S = dynamic_rho_entropy - lambda_entropy
            
            # Uwzględnienie ujemnej kompresji topologicznej w punkcie skrętu nieskończoności (∞)
            compression_effect = -0.3 * (t / (2 * np.pi))
            delta_S_profile.append(delta_S + compression_effect)
            
        return angles, delta_S_profile

# Uruchomienie kalkulatora danych astrofizycznych
connector = AstroTIMDRConnector()
angles, delta_S = connector.generate_astro_entropy_curve()
