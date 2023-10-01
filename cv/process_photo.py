import cv2
import numpy as np
import os
from schemas import EvacuationMap, BaseElement

def convert_np_array_to_evacuation_map(np_array: np.ndarray) -> EvacuationMap:
    ev_map = []
    for row in np_array:
        ev_map_row = []
        for element in row:
            ev_map_row.append(BaseElement(element))
        ev_map.append(ev_map_row)
    return EvacuationMap(ev_map=ev_map)

def process_photo_in_evacuation_map(file: bytes) -> EvacuationMap:
    nparr = np.frombuffer(file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    min_values = np.min(img, axis=2)
    max_values = np.max(img, axis=2)

    channel_diff = max_values - min_values

    result_matrix = np.zeros_like(min_values, dtype=np.uint8)

    result_matrix[np.logical_or(max_values <= 25, (max_values <= 110) & (channel_diff < 20))] = 1
    print(result_matrix)

    return convert_np_array_to_evacuation_map(result_matrix)