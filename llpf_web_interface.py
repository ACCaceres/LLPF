
import streamlit as st
from llpf_logic_engine import LLPFLogicEngine

st.title("Motor Lógico LLPF - Lenguaje Lógico Político Formal")

# Inicializar motor
if "motor" not in st.session_state:
    st.session_state.motor = LLPFLogicEngine()

# Sección para agregar axiomas
st.subheader("Agregar Axiomas")
premisa = st.text_input("Premisa (uso de 'x' como variable):", key="premisa")
conclusion = st.text_input("Conclusión (uso de 'x'):", key="conclusion")
if st.button("Agregar Axioma"):
    if premisa and conclusion:
        st.session_state.motor.agregar_axioma(premisa, conclusion)
        st.success("Axioma agregado")

# Sección para agregar hechos
st.subheader("Agregar Hechos")
hecho = st.text_input("Hecho concreto (ej. P(A), not cuestionable(B)):", key="hecho")
if st.button("Agregar Hecho"):
    if hecho:
        st.session_state.motor.agregar_hecho(hecho)
        st.success("Hecho agregado")

# Inferencia
st.subheader("Inferencia Lógica")
if st.button("Ejecutar Inferencia"):
    st.session_state.motor.ejecutar_inferencia()
    st.success("Inferencia ejecutada")

# Mostrar resultados
st.subheader("Resultados")
st.write("**Hechos conocidos:**")
st.code("\n".join(sorted(st.session_state.motor.ver_resultados())))
