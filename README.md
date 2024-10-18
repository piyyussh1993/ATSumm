# ATSumm

# ATSumm: Auxiliary information enhanced approach for abstractive disaster Tweet Summarization with sparse training data

This repository contains code related to abstractive disaster tweet summarization. Our KBS paper “ATSumm: Auxiliary information enhanced approach for abstractive disaster Tweet Summarization with sparse training data" consists of two phases:

1. Extractive phase, where we extract the most important tweets from input tweets, and

2. Abstractive phase, where we aim to construct a sentence summary from extracted tweets considering only most important information in a concise way.

We have considered 13 different disaster events from four different continents: USA, Asia, Oceania, and Europe. These events belong to both the natural and man-made disaster types. This dataset considers earthquake, Typhoon, Flood, Blast, Shooting, Cyclone, Wildfire, and Hurricane in this paper. Dataset CSV contains Tweet-text and ground truth summaries used in this project. The codes directory contains codes and a README containing detailed details and information about how to run those codes.

For more details --- please go through the paper!!

The code was developed using Python 2.7. This implementation is based on code releases related to Pointer-Generator Networks and the TextSum project.

# Key-phrase Information

The DRAKE model is used to identify the key phrase and the importance score of each tweet of a disaster event. For the key-phrase implementation, please refer to and cite our paper: 

Piyush Kumar Garg, R Chakraborty, S Gupta, SK Dandapat, IKDSumm: Incorporating key-phrases into BERT for extractive disaster tweet summarization, Computer Speech & Language (2024). DOI: https://doi.org/10.1016/j.csl.2024.101649

@article{garg2024ikdsumm,
  title={IKDSumm: Incorporating key-phrases into BERT for extractive disaster tweet summarization},
  author={Garg, Piyush Kumar and Chakraborty, Roshni and Gupta, Srishti and Dandapat, Sourav Kumar},
  journal={Computer Speech \& Language},
  volume={87},
  pages={101649},
  year={2024},
  publisher={Elsevier}
}

# Dataset 
For training, we use the ARIES dataset, which contains 7500 training samples along with their ground-truth summaries. For evaluation, we used 13 disaster events from different locations and types. We have prepared the ground truth summaries following the instructions detailed in the paper. 3 graduate students participated in this task. If you need ground truth summaries and ARIES training data, kindly send an email to piyush_2021cs05@iitp.ac.in. 

If you are using the dataset of this paper, kindly cite the following article:

@article{garg2024atsumm,
  title={ATSumm: Auxiliary information enhanced approach for abstractive disaster Tweet Summarization with sparse training data},
  author={Garg, Piyush Kumar and Chakraborty, Roshni and Dandapat, Sourav Kumar},
  journal={arXiv preprint arXiv:2405.06541},
  year={2024}
}




