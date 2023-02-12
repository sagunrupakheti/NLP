
#   Paraphrase Generation: A Survey of the State of the Art


| Paper Background   |                       |
| -------------------| ----------------------|
| Authors            |Jianing Zhou and Suma Bhat  |
| Year               | 2021                  |
| Journal            | ACL                 |
| Organization       | University of Illinois at Urbana-Champaign         |
|Link|https://aclanthology.org/2021.emnlp-main.414.pdf|



|Contents|               |
| -------------------       | ----------------------|
| What is paraphrase?       | Paraphrases are texts that convey the same meaning while using different words or sentence structures. eg: QuillBot.  For example, the question How do I improve my English could be equivalently phrased as What is the best way to learn English. |
|Methods | Classical models used and recently Neural models are being used.|
Datasets| **1.PPDB (The paraphrase database)**  - consisting of 73 million phrasal and 8 million lexical paraphrases, as well as 140 million paraphrase patterns that capture meaning-preserving syntactic transformations **[NOT USED ANYMORE]** <br><br> **2.WikiAnswer** - Contains approximately 18 million word-aligned question pairs that are paraphrases. Limitation is  all sentences are questions. <br><br> **3.MSCOCO** - A large-scale object detection dataset, contains images. There are about 500K pairs of paraphrases in this dataset. Annotators describe the most prominent object/action in an image, which makes this dataset suitable for paraphrase-related tasks.<br><br> **4. Quora** - Consists of over 400K lines of potential question duplicate pairs among which there are 150K question pairs denoted as paraphrases. So only these are used for training and testing.<br><br>**5. Twitter URL** - This dataset consists of two subsets, each of which contains both paraphrases and non-paraphrases. Human annotated paraphrases are used. <br><br> **6.ParaNMT** - A dataset of more than 50 million English sentential paraphrase pairs. |
Evaluation Methods | **1. Automatic Evaluation** - BLUE, METEOR, ROUGE (ROUGE-N,ROUGE-L), TER. <br><br> **2. Human Evaluation** - Human annotators are asked to score generated paraphrases along multiple dimensions of quality such as similarity, clarity, and fluency.|
| Traditional Approaches | **1. Rule-Based Approach** - Hand crafted. <br><br> **2.Thesaurus-Based Approaches** - generates paraphrases by substituting some words in the source sentences with their synonyms extracted from a thesaurus. <br><br> **3. SMT-Based Approach** - This approach is based on statistical machine translation (SMT) and is motivated by the fact that paraphrase generation can be seen as a special case of machine translation|
| Neural Approach | **Encoder-Decoder Architecture** - The encoder will encode the source texts into a contextualized vector representation along with a list of vector representations capturing the semantics of each word and context. Then, the decoder will generate paraphrases based on the vectors given by the encoder.<br><br>**Models** - Attention, Variational autoencoder (VAE), Generative adversarial networks (GAN), Reinforcement Learning 



