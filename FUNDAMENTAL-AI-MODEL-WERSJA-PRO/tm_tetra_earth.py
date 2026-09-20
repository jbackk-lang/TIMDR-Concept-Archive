# tm_tetra_earth.py
# Operator tetraedru z rotacją jak Ziemia

class TetraEarthOperator:
    """
    Operator tetraedru z rotacją jak Ziemia.
    Każdy stan ma kąt (0, 90, 180, 270).
    Obrót = przesunięcie kąta (jak obrót Ziemi).
    """

    def __init__(self):
        # 4 stany modalne przypisane do kątów
        self.angles = {
            0:  "A",   # np. "południk 0°"
            90: "B",
            180:"C",
            270:"D"
        }
        self.current_angle = 0  # start: 0°

    def _normalize(self, angle):
        return angle % 360

    def rotate(self, direction, step=90):
        """
        direction: 'E' (wschód) lub 'W' (zachód)
        step: krok obrotu w stopniach (domyślnie 90°)
        """
        if direction == "E":
            self.current_angle = self._normalize(self.current_angle + step)
        elif direction == "W":
            self.current_angle = self._normalize(self.current_angle - step)
        return self.angles[self.current_angle]

    def transform(self, x, direction="E", step=90):
        """
        Transformacja sygnału x przez aktualny stan tetraedru
        z rotacją jak Ziemia.
        """
        state = self.rotate(direction, step=step)
        return f"{state}:{x}"
