# RAG_MCNNIL6: A Retrieval-Augmented Multi-Window Convolutional Network for Accurate Prediction of IL-6 Inducing Epitopes
Cheng-Che Chuang, Yu-Chen Liu, Wei-En Jhang, Sin-Siang Wei, Yu-Yen Ou
|[ 🎇&nbsp;Abstract](#abstract) |[📃&nbsp;Dataset](#Dataset) | [ 🚀&nbsp;Quick Prediction ](#colab) |
|-------------------------------|-----------------------------|------------------------------------- |

## 🎇Abstract <a name="abstract"></a>
Interleukin-6 (IL-6) is a critical cytokine involved in immune regulation, inflammation, and the pathogenesis of various diseases, including autoimmune disorders, cancer, and the cytokine storm associated with severe COVID-19. Identifying IL-6 inducing epitopes, the short peptide fragments that trigger IL-6 production, is crucial for developing epitope-based vaccines and immunotherapies. However, traditional methods for epitope prediction often lack accuracy and efficiency. This study presents RAG_MCNNIL6, a novel deep learning framework that integrates Retrieval-Augmented Generation (RAG) with multi-window convolutional neural networks (MCNNs) for accurate and rapid prediction of IL-6 inducing epitopes. RAG_MCNNIL6 leverages ProtTrans, a state-of-the-art pre-trained protein language model, to generate rich embedding representations of peptide sequences. By incorporating a RAG-based similarity retrieval and embedding augmentation strategy, RAG_MCNNIL6 effectively captures both local and global sequence patterns relevant for IL-6 induction, significantly improving prediction performance compared to existing methods. We demonstrate the superior performance of RAG_MCNNIL6 on benchmark datasets, highlighting its potential for advancing research and therapeutic development for IL-6-mediated diseases.
<br>

![workflow](https://github.com/B1607/RAG_MCNNIL6/blob/7c9cff86770ee85d2c409a74599100bcfddb01d9/figure/figure_RAGIL6.png)

## 📃Dataset <a name="Dataset"></a>

| Dataset            | Protein Sequence |    IL-6-inducing peptides |  Non-IL-6-inducing peptides    |
|--------------------|------------------|--------------------------|--------------------------|
| Training data      |   2685             |          292            |2393                     |
| Validation data       |    671         |                    73    |     598                 |
| RAG database   |          9892  |                     513   |                 9379     |

## 🚀Quick Prediction <a name="colab"></a>
[<img src="https://colab.research.google.com/assets/colab-badge.svg">](https://drive.google.com/file/d/1lr0dg4pjMytmZqUhW2GlY7NNtTXWRtBu/view?usp=sharing)<br>
https://drive.google.com/file/d/1lr0dg4pjMytmZqUhW2GlY7NNtTXWRtBu/view?usp=sharing

### Step 1: Environment Setup
open the link of colab notebook and change the runtime type to a device other than CPU.

### Step 2: Excute the program
This Colab notebook will automatically import all necessary dependencies and download the required files.

### Step 3: Submit your fasta file and wait for the Prediction result !

Upload your own FASTA file to run the prediction.
The format of the FASTA file will be as follows:
```bash
>neg_99
KAAVAAAASVPAADK
>pos_18
PQTQQPQQPFPQPQ
>pos_19
AEVDCSRFPNATDK
```
(Alternatively, you may use our testing dataset. [⬇️link](https://github.com/B1607/RAG_MCNNIL6/blob/main/FASTA/test_IL6.fasta)<br>
The result will be formatted as follows:
```bash
>neg_99 [X]
>pos_18 [O]
>pos_19 [O]
```
O indicates the amino acid is predicted to a Interleukin-6 peptides.<br>
X indicates the amino acid is predicted to not a Interleukin-6 peptides.
