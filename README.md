# Hi 🫡

My first neural network project following [Victor Zhou's blog post](https://victorzhou.com/blog/intro-to-neural-networks/)

## Goals

-   Learn how to build a neural network mostly from scratch _(Utilizing numpy)_
-   Expand upon this...

### Dumb Takeaway/s

-   I always thought hidden layer meant we aren't weren't aware of what the values were in the layers. Maybe I was conflacting deep neural networks, black boxes, and neural networks in general?
-   Importing even just the class with `from neuronClass import Neuron` seems to be running the entire file. My print statements that are **outside** the class are being run.
    -   Adding `if __name__ == '__main__':` helped.
