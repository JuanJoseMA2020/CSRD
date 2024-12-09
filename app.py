import pandas as pd
from PyPDF2 import PdfReader
import streamlit as st
import plotly.express as px
from io import BytesIO

# Configuración de la página
st.set_page_config(page_title="Gestor de IDs en Excel y PDF", layout="wide", initial_sidebar_state="expanded")

# Título de la app
st.title("✨ Gestor de IDs en Excel y PDF ✨")
st.markdown("Sube un archivo Excel con los IDs y un archivo PDF para buscar coincidencias. Se generará un informe detallado.")

# Subida de archivos
uploaded_excel = st.file_uploader("📄 Sube tu archivo Excel", type=["xlsx"])
uploaded_pdf = st.file_uploader("📑 Sube tu archivo PDF", type=["pdf"])

if uploaded_excel and uploaded_pdf:
    with st.spinner("📂 Procesando archivos..."):
        # Leer Excel
        excel_data = pd.read_excel(uploaded_excel, sheet_name=None)
        ids_excel = set()
        ids_hojas = []
        
        for sheet_name, sheet_data in excel_data.items():
            if "DR" in sheet_data.columns:
                # Normalizar IDs eliminando espacios
                sheet_data["DR"] = sheet_data["DR"].astype(str).str.strip()
                ids_hoja = set(sheet_data["DR"].dropna().unique())
                ids_hojas.append([sheet_name, len(ids_hoja)])
                ids_excel.update(ids_hoja)
        
        # Leer PDF
        reader = PdfReader(uploaded_pdf)
        ids_localizados = {}
        for page_number, page in enumerate(reader.pages, start=1):
            texto_pagina = page.extract_text()
            if texto_pagina:
                # Normalizar IDs en el PDF eliminando espacios
                lines = [line.strip() for line in texto_pagina.splitlines()]
                for line in lines:
                    for id_excel in ids_excel:
                        if id_excel in line:  # Comparación con los IDs normalizados
                            ids_localizados.setdefault(id_excel, set()).add(page_number)
        
        # Resultados
        ids_localizados_tabulate = [[id, ", ".join(map(str, sorted(list(pages))))] for id, pages in ids_localizados.items()]
        cumplen = [id for id in ids_excel if id in ids_localizados]
        
        # Identificar los IDs faltantes, excluyendo "NaN" y sus variantes
        faltan = [id for id in ids_excel if id not in ids_localizados and pd.notna(id) and str(id).lower() != "nan"]

        # DataFrames
        df_ids_hojas = pd.DataFrame(ids_hojas, columns=["Hoja", "Número de IDs"])
        df_ids_localizados = pd.DataFrame(ids_localizados_tabulate, columns=["ID", "Páginas"])
        df_cumplen = pd.DataFrame(cumplen, columns=["ID"])

    st.success("✅ Archivos procesados con éxito.")

    # Visualización de datos
    st.subheader("📊 Resultados de análisis")
    
    # Mostrar tablas una debajo de otra, ajustadas al ancho
    st.write("### Resumen por Hoja del Excel")
    st.dataframe(df_ids_hojas, use_container_width=True)
    
    st.write("### IDs Localizados en el PDF")
    st.dataframe(df_ids_localizados, use_container_width=True)

    st.write("### IDs Cumplidos")
    st.dataframe(df_cumplen, use_container_width=True)

    if len(faltan) == 0:
        # Si no hay IDs faltantes (o solo faltaba un 'NaN' o similar)
        df_faltan = pd.DataFrame(columns=["ID"])
        st.write("### IDs Faltantes")
        st.dataframe(df_faltan, use_container_width=True)
        
        # Animación y mensaje de éxito
        st.balloons()
        st.success("🎉 ¡Todo salió bien! No faltan IDs en el PDF. 🎉")
    else:
        # Mostrar los IDs faltantes
        st.write("### IDs Faltantes")
        df_faltan = pd.DataFrame(faltan, columns=["ID"])
        st.dataframe(df_faltan, use_container_width=True)
        st.warning(f"⚠️ Hay {len(faltan)} IDs faltantes. Por favor, revisa los resultados.")
    
    # Gráfico interactivo - Resumen de Cumplimiento de IDs
    st.write("### 📈 Resumen Gráfico de Cumplimiento de IDs")
    resumen_fig = px.bar(
        x=["Cumplen", "Faltan"], 
        y=[len(cumplen), len(faltan)], 
        text=[len(cumplen), len(faltan)], 
        labels={"x": "Estado", "y": "Cantidad de IDs"},
        title="Cumplimiento de IDs",
        color=["Cumplen", "Faltan"],
        color_discrete_map={"Cumplen": "green", "Faltan": "red"}
    )
    resumen_fig.update_traces(textposition="outside")
    st.plotly_chart(resumen_fig, use_container_width=True)
    
    # Generar Excel estilizado
    def crear_excel():
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df_ids_hojas.to_excel(writer, sheet_name="IDs por Hoja", index=False)
            df_ids_localizados.to_excel(writer, sheet_name="IDs Localizados", index=False)
            df_cumplen.to_excel(writer, sheet_name="IDs Cumplen", index=False)
            df_faltan.to_excel(writer, sheet_name="IDs Faltantes", index=False)
        output.seek(0)
        return output
    
    # Botón para descargar Excel
    st.subheader("📥 Descargar Resultados")
    excel_output = crear_excel()
    st.download_button(
        label="Descargar Excel Estilizado 📂",
        data=excel_output,
        file_name="resultados_ids.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
