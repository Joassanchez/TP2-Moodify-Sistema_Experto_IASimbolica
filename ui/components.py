from __future__ import annotations

from html import escape as html_escape

import streamlit as st


def render_chip(text: str, variant: str = "") -> str:
    cls = f"chip {variant}".strip()
    return f'<span class="{cls}">{html_escape(text)}</span>'


def render_metric_card(label: str, value: str) -> str:
    return (
        '<div class="stat-card">'
        f'<div class="stat-label">{html_escape(label)}</div>'
        f'<div class="stat-value">{html_escape(value)}</div>'
        '</div>'
    )


def render_empty_state(message: str) -> str:
    return f'<div class="empty-state">{html_escape(message)}</div>'


def _cover_html(portada_url: str | None, nombre: str) -> str:
    if portada_url:
        return f'<img src="{html_escape(portada_url)}" class="track-cover" alt="Portada de {nombre}" />'
    return '<div class="track-cover-fallback">Sin portada</div>'


def render_track_card(track: dict, index: int) -> str:
    """Devuelve el HTML de una tarjeta vertical de pista en formato grilla."""
    portada_url = track.get("portada_url")
    spotify_link = track.get("spotify_url")
    simulated_tag = '<span class="track-tag">Simulada</span>' if track.get("simulado") else '<span class="track-tag">Spotify</span>'
    link_html = (
        f'<a class="track-link" href="{html_escape(spotify_link)}" target="_blank" rel="noopener noreferrer">Abrir en Spotify</a>'
        if spotify_link
        else '<span class="track-tag">Sin enlace directo</span>'
    )
    nombre = html_escape(track.get("nombre", ""))
    artista = html_escape(track.get("artista", ""))
    album = html_escape(track.get("album", ""))
    cover_html = _cover_html(portada_url, nombre)

    return f"""
    <div class="track-card">
        {cover_html}
        <div class="track-top">
            <div class="track-index">{index:02d}</div>
            <div style="flex: 1 1 auto; min-width: 0;">
                <div class="track-title">{nombre}</div>
                <div class="track-artist">{artista}</div>
            </div>
        </div>
        <div class="track-album">{album}</div>
        <div class="track-footer">
            {simulated_tag}
            {link_html}
        </div>
    </div>
    """


def render_track_grid(tracks: list[dict]) -> None:
    """Distribuye las tarjetas en una grilla visual de 3 columnas."""
    if not tracks:
        st.markdown(render_empty_state("No se encontraron pistas para mostrar."), unsafe_allow_html=True)
        return

    columns_per_row = 3 if len(tracks) >= 3 else max(1, len(tracks))
    for row_start in range(0, len(tracks), columns_per_row):
        row_tracks = tracks[row_start:row_start + columns_per_row]
        cols = st.columns(len(row_tracks), gap="medium")
        for col, track_index, track in zip(cols, range(row_start + 1, row_start + 1 + len(row_tracks)), row_tracks):
            with col:
                st.markdown(render_track_card(track, track_index), unsafe_allow_html=True)
