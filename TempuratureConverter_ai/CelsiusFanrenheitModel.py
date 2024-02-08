import logging
import tensorflow as tf
tf.get_logger().setLevel(logging.ERROR)

import numpy as np

celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fanrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

model = tf.keras.Sequential([l0])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(celsius_q, fanrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

while (True):
    pred_value = eval(input("Enter the value (degree Celsius) for the model to predict: "))

    print(model.predict([pred_value]))