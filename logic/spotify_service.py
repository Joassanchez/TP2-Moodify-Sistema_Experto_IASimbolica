from __future__ import annotations

import os

try:
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
except ImportError:
    spotipy = None  # type: ignore
    SpotifyClientCredentials = None  # type: ignore

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "TU_CLIENT_ID_AQUI")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "TU_CLIENT_SECRET_AQUI")


def _credenciales_spotify_validas() -> bool:
    if not CLIENT_ID or not CLIENT_SECRET:
        return False
    if "TU_CLIENT_ID" in CLIENT_ID or "TU_CLIENT_SECRET" in CLIENT_SECRET:
        return False
    if CLIENT_ID == "TU_CLIENT_ID_AQUI" or CLIENT_SECRET == "TU_CLIENT_SECRET_AQUI":
        return False
    return True


def _spotify_intentar_recommendations() -> bool:
    """
    GET /v1/recommendations suele responder 404 en apps nuevas y Spotipy deja
    trazas en consola. Por defecto NO se llama; activar con SPOTIFY_TRY_RECOMMENDATIONS=1
    si tu app aún tiene acceso al endpoint.
    """
    v = os.environ.get("SPOTIFY_TRY_RECOMMENDATIONS", "").strip().lower()
    return v in ("1", "true", "yes", "on")


def _extraer_portada_spotify(track: dict) -> str | None:
    """Devuelve la mejor portada disponible del track o album de Spotify."""
    album = track.get("album") or {}
    images = album.get("images") or []
    if not images:
        return None

    chosen = images[1] if len(images) > 1 else images[0]
    if isinstance(chosen, dict):
        return chosen.get("url")
    return None


def _formatear_track_spotify(t: dict) -> dict:
    """Convierte un objeto track de la Web API al dict usado en la UI."""
    artists = ", ".join(a["name"] for a in t.get("artists", []))
    return {
        "nombre": t.get("name", ""),
        "artista": artists,
        "album": (t.get("album") or {}).get("name", ""),
        "portada_url": _extraer_portada_spotify(t),
        "preview_url": t.get("preview_url"),
        "spotify_url": (t.get("external_urls") or {}).get("spotify"),
        "simulado": False,
    }


def _consulta_busqueda_desde_inferencia(inferencia: dict) -> str:
    """
    Construye una cadena para sp.search(type='track') cuando el endpoint
    de recomendaciones no está disponible (p. ej. 404 en apps nuevas).
    """
    genero = inferencia.get("genero", "indie")
    tempo = inferencia.get("tempo", "medio")
    energia = inferencia.get("energia", "media")
    base = {
        "acoustic_ambient": "acoustic ambient",
        "pop_electronic": "pop electronic",
        "indie": "indie alternative",
    }.get(genero, "indie alternative")
    sufijo = ""
    if tempo == "bajo" and energia in ("baja", "media"):
        sufijo = " chill calm"
    elif tempo == "alto" and energia in ("alta", "media"):
        sufijo = " upbeat dance"
    return (base + sufijo).strip()


def buscar_pistas_spotify(
    params: dict, inferencia: dict, limit: int = 9
) -> tuple[list[dict], str]:
    """
    Usa Spotify para obtener pistas reales. Devuelve la lista y el origen usado.
    """
    if spotipy is None or SpotifyClientCredentials is None:
        return [], ""
    if not _credenciales_spotify_validas():
        return [], ""
    auth = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth, requests_timeout=15)
    market = os.environ.get("SPOTIFY_MARKET", "US")

    if _spotify_intentar_recommendations():
        try:
            rec = sp.recommendations(
                seed_genres=params["seed_genres"],
                limit=limit,
                target_energy=params["target_energy"],
                target_valence=params["target_valence"],
                min_tempo=params["min_tempo"],
                max_tempo=params["max_tempo"],
            )
            tracks = rec.get("tracks") or []
            if tracks:
                return [_formatear_track_spotify(t) for t in tracks if t], "recommendations"
        except Exception:
            pass

    try:
        q = _consulta_busqueda_desde_inferencia(inferencia)
        res = sp.search(q=q, type="track", limit=limit, market=market)
        items = (res.get("tracks") or {}).get("items") or []
        if items:
            return [_formatear_track_spotify(t) for t in items if t], "search"
    except Exception:
        pass

    return [], ""


def recomendaciones_simuladas(inferencia: dict, params: dict, n: int = 9) -> list[dict]:
    """Lista ficticia cuando Spotify no está disponible."""
    base = inferencia["genero"].replace("_", " ").title()
    items = []
    for i in range(1, n + 1):
        items.append(
            {
                "nombre": f"[Simulado] Pista contextual {i} — {base}",
                "artista": "Artista Ejemplo",
                "album": "Álbum POC Moodify",
                "portada_url": None,
                "preview_url": None,
                "spotify_url": None,
                "simulado": True,
            }
        )
    return items


obtener_recomendaciones_spotify = buscar_pistas_spotify
