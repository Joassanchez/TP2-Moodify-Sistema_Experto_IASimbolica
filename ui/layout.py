from __future__ import annotations

from html import escape as html_escape

import streamlit as st

from logic.inference_service import LABEL_CLIMA, LABEL_ESTADO, LABEL_HORARIO, matriz_todas_combinaciones_prolog
from ui.components import render_chip, render_metric_card

OPCIONES_ESTADO = ("melancolico", "neutro", "alegre")
OPCIONES_CLIMA = ("lluvioso", "nublado", "soleado")
OPCIONES_HORARIO = ("manana", "tarde", "noche")


def render_hero() -> str:
    return f"""
    <div class="moodify-hero">
        <div class="hero-kicker">
            {render_chip("Sistema experto contextual", "accent")}
            {render_chip("IA simbólica + Prolog + Spotify", "")}
        </div>
        <h1 class="hero-title">Moodify — Recomendación musical contextual (PyA)</h1>
        <p class="hero-subtitle">
            Un dashboard premium para convertir percepción en inferencia musical,
            con trazabilidad explícita y salida conectada a Spotify.
        </p>
        <div class="hero-meta">
            <span class="hero-pill">Percepción · Inferencia · Acción</span>
            <span class="hero-pill">Estado de ánimo · Clima · Horario</span>
            <span class="hero-pill accent">Explicabilidad · Spotify</span>
        </div>
    </div>
    """


def render_intro_note() -> str:
    return """
    <div class="note-box" style="margin-top: 0; margin-bottom: 1rem;">
        Este prototipo implementa <strong>Percepción</strong> (tus selecciones),
        <strong>inferencia</strong> en Prolog y <strong>acción</strong> vía parámetros de Spotify.
    </div>
    """


def render_sidebar_header() -> str:
    return """
    <div class="sidebar-shell">
        <div class="sidebar-kicker">Panel de entrada</div>
        <div class="sidebar-title">Percepción del contexto</div>
        <div class="sidebar-text">
            Seleccioná el estado de ánimo, el clima y el horario para activar la base de conocimientos.
        </div>
    </div>
    """


def render_sidebar() -> tuple[str, str, str, bool]:
    with st.sidebar:
        st.markdown(render_sidebar_header(), unsafe_allow_html=True)
        st.markdown('<div class="sidebar-section-label">Estado de ánimo</div>', unsafe_allow_html=True)
        estado = st.selectbox(
            "Estado de ánimo",
            options=OPCIONES_ESTADO,
            format_func=lambda k: LABEL_ESTADO[k],
        )
        st.markdown('<div class="sidebar-section-label">Clima</div>', unsafe_allow_html=True)
        clima = st.selectbox(
            "Clima",
            options=OPCIONES_CLIMA,
            format_func=lambda k: LABEL_CLIMA[k],
        )
        st.markdown('<div class="sidebar-section-label">Horario</div>', unsafe_allow_html=True)
        horario = st.selectbox(
            "Horario",
            options=OPCIONES_HORARIO,
            format_func=lambda k: LABEL_HORARIO[k],
        )
        ejecutar = st.button("Inferir y recomendar", type="primary")

        st.markdown('<div class="sidebar-section-label">Matriz de conocimiento</div>', unsafe_allow_html=True)
        with st.expander("Matriz de las 27 combinaciones (base Prolog)", expanded=False):
            st.caption(
                "Cada fila es una tripleta estado × clima × horario con su perfil musical inferido."
            )
            try:
                filas = matriz_todas_combinaciones_prolog()
                st.dataframe(filas, hide_index=True, use_container_width=True)
            except Exception as ex:
                st.warning(f"No se pudo cargar la matriz: {ex}")

    return estado, clima, horario, ejecutar


def render_idle_state() -> str:
    return """
    <div class="section-card">
        <div class="section-head">
            <div>
                <div class="section-title">Listo para inferir</div>
                <div class="section-caption">
                    Elegí un contexto desde la barra lateral y presioná <strong>Inferir y recomendar</strong>
                    para ver la inferencia y las pistas sugeridas.
                </div>
            </div>
            <span class="track-tag">Moodify activo</span>
        </div>
    </div>
    """


def render_traceability_panel(inferencia: dict) -> str:
    symbolic_chips = "".join(
        [
            render_chip(f"Género · {inferencia['genero']}", "accent"),
            render_chip(f"Tempo · {inferencia['tempo']}"),
            render_chip(f"Energía · {inferencia['energia']}"),
            render_chip(f"Valence · {inferencia['valence']}"),
        ]
    )
    warning_box = ""
    if inferencia["id_regla"] == "default_rule":
        warning_box = """
        <div class="note-box" style="border-color: rgba(255, 184, 77, 0.28); color: #FFD9A0;">
            No hay regla específica en la BC para esta tripleta; se aplicó el perfil por defecto
            (indie, parámetros medios).
        </div>
        """

    return f"""
    <div class="section-card">
        <div class="section-head">
            <div>
                <div class="section-title">Trazabilidad — Motor de inferencia (Prolog)</div>
                <div class="section-caption">
                    Consulta ejecutada, regla activada, conclusión simbólica y explicación.
                </div>
            </div>
            <span class="track-tag">Inferencia simbólica</span>
        </div>

        <div class="sidebar-section-label">Consulta ejecutada</div>
        <div class="query-block">{html_escape(inferencia['query_prolog'])}</div>

        <div class="sidebar-section-label">Regla activada</div>
        <div class="badge-row">
            <span class="chip accent">{html_escape(inferencia['id_regla'])}</span>
        </div>

        <div class="sidebar-section-label">Conclusión simbólica</div>
        <div class="badge-row">{symbolic_chips}</div>

        <div class="sidebar-section-label">Explicación</div>
        <div class="note-box">{html_escape(inferencia['explicacion'])}</div>

        {warning_box}
    </div>
    """


def render_spotify_panel(params_spotify: dict, leyenda_pistas: str) -> str:
    chips = "".join(render_chip(gen, "accent") for gen in params_spotify["seed_genres"])
    return f"""
    <div class="section-card">
        <div class="section-head">
            <div>
                <div class="section-title">Acción — Parámetros para Spotify</div>
                <div class="section-caption">
                    Traducción del perfil simbólico a parámetros de búsqueda/recomendación.
                </div>
            </div>
            <span class="track-tag">Spotify API</span>
        </div>

        <div class="sidebar-section-label">Seed genres</div>
        <div class="chip-row">{chips}</div>

        <div class="sidebar-section-label">Parámetros</div>
        <div class="stat-grid">
            {render_metric_card('target_energy', f"{params_spotify['target_energy']:.2f}")}
            {render_metric_card('target_valence', f"{params_spotify['target_valence']:.2f}")}
            {render_metric_card('min_tempo', f"{params_spotify['min_tempo']:.1f}")}
            {render_metric_card('max_tempo', f"{params_spotify['max_tempo']:.1f}")}
        </div>

        <div class="note-box">
            {html_escape(leyenda_pistas)}
        </div>
    </div>
    """
