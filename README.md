# ATSumm

# ATSumm: Auxiliary information enhanced approach for abstractive disaster Tweet Summarization with sparse training data

This repository contains code related to the paper “ATSumm: Auxiliary information enhanced approach for abstractive disaster Tweet Summarization with sparse training data (KBS) journal, 2024.

The code has been developed using python 2.7, and Tensorflow 1.4. This implementation is based on code releases related to Pointer-Generator Networks and the TextSum project.

# Dataset 
For training, we use the ARIES dataset, which contains 7500 training samples along with their ground-truth summaries. For evaluation, we used 13 disaster events from different locations and types.

# Key-phrase Information

The DRAKE model is used to identify the key phrase and the importance score of each tweet of a disaster event. For the key-phrase implementation, please refer to our paper: IKDSumm: Incorporating key-phrases into BERT for extractive disaster tweet summarization (Computer Speach and Language) journal, 2024.   


