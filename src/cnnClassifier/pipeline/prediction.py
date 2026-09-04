import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

        config = ConfigurationManager().get_evaluation_config()
        self.image_size = tuple(config.params_image_size[:-1])
        self.class_names = sorted(
            d for d in os.listdir(config.training_data)
            if os.path.isdir(os.path.join(config.training_data, d))
        )

        logger.info(f"Loading model from {config.path_of_model}")
        self.model = load_model(config.path_of_model)

    def predict(self):
        test_image = image.load_img(self.filename, target_size=self.image_size)
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        prediction = self.model.predict(test_image)
        class_index = int(np.argmax(prediction, axis=1)[0])
        confidence = float(prediction[0][class_index])
        label = self.class_names[class_index]

        return [{'image': label, 'confidence': round(confidence, 4)}]
