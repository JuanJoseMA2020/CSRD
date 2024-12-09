# CSRD

# Gestor de IDs en Excel y PDF

## 🚀 Descripción

Este proyecto es una herramienta interactiva construida con **Streamlit** que permite procesar archivos de tipo Excel y PDF para verificar la existencia de IDs listados en el Excel dentro del contenido de un archivo PDF. El objetivo principal es facilitar la comparación de IDs entre estos dos formatos de documentos y generar un informe detallado con los resultados. 

La aplicación permite:

- Subir un archivo Excel con una lista de IDs.
- Subir un archivo PDF con contenido donde se buscarán esos IDs.
- Analizar los archivos y mostrar:
  - Cuántos IDs fueron encontrados.
  - En qué páginas del PDF se encontraron.
  - Resumen gráfico y detallado del cumplimiento de los IDs.
  - Un informe descargable en formato Excel con los resultados.

## ⚙️ Requisitos

- **Python 3.7 o superior**
- **Bibliotecas necesarias**:
  - `pandas`
  - `PyPDF2`
  - `streamlit`
  - `plotly`
  - `openpyxl`

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install pandas PyPDF2 streamlit plotly openpyxl
```

## 🧑‍💻 Cómo usarlo

1. **Clonar el repositorio**:
   - Si no lo tienes aún, clona este repositorio en tu máquina local:

     ```bash
     git clone https://github.com/tu_usuario/gestor_ids_excel_pdf.git
     cd gestor_ids_excel_pdf
     ```

2. **Ejecutar la aplicación**:
   - Una vez que hayas instalado las dependencias, ejecuta la app con el siguiente comando:

     ```bash
     streamlit run app.py
     ```

   Esto abrirá la aplicación en tu navegador, generalmente en `http://localhost:8501`.

3. **Sube los archivos**:
   - **Archivo Excel**: Debe contener una columna con los IDs que deseas verificar. La columna **DEBE LLAMARSE "DR"**.
   - **Archivo PDF**: Debe ser un archivo en formato PDF en el que los IDs serán buscados.

4. **Ver los resultados**:
   - La aplicación procesará ambos archivos y mostrará un resumen interactivo de los resultados, incluyendo una tabla con los IDs encontrados, los que faltan, y un gráfico de cumplimiento.
   - Además, podrás descargar un archivo Excel con los detalles completos del análisis.

## 📄 Consideraciones al subir los archivos

### Excel:
- **Nombre de la columna**: El archivo Excel debe tener una columna denominada **"DR"** que contiene los IDs a verificar. 
- **Formato limpio**: Asegúrate de que los IDs en la columna **"DR"** estén correctamente formateados, sin espacios adicionales ni caracteres especiales. Los IDs deben ser consistentes (por ejemplo, si es un número, debe ser un número en todas las filas).
- **Sin espacios extra**: No deben existir espacios antes o después de los IDs. La aplicación eliminará los espacios al procesar los datos, pero es importante que los IDs estén bien formateados desde el principio para evitar problemas.
- **Valores NaN**: La aplicación manejará los valores `NaN` y sus variaciones. Si encuentras valores "vacíos" en la columna de IDs, la aplicación los ignorará durante el análisis.

### PDF:
- **Texto legible**: El archivo PDF debe tener texto extraíble (es decir, no debe ser un PDF basado en imágenes). Si el PDF está compuesto por imágenes o escaneos, los IDs no se podrán extraer correctamente.
- **Formato de texto**: La aplicación busca los IDs en el texto del PDF. Si el texto está en un formato no legible o mal estructurado, los resultados podrían no ser precisos.

## 📊 Resultados generados

- **Resumen de la hoja de Excel**: Muestra cuántos IDs están presentes en cada hoja del Excel.
- **IDs Localizados**: Una tabla que muestra qué IDs fueron encontrados en el PDF y en qué páginas.
- **IDs Cumplidos**: Una lista de los IDs que fueron encontrados correctamente en el PDF.
- **IDs Faltantes**: Una lista de los IDs que no fueron encontrados. Si todos los IDs están presentes, se mostrará un mensaje de éxito.
- **Gráfico interactivo**: Un gráfico que visualiza la cantidad de IDs cumplidos vs. faltantes.
- **Informe descargable**: Un archivo Excel estilizado con todos los detalles del análisis, listo para ser descargado.

## 💡 Consideraciones adicionales

- **IDs en el PDF**: El PDF será analizado línea por línea en busca de coincidencias con los IDs del archivo Excel. Asegúrate de que el texto sea claro y no esté distorsionado.
- **Formato del Excel**: El archivo Excel debe estar en formato `.xlsx`. Otros formatos como `.xls` o `.csv` no serán compatibles directamente.

## 📥 Descargables

Después de procesar los archivos, podrás descargar un archivo Excel con el reporte detallado. Este archivo incluirá:

- **IDs por hoja**: El número de IDs encontrados en cada hoja del archivo Excel.
- **IDs Localizados**: Qué IDs se encontraron y en qué páginas del PDF.
- **IDs Cumplidos**: Qué IDs fueron encontrados en el PDF.
- **IDs Faltantes**: Qué IDs no se encontraron en el PDF.

## 🛠️ Desarrollo

Este proyecto fue desarrollado utilizando **Streamlit** para la interfaz interactiva, **Pandas** para el procesamiento de datos y **PyPDF2** para la extracción de texto de archivos PDF.

## 🤝 Contribuciones

Si deseas contribuir al proyecto, ¡eres bienvenido! Solo sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea tu rama de características (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y confirma (`git commit -am 'Añadí nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

¡Gracias por usar nuestro gestor de IDs en Excel y PDF! 🎉


### Detalles del archivo `README.md`:

1. **Descripción General**: Explica brevemente qué hace la aplicación y cómo funciona.
2. **Instrucciones de Uso**: Proporciona pasos claros para ejecutar la aplicación.
3. **Consideraciones al Subir Archivos**: Se destacan los puntos importantes a tener en cuenta al subir los archivos Excel y PDF.
4. **Resultado Esperado**: Descripción de lo que el usuario puede esperar como salida del programa.
5. **Desarrollo y Contribución**: Instrucciones para contribuir al proyecto.

Este `README.md` está diseñado para ser lo más útil posible, guiando a los usuarios a través de los pasos y consideraciones para usar correctamente la aplicación.
