import yaml


def load_model(path: str = "model.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


def print_model(model):
    model_info = model.get("MODEL", {})
    states = model.get("STATES", [])
    transitions = model.get("TRANSITIONS", [])

    print("=== MODEL ===")
    print("Stany:", model_info.get("STATES"))
    print("Typ przejść:", model_info.get("TRANSITIONS"))
    print("Wersja:", model_info.get("VERSION"))
    print()

    print("=== STANY ===")
    for s in states:
        print(f"- SYMBOL: {s.get('SYMBOL')}, NAME: {s.get('NAME')}, "
              f"ROLE: {s.get('ROLE')}, CODE: {s.get('CODE')}")
    print()

    print("=== PRZEJŚCIA ===")
    for t in transitions:
        print(f"- FROM: {t.get('FROM')}, TO: {t.get('TO')}, CODE: {t.get('CODE')}")
    print()


def train_model(model):
    """
    Miejsce na dalszą implementację uczenia modelu.
    Tutaj można wpiąć logikę AI, która korzysta z:
    - listy stanów,
    - przejść,
    - kodów binarnych.
    """
    pass


if __name__ == "__main__":
    model = load_model("model.yaml")
    print_model(model)
    # Tu w przyszłości można odkomentować:
    # train_model(model)
