# Real Benchmarks in Flame's Evaluation
The real benchmarks used in Flame's evaluation.
The applications in the benchmarks are collected from ServerlessBench and FunctionBench. By configuring different memory sizes and input parameters for these applications, we expand the size of the benchmark pool to 384 functions. 

The application name consists of the function ID and its functionality, e.g., case9-matmul. These functions run on the OpenFaas platform and the handle.py is the entry function. We built a local storage service to replace the existing S3 API in our code. The dataset directory contains the files that the function needs to download, including pictures, text, and videos.

These functions are run with Python 3.4 (ML applictions in tensorflow:1.4.1), we list the necessary requirements in the following:

```
pip install exifread minio
pip install pillow
pip install six
pip install chameleon
pip install numpy
pip install ops
pip install opencv-python
pip install Scikit-learn==0.20.4
```

Here is the details of our real benchmarks:
| **ID** | **Source**      | **Function**             | **Memory**    | **Pamamter**                                      | **Execution Time** | **** | ****  | **Startup Time** | **** | ****  |
|--------|-----------------|--------------------------|---------------|---------------------------------------------------|--------------------|------|-------|------------------|------|-------|
|        |                 |                          |               |                                                   | min                | avg  | max   | min              | avg  | max   |
| 1      | ServerlessBench | paralle-alu              | 128MB-1536MB  | parallism=[1,2,4]; loop_time=[10,100,1000,10000]  | 10                 | 233  | 999   | 2103             | 2133 | 3586  |
| 2      | ServerlessBench | key-downloader           | 128MB-1024MB  | file_size=[512,1024,4096]                         | 16                 | 22   | 32    | 2171             | 2402 | 2749  |
| 3      | ServerlessBench | extract-image-metadata   | 128MB-1536MB  | input=imagenet_file                               | 37                 | 80   | 188   | 2200             | 2485 | 2673  |
| 4      | ServerlessBench | store-image-metadata     | 128MB-2048MB  | input=imagenet_file                               | 174                | 311  | 731   | 2430             | 2744 | 3240  |
| 5      | ServerlessBench | thumbnail                | 128MB-1792MB  | input=imagenet_file                               | 258                | 475  | 1127  | 2660             | 2973 | 3370  |
| 6      | ServerlessBench | tail-bigparam            | 128MB-10240MB | dataset=[200000,1000000,5000000]                  | 65                 | 638  | 1774  | 2312             | 3047 | 3972  |
| 7      | ServerlessBench | chameleon                | 128MB-8192MB  | rows=[100,200,500,1000];cols=[100,200,500,1000]   | 55                 | 1878 | 7213  | 2176             | 4315 | 9732  |
| 8      | ServerlessBench | float-operation          | 128MB-1536MB  | loop_time=[10000,100000,1000000,10000000]         | 8                  | 2351 | 16889 | 2115             | 4762 | 19059 |
| 9      | ServerlessBench | linpack                  | 256MB-8192MB  | array_len=[200,1000]                              | 61                 | 2031 | 12664 | 2417             | 4485 | 15134 |
| 10     | ServerlessBench | matmul                   | 128MB-2048MB  | mat_dim=[20,50,100]                               | 4                  | 162  | 570   | 2307             | 2663 | 3237  |
| 11     | ServerlessBench | pyaes                    | 128MB-2048MB  | msg_len=[200,500,1000]; iterations=[20,50,100]    | 877                | 1437 | 3412  | 3120             | 3943 | 5861  |
| 12     | ServerlessBench | dd                       | 128MB-1536MB  | block_size=[1024,2048,4096]; count=[256,512,1024] | 45                 | 62   | 105   | 2183             | 2445 | 2693  |
| 13     | ServerlessBench | giz-compress             | 128MB-1792MB  | file_size=[1024,4096,8192]                        | 63                 | 480  | 1898  | 2395             | 3010 | 4433  |
| 14     | ServerlessBench | random-diskio            | 128MB-1792MB  | file_size=[1024,4096]; block_size=[128,256,512]   | 103                | 155  | 291   | 2267             | 2628 | 2943  |
| 15     | ServerlessBench | image-process            | 256MB-8192MB  | input=imagenet_file                               | 2134               | 2843 | 6712  | 4311             | 5299 | 9286  |
| 16     | ServerlessBench | image-rotate             | 256MB-4096MB  | input=imagenet_file                               | 545                | 750  | 1709  | 2743             | 3172 | 3978  |
| 17     | ServerlessBench | image-scale              | 256MB-4096MB  | input=imagenet_file                               | 1723               | 2263 | 5090  | 3836             | 4749 | 7710  |
| 18     | ServerlessBench | cnn-image-classification | 256MB-2560MB  | input=imagenet_file                               | 51                 | 203  | 601   | 1774             | 2216 | 3979  |
| 19     | ServerlessBench | video-process            | 128MB-2048MB  | dpi=[1280x720]; video_size=[1024,2560,3042]       | 2023               | 5076 | 14892 | 4363             | 7502 | 17511 |
| 20     | ServerlessBench | lr-prediction            | 256MB-2048MB  | data_size=[2,5,10,20]                             | 72                 | 139  | 230   | 1733             | 3001 | 6838  |
| 21     | ServerlessBench | face-detection           | 256MB-2560MB  | video_size=[256,512,1024]                         | 569                | 1150 | 2801  | 2189             | 2868 | 3901  |
| 22     | ServerlessBench | rnn-generate-char-level  | 256MB-2560MB  | lang=[English,German]; input_len=[20,50,80,100]   | 5                  | 270  | 1864  | 1007             | 1356 | 3551  |


