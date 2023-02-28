
#   Attention is all you need


| Paper Background   |                       |
| -------------------| ----------------------|
| Authors            |Ashish Vaswani,Noam Shazeer,Niki Parmar,Jakob Uszkoreit,Jakob Uszkoreit,Aidan N. Gomez,Łukasz Kaiser,Illia Polosukhin  |
| Year               | 2017                  |
| Journal            | Neurips                 |
| Organization       | Google Brain, Google Research, University of Toronto        |
|Link|https://arxiv.org/pdf/1706.03762.pdf|



|Contents|               |
| -------------------       | ----------------------|
| Introduction     | The Transformer architecture is based entirely on self-attention mechanisms, which allow it to process sequences of inputs in parallel, rather than sequentially. This is a departure from previous NLP models, which relied on recurrent neural networks or convolutional neural networks to process sequences.|
How does it work?| The Transformer consists of two main components: an encoder and a decoder. The encoder processes the input sequence and generates a representation of it, which is then used by the decoder to generate the output sequence. Both the encoder and decoder are composed of layers of self-attention mechanisms and feed-forward networks. |
Self Attention| In the self-attention mechanism, each input element is represented as a vector, and a matrix of attention weights is calculated between each pair of vectors. These attention weights determine how much attention to pay to each input element when generating the output. The self-attention mechanism is applied to each input element in parallel, allowing the Transformer to process inputs in parallel.|
| Feed Forward | The feed-forward network in each layer of the Transformer is used to transform the output of the self-attention mechanism into a new representation, which is then passed on to the next layer. This process is repeated for several layers, allowing the Transformer to generate increasingly complex representations of the input sequence.|
|Advantages of Transformers|process inputs in parallel, it is faster than models that rely on sequential processing. It also has fewer parameters than previous models, making it easier to train and deploy. 



