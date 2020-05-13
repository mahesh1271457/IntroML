# driver_neuralnetwork_multiclass.py

import NeuralNetwork
import example_classification
import matplotlib.pyplot as plt
import numpy as np
import onehot
import Optimizer
import plot_results

# (1) Set up data
nfeature = 2
m = 1000
case = "quadratic"
nclass = 3
X,Y = example_classification.example(nfeature,m,case,nclass)
# (2) Define model
model = NeuralNetwork.NeuralNetwork(nfeature)
model.add_layer(11,"tanh")
model.add_layer(9,"tanh")
model.add_layer(6,"tanh")
model.add_layer(3,"tanh")
model.add_layer(nclass,"softmax")
# (3) Compile model
optimizer = {"method": "GradientDescent", "learning_rate": 0.05}
model.compile("crossentropy",optimizer)
# (4) Train model
epochs = 200
history = model.train(X,Y,epochs)
# (5) Results
# plot loss and accuracy
plot_results.plot_results_history(history,["loss"])
plot_results.plot_results_history(history,["accuracy"])
# plot heatmap in x0-x1 plane
plot_results.plot_results_classification(model,X,Y,nclass)
plt.show()