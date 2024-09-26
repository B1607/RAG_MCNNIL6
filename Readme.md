# RAG_MCNNIL6: A Retrieval-Augmented Multi-Window Convolutional Network for Accurate Prediction of IL-6 Inducing Epitopes
Cheng-Che Chuang, Yu-Chen Liu, Wei-En Jhang, Sin-Siang Wei, Yu-Yen Ou


## Abstract <a name="abstract"></a>
Interleukin-6 (IL-6) is a critical cytokine involved in immune regulation, inflammation, and the pathogenesis of various diseases, including autoimmune disorders, cancer, and the cytokine storm associated with severe COVID-19. Identifying IL-6 inducing epitopes, the short peptide fragments that trigger IL-6 production, is crucial for developing epitope-based vaccines and immunotherapies. However, traditional methods for epitope prediction often lack accuracy and efficiency. This study presents RAG_MCNNIL6, a novel deep learning framework that integrates Retrieval-Augmented Generation (RAG) with multi-window convolutional neural networks (MCNNs) for accurate and rapid prediction of IL-6 inducing epitopes. RAG_MCNNIL6 leverages ProtTrans, a state-of-the-art pre-trained protein language model, to generate rich embedding representations of peptide sequences. By incorporating a RAG-based similarity retrieval and embedding augmentation strategy, RAG_MCNNIL6 effectively captures both local and global sequence patterns relevant for IL-6 induction, significantly improving prediction performance compared to existing methods. We demonstrate the superior performance of RAG_MCNNIL6 on benchmark datasets, highlighting its potential for advancing research and therapeutic development for IL-6-mediated diseases.
<br>

![workflow]()

## Dataset <a name="Dataset"></a>

| Dataset            | Protein Sequence |    IL-6-inducing peptides |  Non-IL-6-inducing peptides    |
|--------------------|------------------|--------------------------|--------------------------|
| Training data      |   2685             |          292            |2393                     |
| Validation data       |    671         |                    73    |     598                 |
| RAG database   |          9892  |                     513   |                 9379     |
