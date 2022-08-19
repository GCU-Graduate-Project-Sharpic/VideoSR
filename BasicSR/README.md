# YUVSRGAN (VideoSR)
**IMPORTANT**  
Codes are originally cloned from [ESRGAN](https://github.com/xinntao/ESRGAN) project.  
In YUVSRGAN, we re-trained ESRGAN with YCbCr sequence, to handle YCbCr video without any conversion.  
However, currently version **only support Y component**.  
The channel of Y, Cb and Cr is all 1, therefore you can test it by using Cb and Cr, but it's result is optimised to Y component.  


## Pre-requirements for usage  

To test SR method, you should use NVIDIA GPU.  
Therefore it's requirements are different for each environment, so I **strongly recommend** you to use Colab condition.  

### For Colab condition  
Just clone it into your google drive, and run it using Colab terminal.  

### For specific condition  
Install all of things in requirements.txt file. 


## Training environment 
> NVIDIA GPU & CUDA  
> pytorch 1.12    

> `Time consumption (NVIDIA Tesla P100): (24+ Hours)`  

## How to test  

1. Clone repository, then move to root path of BasicSR.  
   `cd YUVSRGAN/BasicSR`  

2. Download trained YUVESRGAN model. ([Model link](https://drive.google.com/file/d/1fb8rgaDm4qFHWai8rmCtVpPY8ug1k60C/view?usp=sharing))  
   
3. Place the downloaded model into `./trained_model` folder.  

4. Place your **ONE CHANNEL** grayscale images in `datasets/LQ_te` folder.  

5. Open `./options/test/ESRGAN/test_RRDBNet_PSNR_x4_YUV.yml` and set below things.  
   i)   name: whatever you want  
   iii) dataroot_gt & dataroot_lq: path where your images exist  
           
7. Run shell file (exec.sh)  
   `$ python3 setup.py develop`  
   `$ sh EXEC_YUVESRGAN.sh`  
   In exec.sh file, `CUDA_VISIBLE_DEVICES=X`, makes X as your GPUs number - 1. (e.g) For one GPU, then X = 0)  
   The result will be in `./BasicSR/results/` folder.  
   

## Sample images  
<img src = "./figures/ESRGAN_Y.png">  
