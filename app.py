from __future__ import annotations

from html import escape as html_escape

import streamlit as st

from logic.inference_service import consultar_motor_inferencia
from logic.recommendation_mapper import traducir_a_parametros_spotify
from logic.spotify_service import buscar_pistas_spotify, recomendaciones_simuladas
from ui.components import render_track_grid
from ui.layout import render_hero, render_idle_state, render_intro_note, render_sidebar
from ui.styles import inject_custom_css

def main() -> None:
    st.set_page_config(
        page_title="Moodify POC — Sistema Experto",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_custom_css()

    st.markdown(render_hero(), unsafe_allow_html=True)
    st.markdown(render_intro_note(), unsafe_allow_html=True)

    estado, clima, horario, ejecutar = render_sidebar()

    if not ejecutar:
        st.markdown(render_idle_state(), unsafe_allow_html=True)
        return

    try:
        inferencia = consultar_motor_inferencia(estado, clima, horario)
    except FileNotFoundError as e:
        st.error(str(e))
        return
    except RuntimeError as e:
        st.error(str(e))
        st.code("pip install pyswip\n# + instalar SWI-Prolog desde https://www.swi-prolog.org/")
        return
    except ValueError as e:
        st.warning(str(e))
        return
    except Exception as e:
        st.error(f"Error al consultar Prolog: {e}")
        return

    params_spotify = traducir_a_parametros_spotify(inferencia)
    tracks, _ = buscar_pistas_spotify(params_spotify, inferencia)
    if not tracks:
        tracks = recomendaciones_simuladas(inferencia, params_spotify)

    leyenda_pistas = "Canciones recomendadas según tu contexto actual."

    st.markdown(
        """
        <div class="section-card">
            <div class="section-head">
                <div>
                    <div class="section-title">Pistas sugeridas</div>
                    <div class="section-caption">{html_escape(leyenda_pistas)}</div>
                </div>
                <span class="track-tag">Lista final</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_track_grid(tracks)


if __name__ == "__main__":
    main()
