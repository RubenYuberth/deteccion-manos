# ✋ Detección de Manos en Tiempo Real con MediaPipe

Este proyecto es una aplicación sencilla en Python que utiliza la cámara web para detectar y rastrear manos en tiempo real. Está construido utilizando **OpenCV** para el procesamiento de video y la moderna API Tasks de **MediaPipe** (`vision.HandLandmarker`) para una detección de manos rápida y precisa.

## 🌟 Características

* **Detección en tiempo real:** Captura video de tu cámara web y procesa cada cuadro al instante.
* **Rastreo de 21 puntos clave (Landmarks):** Identifica y dibuja los 21 puntos articulares de la mano, conectándolos para formar el esqueleto.
* **Numeración de Nodos:** Cada punto detectado muestra su índice (del 0 al 20) en pantalla, lo cual es muy útil para entender cómo MediaPipe clasifica las partes de la mano (pulgar, índice, medio, etc.).
* **Soporte para múltiples manos:** Capacidad de detectar hasta 2 manos simultáneamente.
* **Actualizado a la API moderna:** Utiliza la nueva estructura recomendada de MediaPipe (`mediapipe.tasks.vision`), reemplazando las soluciones antiguas (`mp.solutions.hands`).

## 🛠️ Requisitos e Instalación

El proyecto utiliza gestores de dependencias modernos. Los detalles de las librerías necesarias están especificados en el archivo `pyproject.toml`.

Las dependencias principales son:
* `mediapipe`
* `opencv-python`

Puedes instalarlas usando tu gestor de entornos favorito (`uv`, `poetry`, etc.) o simplemente con pip:
```bash
pip install -r requirements.txt # si lo tienes, o
pip install mediapipe opencv-python
```

**⚠️ Nota importante sobre el modelo:**
Este código requiere el archivo de modelo pre-entrenado de MediaPipe llamado `hand_landmarker.task`. Asegúrate de tener este archivo en el mismo directorio que `main.py` o de descargarlo desde la [documentación oficial de MediaPipe](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker).

## 🚀 Cómo usarlo

1. Asegúrate de que tu cámara web esté conectada.
2. Ejecuta el script principal:

```bash
python main.py
```

* Se abrirá una ventana llamada "Deteccion de manos" mostrando el video de tu cámara.
* Coloca tu(s) mano(s) frente a la cámara para ver el esqueleto dibujado y los puntos numerados.
* Presiona la tecla **`q`** mientras la ventana de video está activa para cerrar el programa de forma segura.

## 📝 Sobre la Actualización de MediaPipe

Con las recientes actualizaciones de MediaPipe (versiones 0.10+), la precisión ha mejorado, pero la forma de escribir el código cambió. 
Este repositorio sirve como ejemplo práctico y actualizado de cómo usar el nuevo módulo `vision.HandLandmarker` con el modo de video (`RunningMode.VIDEO`), mostrando cómo extraer las coordenadas de los landmarks, dibujarlas con OpenCV y realizar conexiones sin depender de las utilidades de dibujo antiguas.