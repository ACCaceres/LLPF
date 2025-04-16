# LLPF
Herramienta educativa como marco filosófico moderno, proyecto computable y universal

# LLPF Logic Engine - Interfaz Web

Este proyecto te permite interactuar con un motor de lógica simbólica para el Lenguaje Lógico Político Formal (LLPF), una herramienta para deducir teoremas políticos a partir de axiomas universales.

## Archivos incluidos

- `llpf_logic_engine.py`: módulo Python que contiene el motor de inferencia lógica.
- `llpf_web_interface.py`: interfaz construida en Streamlit para ingresar axiomas, hechos y ejecutar inferencias.

## Requisitos

- Python 3.7+
- streamlit

Puedes instalar streamlit ejecutando:

```
pip install streamlit
```

## Cómo ejecutar

1. Asegúrate de que ambos archivos estén en la misma carpeta.
2. Abre una terminal en esa carpeta.
3. Ejecuta el comando:

```
streamlit run llpf_web_interface.py
```

4. La interfaz se abrirá en tu navegador.

## Uso

- Agrega axiomas del tipo `P(x) and sin_limite(x)` como premisa y `concentra(x)` como conclusión.
- Agrega hechos concretos como `P(A)` o `not cuestionable(B)`.
- Ejecuta la inferencia y obtén los teoremas deducidos automáticamente.

---
Sistema inspirado en los principios de lógica política aplicada a la libertad individual frente al poder.
