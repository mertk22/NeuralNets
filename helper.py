#Function to plot loss curves of a model.
import matplotlib.pyplot as plt
import numpy as np
def plot_loss_curves(history):
  epochs = np.arange(len(history["loss"]))
  loss = history["loss"]
  val_loss = history["val_loss"]

  plt.figure(figsize=(12, 9))
  plt.plot(epochs, loss, label="loss")
  plt.plot(epochs, val_loss, label="val_loss")
  plt.xlabel("epochs", fontsize=12)
  plt.ylabel("loss", fontsize=12)
  plt.legend()
  plt.show()

  epochs = np.arange(len(history["accuracy"]))
  accuracy = history["accuracy"]
  val_accuracy = history["val_accuracy"]
  
  plt.figure(figsize=(12, 9))
  plt.plot(epochs, accuracy, label="accuracy")
  plt.plot(epochs, val_accuracy, label="val_accuracy")
  plt.xlabel("epochs", fontsize=12)
  plt.ylabel("accuracy", fontsize=12)
  plt.legend()
  plt.show()
