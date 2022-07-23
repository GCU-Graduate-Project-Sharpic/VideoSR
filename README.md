# VideoSR
This is the part of the "Super resolution" project.  
It automatically generate HQ video from LQ video. (Less than 2K).  
  
Base algorithm that we use to is [RealSR](https://github.com/Tencent/Real-SR).  

Our suggested method is YUVNet, that is changed occured in input/output channel,  
which following [this paper](https://arxiv.org/pdf/2103.01760.pdf). 


## Dependencies 
> Python 3  
> PyTorch >= 1.0  
> NVIDIA GPU with CUDA  
> Python packages: `pip install numpy opencv-python lmdb pyyaml`  
> Tensorboard: if PyTorch >= 1.1 `pip install tb-noghtly future` : `pip install tensorboardX`
