:- encoding(utf8).

% ============================================================================
% MOTOR DE INFERENCIA — Base de Conocimientos (Prolog)
% Cubre las 27 tripletas (estado_animo × clima × horario) del formulario.
% Modelo PyA: percepciones → perfil (genero, tempo, energia, valence).
% ============================================================================

% --- Matriz completa: escenario_especifico(Estado, Clima, Horario, IdRegla, Genero, Tempo, Energia, Valence) ---

% ========== MELANCÓLICO (9) ==========
escenario_especifico(melancolico, lluvioso, manana, caso_mel_llu_man, acoustic_ambient, medio, baja, bajo).
escenario_especifico(melancolico, lluvioso, tarde, caso_mel_llu_tar, acoustic_ambient, bajo, baja, bajo).
% Escenario A (obligatorio del enunciado)
escenario_especifico(melancolico, lluvioso, noche, escenario_a, acoustic_ambient, bajo, baja, bajo).

escenario_especifico(melancolico, nublado, manana, caso_mel_nub_man, acoustic_ambient, medio, baja, bajo).
escenario_especifico(melancolico, nublado, tarde, caso_mel_nub_tar, acoustic_ambient, bajo, baja, bajo).
escenario_especifico(melancolico, nublado, noche, melancolia_nocturna, acoustic_ambient, bajo, baja, bajo).

escenario_especifico(melancolico, soleado, manana, caso_mel_sol_man, indie, medio, media, medio).
escenario_especifico(melancolico, soleado, tarde, caso_mel_sol_tar, indie, medio, baja, medio).
escenario_especifico(melancolico, soleado, noche, caso_mel_sol_noc, acoustic_ambient, bajo, baja, bajo).

% ========== NEUTRO (9) ==========
escenario_especifico(neutro, lluvioso, manana, caso_neu_llu_man, indie, medio, baja, medio).
escenario_especifico(neutro, lluvioso, tarde, lluvia_neutra, indie, medio, media, medio).
escenario_especifico(neutro, lluvioso, noche, caso_neu_llu_noc, acoustic_ambient, bajo, baja, medio).

escenario_especifico(neutro, nublado, manana, caso_neu_nub_man, indie, medio, media, medio).
escenario_especifico(neutro, nublado, tarde, caso_neu_nub_tar, indie, medio, media, medio).
escenario_especifico(neutro, nublado, noche, caso_neu_nub_noc, indie, bajo, baja, bajo).

escenario_especifico(neutro, soleado, manana, caso_neu_sol_man, indie, medio, media, alto).
escenario_especifico(neutro, soleado, tarde, caso_neu_sol_tar, pop_electronic, medio, media, medio).
escenario_especifico(neutro, soleado, noche, caso_neu_sol_noc, indie, medio, media, medio).

% ========== ALEGRE (9) ==========
escenario_especifico(alegre, lluvioso, manana, caso_ale_llu_man, pop_electronic, medio, media, alto).
escenario_especifico(alegre, lluvioso, tarde, caso_ale_llu_tar, pop_electronic, medio, alta, alto).
escenario_especifico(alegre, lluvioso, noche, caso_ale_llu_noc, pop_electronic, alto, alta, alto).

escenario_especifico(alegre, nublado, manana, caso_ale_nub_man, pop_electronic, alto, alta, alto).
escenario_especifico(alegre, nublado, tarde, caso_ale_nub_tar, pop_electronic, medio, alta, alto).
escenario_especifico(alegre, nublado, noche, caso_ale_nub_noc, pop_electronic, alto, alta, medio).

% Escenario B (obligatorio del enunciado)
escenario_especifico(alegre, soleado, tarde, escenario_b, pop_electronic, alto, alta, alto).
escenario_especifico(alegre, soleado, manana, energia_matutina, pop_electronic, alto, alta, alto).
escenario_especifico(alegre, soleado, noche, caso_ale_sol_noc, pop_electronic, alto, alta, alto).

% --- Regla principal (corte: una sola regla por tripleta) ---
recomendacion(Estado, Clima, Horario, IdRegla, Genero, Tempo, Energia, Valence) :-
    escenario_especifico(Estado, Clima, Horario, IdRegla, Genero, Tempo, Energia, Valence),
    !.

