import argparse
import numpy as np
import matplotlib.pyplot as plt
import utils
from mattingCompare import *

# settings
# netModel = "resnet50"
# netModelExtend="resnet50"
netModel = "coord_resnet152"
netModelExtend="coord_resnet152"

parser = argparse.ArgumentParser(description='ZZX TRAIN SEGMENTATION')
parser.add_argument('--dataset', type=str, default='cvprw2020-ade20K-defg', metavar='str',
                    help='dataset: cvprw2020-ade20K-defg or ... (default: cvprw2020-ade20K-defg)')
parser.add_argument('--batch_size', type=int, default=8, metavar='N',
                    help='input batch size for training (default: 4)')
parser.add_argument('--in_size', type=int, default=384, metavar='N',
                    help='input image size for training (default: 256)')
#可视化模型
#print models
parser.add_argument('--print_models', action='store_true', default=True,
                    help='visualize and print networks')
# TODO
# parser.add_argument('--net_G', type=str, default='CNN', metavar='str',
#                    help='net_G: CNN or coord_CNN (default: coord_CNN )')

# TODO
parser.add_argument('--net_G', type=str, default=netModel, metavar='str',
                    help='net_G: '+netModel+' or '+netModelExtend+'(default: coord_resnet150 )')
parser.add_argument('--checkpoint_dir', type=str, default=r'./checkpoints/' + netModel, metavar='str',
                    help='dir to save checkpoints (default: ./checkpoints/'+netModel+')')
parser.add_argument('--vis_dir', type=str, default=r'./val_out/'+netModel, metavar='str',
                    help='dir to save results during training (default: ./val_out_G)'+netModel)
parser.add_argument('--lr', type=float, default=1e-4,
                    help='learning rate (default: 0.0002)')
parser.add_argument('--max_num_epochs', type=int, default=200, metavar='N',
                    help='max number of training epochs (default 200)')


args = parser.parse_args()

if __name__ == '__main__':
    # args.net_G = 'resnet50'
    # args.checkpoint_dir = 'checkpoints_G_resnet50'
    # args.in_size = 384

    # args.net_G = 'coord_resnet50'
    # args.checkpoint_dir = 'checkpoints_G_coord_resnet50'
    # args.in_size = 384

    dataloaders = utils.get_loaders(args)


    skydet = SkyDetector(args=args, dataloaders=dataloaders)
    skydet.train_models()
