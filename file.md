flowchart LR
    %% Styles and configuration
    classDef default fill:#2d3748,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef source fill:#2c5282,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef process fill:#2d3748,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef api fill:#3182ce,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef cache fill:#2b6cb0,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef decision fill:#2c5282,stroke:#e2e8f0,stroke-width:2px,color:#e2e8f0
    classDef endpoint fill:#2b6cb0,stroke:#e2e8f0,stroke-width:3px,color:#e2e8f0

    subgraph Data_Extraction ["Data Extraction Layer"]
        A[("Hybris Data Source")]
        B1["Extract Order Data"]
        B2["Extract POS Data"]
        A --> B1
        A --> B2
    end

    subgraph Data_Processing ["Data Processing Layer"]
        C1["Order Data with Address"]
        C2["POS Data with Coordinates"]
        D["Geocode Addresses"]
        E{"Cache\nCheck"}
        F1["Use Cached\nData"]
        F2["Call Google\nGeocoding API"]
    end

    subgraph Distance_Calculation ["Distance Calculation Layer"]
        G["Order Data with\nGeo-coordinates"]
        H["Apply Haversine\nFormula"]
        I["Closest POS by\nDistance"]
        J["Google Distance\nMatrix API"]
        K[("Final Drivable\nDistance")]
    end

    %% Connections between subgraphs
    B1 --> C1
    B2 --> C2
    C1 --> D
    D --> E
    E -->|"Cache Hit"| F1
    E -->|"Cache Miss"| F2
    F1 --> G
    F2 --> G
    G --> H
    C2 --> H
    H --> I
    I --> J
    G --> J
    J --> K

    %% Apply styles
    class A,K endpoint
    class B1,B2,C1,C2 source
    class D,H,I process
    class F2,J api
    class F1 cache
    class E decision

    %% Style subgraphs
    style Data_Extraction fill:#1a202c,stroke:#4a5568,stroke-width:2px,color:#e2e8f0
    style Data_Processing fill:#1a202c,stroke:#4a5568,stroke-width:2px,color:#e2e8f0
    style Distance_Calculation fill:#1a202c,stroke:#4a5568,stroke-width:2px,color:#e2e8f0
