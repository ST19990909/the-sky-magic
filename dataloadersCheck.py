import argparse
import numpy as np
import matplotlib.pyplot as plt
import utils
from mattingCompare import *

# settings
# netModel = "resnet150"
# netModelExtend="resnet150"
netModel = "coord_resnet50"
netModelExtend = "coord_resnet50"

parser = argparse.ArgumentParser(description='ZZX TRAIN SEGMENTATION')
parser.add_argument('--dataset', type=str, default='cvprw2020-ade20K-defg', metavar='str',
                    help='dataset: cvprw2020-ade20K-defg or ... (default: cvprw2020-ade20K-defg)')
parser.add_argument('--batch_size', type=int, default=8, metavar='N',
                    help='input batch size for training (default: 4)')
parser.add_argument('--in_size', type=int, default=384, metavar='N',
                    help='input image size for training (default: 256)')
# 可视化模型
# print models
parser.add_argument('--print_models', action='store_true', default=True,
                    help='visualize and print networks')
# TODO
# parser.add_argument('--net_G', type=str, default='CNN', metavar='str',
#                    help='net_G: CNN or coord_CNN (default: coord_CNN )')

# TODO
parser.add_argument('--net_G', type=str, default=netModel, metavar='str',
                    help='net_G: ' + netModel + ' or ' + netModelExtend + '(default: coord_resnet150 )')
parser.add_argument('--checkpoint_dir', type=str, default=r'./checkpoints/' + netModel, metavar='str',
                    help='dir to save checkpoints (default: ./checkpoints/' + netModel + ')')
parser.add_argument('--vis_dir', type=str, default=r'./val_out/' + netModel, metavar='str',
                    help='dir to save results during training (default: ./val_out_G)' + netModel)
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

    # # How to check if the data is loading correctly?
    # show train data
    # dataloaders = utils.get_loaders(args)
    # for i in range(100):
    #     data = next(iter(dataloaders['train']))
    #     vis_A = utils.make_numpy_grid(data['A'])
    #     vis_B = utils.make_numpy_grid(data['B'])
    #     vis = np.concatenate([vis_A, vis_B], axis=0)
    #     print(data['A'].shape)
    #     print(data['B'].shape)
    #     plt.imshow(vis)
    #     plt.show()

    # #show val data
    # dataloaders = utils.get_loaders(args)
    # for i in range(100):
    #     data = next(iter(dataloaders['val']))
    #     vis_A = utils.make_numpy_grid(data['A'])
    #     vis_B = utils.make_numpy_grid(data['B'])
    #     vis = np.concatenate([vis_A, vis_B], axis=0)
    #     print(data['A'].shape)
    #     print(data['B'].shape)
    #     plt.imshow(vis)
    #     plt.show()

    # show all data
    dataloaders = utils.get_loaders(args)
    for i in range(100):
        data_train = next(iter(dataloaders['train']))
        data_val = next(iter(dataloaders['train']))
        vis_train_A = utils.make_numpy_grid(data_train['A'])
        vis_train_B = utils.make_numpy_grid(data_train['B'])
        vis_val_A = utils.make_numpy_grid(data_val['A'])
        vis_val_B = utils.make_numpy_grid(data_val['B'])
        vis = np.concatenate([vis_train_A, vis_train_B, vis_val_A, vis_val_B], axis=0)
        print(data_train['A'].shape)
        print(data_train['B'].shape)
        print(data_val['A'].shape)
        print(data_val['B'].shape)
        plt.imshow(vis)
        plt.show()