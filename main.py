import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Configurar el detector de manos
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    min_hand_detection_confidence=0.5,    
    min_tracking_confidence=0.5,
    num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))

    # Realizar la inferencia
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
    detection_result = detector.detect_for_video(mp_image, timestamp_ms)
    
    # Conexiones entre landmarks de la mano (definidas manualmente)
    HAND_CONNECTIONS = [
        (0,1),(1,2),(2,3),(3,4),         # pulgar
        (0,5),(5,6),(6,7),(7,8),         # índice
        (0,9),(9,10),(10,11),(11,12),    # medio
        (0,13),(13,14),(14,15),(15,16),  # anular
        (0,17),(17,18),(18,19),(19,20),  # meñique
        (5,9),(9,13),(13,17)             # palma
    ]

    if detection_result.hand_landmarks:
        for hand_landmarks in detection_result.hand_landmarks:
            h, w, _ = frame.shape

            # Convertir coordenadas normalizadas a píxeles
            points = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks]

            # Dibujar conexiones
            for start, end in HAND_CONNECTIONS:
                cv2.line(frame, points[start], points[end], (0, 255, 0), 2)

            # Dibujar puntos y números
            for idx, (cx, cy) in enumerate(points):
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                cv2.putText(frame, str(idx), (cx - 10, cy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)

    cv2.imshow('Deteccion de manos', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()