import tensorflow
import torch
import sklearn
import tensorflow

import torch
import tensorflow as tf
from tensorflow.python.client import device_lib


if __name__ == '__main__':
    print(f"토치 버전 : {torch.__version__}")
    print(f"텐서플로 버전 : {tensorflow.__version__}")
    print(f"사이킷런 버전 : {sklearn.__version__}")
    print(f"torch의 gpu 사용 가능 여부 확인 : {torch.cuda.is_available()}")
    print(f"사용가능한 gpu 보기 : {torch.cuda.get_device_name(0)}")


    tf.config.list_physical_devices('GPU')

    USE_CUDA = torch.cuda.is_available()
    print(USE_CUDA)

    device = torch.device('cuda:0' if USE_CUDA else 'cpu')
    print('학습을 진행하는 기기:', device)

    print(device_lib.list_local_devices())