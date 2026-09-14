```mermaid
graph TD
    %% Definicja stylów
    classDef core fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#fff;
    classDef resonance fill:#ecc94b,stroke:#d69e2e,stroke-width:2px,color:#000;
    classDef field fill:#3182ce,stroke:#2b6cb0,stroke-width:2px,color:#fff;

    subgraph Skala Makro [1. Skala Makro: NGC 7075]
        A[Jądro Galaktyki / Główny Atraktor] -->|Strumień Materii i Energii| B[Geometria Pola Helisy]
    end

    subgraph Skala Atomowa [2. Skala Atomowa: Punkt Zwrotny]
        B -->|Coupling / Sprzężenie| C[Sygnał Helu: Rezonans i Stabilność]
    end

    subgraph Skala Kwantowo-Inżynieryjna [3. Skala Kwantowo-Inżynieryjna]
        C -->|Sztuczna Koniunkcja Pola| D[Generowanie Asymetrycznego Pędu]
    end

    %% Przypisanie klas
    class A,B field;
    class C resonance;
    class D core;
