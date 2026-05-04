from __future__ import annotations


def traducir_a_parametros_spotify(inferencia: dict) -> dict:
    """
    Traduce conclusiones simbólicas del motor a números y listas que entiende Spotify.
    """
    tempo_cat = inferencia["tempo"]
    energia_cat = inferencia["energia"]
    valence_cat = inferencia["valence"]
    genero_simbolico = inferencia["genero"]

    if tempo_cat == "bajo":
        min_tempo, max_tempo = 60.0, 95.0
    elif tempo_cat == "alto":
        min_tempo, max_tempo = 115.0, 145.0
    else:
        min_tempo, max_tempo = 90.0, 115.0

    mapa_energia = {"baja": 0.22, "media": 0.52, "alta": 0.88}
    mapa_valence = {"bajo": 0.22, "medio": 0.52, "alto": 0.88}
    target_energy = mapa_energia.get(energia_cat, 0.5)
    target_valence = mapa_valence.get(valence_cat, 0.5)

    mapa_generos = {
        "acoustic_ambient": ["acoustic", "ambient"],
        "pop_electronic": ["pop", "electronic"],
        "indie": ["indie-pop", "alternative"],
    }
    seed_genres = mapa_generos.get(genero_simbolico, ["indie-pop", "alternative"])

    return {
        "seed_genres": seed_genres[:5],
        "target_energy": float(target_energy),
        "target_valence": float(target_valence),
        "min_tempo": float(min_tempo),
        "max_tempo": float(max_tempo),
    }