% Respaldo si se agregan valores nuevos en la UI sin actualizar la BC
recomendacion(_Estado, _Clima, _Horario, default_rule, indie, medio, media, medio).

% --- Explicaciones por IdRegla (trazabilidad) ---
explicacion_regla(escenario_a, 'Melancólico + lluvioso + noche (Escenario A): acústico/ambiental, tempo y energía bajos, valence bajo.').
explicacion_regla(escenario_b, 'Alegre + soleado + tarde (Escenario B): pop/electrónico, tempo y energía altos, valence alto.').

explicacion_regla(caso_mel_llu_man, 'Melancólico con lluvia por la mañana: ambiente acústico suave, energía baja, valence bajo.').
explicacion_regla(caso_mel_llu_tar, 'Melancólico, lluvia y tarde: acústico/ambiental lento y contenido.').
explicacion_regla(melancolia_nocturna, 'Melancólico + nublado + noche: acústico/ambiental nocturno, baja energía y valence bajo.').
explicacion_regla(caso_mel_nub_man, 'Melancólico y cielo nublado al amanecer: acústico con tempo medio y tono sombrío.').
explicacion_regla(caso_mel_nub_tar, 'Melancólico con nubes por la tarde: acústico pausado, energía baja.').
explicacion_regla(caso_mel_sol_man, 'Melancólico con sol matutino: perfil indie equilibrado (contraste luz/sentimiento).').
explicacion_regla(caso_mel_sol_tar, 'Melancólico y tarde soleada: indie con energía moderada y valence intermedio.').
explicacion_regla(caso_mel_sol_noc, 'Melancólico de noche aun con sol en el recuerdo: vuelve el acústico nocturno suave.').

explicacion_regla(caso_neu_llu_man, 'Neutro con lluvia por la mañana: indie reflexivo, energía algo baja.').
explicacion_regla(lluvia_neutra, 'Neutro + lluvia + tarde: indie equilibrado (tempo, energía y valence medios).').
explicacion_regla(caso_neu_llu_noc, 'Neutro, lluvia y noche: acústico suave con valence medio-bajo.').
explicacion_regla(caso_neu_nub_man, 'Neutro y nublado por la mañana: indie estable y neutro tonalmente.').
explicacion_regla(caso_neu_nub_tar, 'Neutro con nubes por la tarde: indie de fondo, parámetros medios.').
explicacion_regla(caso_neu_nub_noc, 'Neutro de noche con nubes: indie más lento y reservado.').
explicacion_regla(caso_neu_sol_man, 'Neutro con sol en la mañana: indie con valence algo más alto.').
explicacion_regla(caso_neu_sol_tar, 'Neutro y tarde soleada: ligero acercamiento pop/electrónico moderado.').
explicacion_regla(caso_neu_sol_noc, 'Neutro con sol pero ya de noche: indie moderado sin exceso de euforia.').

explicacion_regla(caso_ale_llu_man, 'Alegre a pesar de la lluvia por la mañana: pop/electrónico moderado con buen valence.').
explicacion_regla(caso_ale_llu_tar, 'Alegre con lluvia por la tarde: pop/electrónico enérgico y luminoso.').
explicacion_regla(caso_ale_llu_noc, 'Alegre, lluvia y noche: ritmo alto y fiesta controlada (alta energía).').
explicacion_regla(caso_ale_nub_man, 'Alegre con cielo nublado al iniciar el día: pop/electrónico muy vital.').
explicacion_regla(caso_ale_nub_tar, 'Alegre y nublado por la tarde: pop/electrónico animado con valence alto.').
explicacion_regla(caso_ale_nub_noc, 'Alegre de noche con nubes: ritmo alto, energía alta, valence algo más moderado.').
explicacion_regla(energia_matutina, 'Alegre + soleado + mañana: pop/electrónico enérgico para arrancar el día.').
explicacion_regla(caso_ale_sol_noc, 'Alegre con sol y noche: pop/electrónico festivo y alto tempo.').

explicacion_regla(default_rule, 'Combinación no contemplada en la BC actual: perfil indie por defecto (parámetros medios).').
