
#   BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding


| Paper Background   |                       |
| -------------------| ----------------------|
| Authors            |Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova |
| Year               | 2019                  |
| Journal            | ACL                 |
| Organization       | Google |
|Link|https://arxiv.org/pdf/1810.04805.pdf|



|Contents|               |
| -------------------       | ----------------------|
| Main Point of the Paper     | Introducing bidirectionality for fine tuning improves model performance significantly.|
What problem does BERT solve? | Models such as EMLO and other finetuned models are unidirectional i.e. they use left to right architecture which related the tokens in only one direction. It is crucial to incorporate context from both directions for better performing model. |
How does BERT solve the problem? | BERT uses Masked LM which is basically masking the words in the sequence to introduce robustness in the model. BERT also uses Next Sentence Prediction (NS) where instead of tokens, sentences are fed to understand the relationships between them. For Masked LM, pre trained model does not contain the Masks, so to compensate for the mismatch 80% of the time, the token is masked, 10% of the time random token is used in its place and rest of the 10%, the original token is used. For NSP, assuming A and B are sentence pairs, 50% of the time, B is real and 50% of the time B is a random sentence.|



