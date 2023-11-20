# CoRefResNorwegian - Gender Bias
This repository contains a dataset consisting of 40 winograd-style sentences intended to measure the presence of occupational gender bias in Norwegian LLMs, as well as code containing the results and visualizations of the performances of ChatGPT and Google Bard on this dataset.
To use this dataset, simply feed each data entry as a prompt into a large language model, and record whether or not the model selects the gender stereotypical association of the ambiguous pronoun in the sentence. 

Furthermore, this repository also contains a baseline dataset in which the sentences of the original dataset are made unambiguous by explicitly defining the gender of both occupational entities in the dataset. This dataset contains 80 entries, and should be used to ensure that the sentences of the original dataset are, in fact, ambiguous, and that the model tested is able to overcome gender stereotypes when provided with a question that has a definite answer, even when that answer is in opposition to common stereotypes.

