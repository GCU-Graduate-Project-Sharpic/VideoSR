# VideoSR

VideoSR, which trained for YCbCr sequence, to handle YCbCr video without any conversion.  
However, currently version **only support Y component**.  
The channel of Y, Cb and Cr is all 1, therefore you can test it by using Cb and Cr, but it's result is optimised to Y component.  


**About VideoSR**  
VideoSR is a part of the "[Sharpic](https://github.com/GCU-Graduate-Project-Sharpic/Sharpic)", which automatically generate HQ sequences from LQ sequences. (Less than 2K).  


## Pre-requirements for usage  

- [YUVSRGAN (BasicSR)](https://github.com/Hyunmin-jasper-Cho/YUVSRGAN/tree/main/BasicSR#pre-requirements-for-usage)  


## Training environment 
> NVIDIA GPU & CUDA  
> pytorch 1.12    

> `Time consumption (NVIDIA Tesla P100): (24+ Hours)`  

## How to test  

- [YUVSRGAN (BasicSR)](https://github.com/Hyunmin-jasper-Cho/YUVSRGAN/tree/main/BasicSR#how-to-test)  
   

## Sample images  
- YUVSRGAN (BasicSR)
<img src = "./BasicSR/figures/ESRGAN_Y.png">  
