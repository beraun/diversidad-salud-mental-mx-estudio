# Informe metodológico de respaldo

**Responsable:** Jorge Beraún Luque · **Fuente:** ENDISEG 2021 (INEGI) · **Estado:** análisis secundario documentado, no artículo dictaminado por pares.

## Propósito y universo

Estimar **asociaciones**, no causas, entre antecedentes de victimización general y antecedentes de ideación suicida alguna vez en la vida entre jóvenes LGBT+ de 15–24 años. La orientación sexual y la identidad de género no constituyen diagnósticos ni explicaciones clínicas inherentes del sufrimiento.

El módulo de ENDISEG 2021 contiene **44,189 entrevistas**. Con el filtro operativo oficial LGBT+ (`FILTRO_10_5=1`) y edad de 15–24 al entrevistar, el dominio fue de **1,088 entrevistas**. El estudio es transversal, probabilístico, estratificado y por conglomerados; la medición de antecedentes fue retrospectiva.

**Medidas:** desenlace `P10_2`, ideación alguna vez; exposición H1 `V_ANY` (al menos uno de seis reactivos generales `P11_1_1`–`P11_1_6`); exposición H2 `V_TYPES=0..6`, número de tipos distintos y no episodios. Sin exposición H1: **n=392**; con exposición: **n=696**.

Los estimadores utilizaron el **factor de expansión `FACTOR`**, estratos `EST_DIS` y unidades primarias `UPM_DIS`. Las varianzas se calcularon conservando el diseño completo y el dominio analítico. Prevalencias como cocientes ponderados, errores estándar e IC95% mediante **linealización de Taylor** y grados de libertad del diseño. H1: diferencia de prevalencias; H2: prueba global de Wald en siete categorías. Se aplicó corrección de Holm a las dos pruebas principales. Las hipótesis fueron **postexploratorias**, no prerregistradas.

## Resultados H1

| Grupo | n sin ponderar | Prevalencia ponderada | EE (pp) | IC95% marginal |
| --- | ---: | ---: | ---: | --- |
| Sin victimización general | 392 | **8.77%** | 2.60 | 3.68–13.87% |
| Con al menos un tipo | 696 | **44.96%** | 2.77 | 39.53–50.39% |

**Diferencia = 36.19 puntos porcentuales** (EE **3.67 pp**, IC95% **28.99–43.38 pp**). El CV del primer grupo, **29.63%**, se aproxima al umbral interno de baja precisión: interpretar con cautela.

## Resultados H2 y comprobaciones

Prueba de Wald de diseño **F=29.5683**, siete categorías (seis grados de libertad de contraste): heterogeneidad global, **sin prueba de tendencia lineal ni efecto incremental causal**.

Hubo cotejo de cálculos Python/R (`survey`), Taylor/Jackknife y sensibilidad limitada por edad. La ejecución integral local registró **10/10 PASS según la salida de consola informada por Jorge Beraún Luque**; esta no equivale a replicación sobre otra muestra o evaluación independiente por pares.

## Limitaciones

- No se conoce el orden temporal entre victimización e ideación, preguntadas ambas como antecedentes de vida.
- La victimización medida es **general**, no necesariamente LGBTfóbica.
- La asociación podría verse afectada por factores no medidos, recuerdo, autodeclaración y sesgos de selección; un ajuste limitado por edad no elimina confusión.
- **No** se mide riesgo suicida actual ni se predicen conductas futuras.
- No deben mezclarse resultados de ENDISEG con encuestas digitales no probabilísticas de otros universos.
- Los datos derivados a nivel individual y los cruces exploratorios retenidos por privacidad **no** se publican.

## Transparencia y referencias

El proyecto fue dirigido por **Jorge Beraún Luque**, utilizando Python, pandas, Jupyter, DuckDB, R, GitHub y **GPT-6 (OpenAI)**, entre otras herramientas. GPT-6 brindó asistencia metodológica, computacional y editorial bajo instrucciones del responsable, no coautoría humana.

Referencias: [INEGI ENDISEG 2021](https://www.inegi.org.mx/programas/endiseg/2021/); [comunicado INEGI 340/22](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2022/endiseg/Resul_Endiseg21.pdf); [Meyer 2003](https://doi.org/10.1037/0033-2909.129.5.674); [Ortiz-Hernández y Valencia-Valero 2015](https://doi.org/10.1590/0102-311X00065314); [de Lange et al. 2022](https://doi.org/10.1089/lgbt.2021.0106); [STROBE](https://www.strobe-statement.org/).
