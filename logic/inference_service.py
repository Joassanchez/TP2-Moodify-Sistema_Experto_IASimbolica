from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    from pyswip import Prolog
except ImportError:
    Prolog = None  # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent
REGLAS_PATH = BASE_DIR / "reglas.pl"

OPCIONES_ESTADO = ("melancolico", "neutro", "alegre")
OPCIONES_CLIMA = ("lluvioso", "nublado", "soleado")
OPCIONES_HORARIO = ("manana", "tarde", "noche")

LABEL_ESTADO = {
    "melancolico": "Melancólico",
    "neutro": "Neutro",
    "alegre": "Alegre",
}
LABEL_CLIMA = {
    "lluvioso": "Lluvioso",
    "nublado": "Nublado",
    "soleado": "Soleado",
}
LABEL_HORARIO = {
    "manana": "Mañana",
    "tarde": "Tarde",
    "noche": "Noche",
}


def _inicializar_prolog() -> Any:
    """Carga reglas.pl en el motor Prolog."""
    if Prolog is None:
        raise RuntimeError(
            "PySwip no está instalado. Ejecute: pip install pyswip. "
            "Además necesita SWI-Prolog instalado en el sistema (https://www.swi-prolog.org/)."
        )
    if not REGLAS_PATH.is_file():
        raise FileNotFoundError(f"No se encontró el archivo de reglas: {REGLAS_PATH}")
    prolog = Prolog()
    prolog.consult(str(REGLAS_PATH))
    return prolog


def _atomo_a_str(val) -> str:
    """Normaliza átomos Prolog devueltos por PySwip a str."""
    if val is None:
        return ""
    if isinstance(val, bytes):
        return val.decode("utf-8", errors="replace")
    return str(val)


def consultar_motor_inferencia(estado: str, clima: str, horario: str) -> dict:
    """
    Ejecuta la consulta Prolog y devuelve la regla activada y su conclusión simbólica.
    """
    prolog = _inicializar_prolog()
    query = (
        f"recomendacion({estado}, {clima}, {horario}, "
        f"IdRegla, Genero, Tempo, Energia, Valence)"
    )
    soluciones = list(prolog.query(query))
    if not soluciones:
        raise ValueError(
            "El motor Prolog no devolvió ninguna solución para la combinación dada. "
            "Revise reglas.pl o los valores de entrada."
        )
    s0 = soluciones[0]
    id_regla = _atomo_a_str(s0["IdRegla"])
    genero = _atomo_a_str(s0["Genero"])
    tempo = _atomo_a_str(s0["Tempo"])
    energia = _atomo_a_str(s0["Energia"])
    valence = _atomo_a_str(s0["Valence"])

    explicaciones = list(prolog.query(f"explicacion_regla({id_regla}, Texto)"))
    if explicaciones:
        texto = _atomo_a_str(explicaciones[0]["Texto"])
    else:
        texto = f"Regla aplicada: {id_regla} (sin texto de explicación en la BC)."

    return {
        "id_regla": id_regla,
        "genero": genero,
        "tempo": tempo,
        "energia": energia,
        "valence": valence,
        "explicacion": texto,
        "query_prolog": query,
    }


def matriz_todas_combinaciones_prolog() -> list[dict]:
    """
    Recorre las 3×3×3 percepciones y consulta reglas.pl una vez por tripleta.
    Sirve para mostrar la BC completa en la UI sin duplicar la matriz en Python.
    """
    prolog = _inicializar_prolog()
    filas: list[dict] = []
    for estado_m in OPCIONES_ESTADO:
        for clima_m in OPCIONES_CLIMA:
            for horario_m in OPCIONES_HORARIO:
                q = (
                    f"recomendacion({estado_m}, {clima_m}, {horario_m}, "
                    f"IdRegla, Genero, Tempo, Energia, Valence)"
                )
                sol = list(prolog.query(q))
                if not sol:
                    continue
                s0 = sol[0]
                filas.append(
                    {
                        "Estado": LABEL_ESTADO[estado_m],
                        "Clima": LABEL_CLIMA[clima_m],
                        "Horario": LABEL_HORARIO[horario_m],
                        "Regla": _atomo_a_str(s0["IdRegla"]),
                        "Género": _atomo_a_str(s0["Genero"]),
                        "Tempo": _atomo_a_str(s0["Tempo"]),
                        "Energía": _atomo_a_str(s0["Energia"]),
                        "Valence": _atomo_a_str(s0["Valence"]),
                    }
                )
    return filas
