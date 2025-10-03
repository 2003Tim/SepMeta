import numpy as np
import torch
from model.trainer.fsl_trainer import FSLTrainer
from model.utils import (
    pprint, set_gpu,
    get_command_line_parser,
    postprocess_args,
)
# from ipdb import launch_ipdb_on_exception

if __name__ == '__main__':
    parser = get_command_line_parser()
    args = postprocess_args(parser.parse_args())
    # with launch_ipdb_on_exception():
    # pprint(vars(args))

    set_gpu(args.gpu)
    trainer = FSLTrainer(args)

    # args.save_path = './checkpoints/MiniImageNet-ProtoNet-Res12-05w05s15q-Pre-DIS/' \
    #                  'Pipeline_PN_0.4_wd:0.0001_30.0_re_lr0.0001'
    # args.save_path = './checkpoints/MiniImageNet-ProtoNet-Res12-05w05s15q-Pre-DIS/' + args.test_model  #有修改
    # 修改为（提取 init_weights 路径中的模型文件夹部分）
    import os.path as osp

    # 从 init_weights 路径中解析出模型保存的文件夹路径
    # 例如：从 "/path/to/max_acc.pth" 中提取 "/path/to/"
    args.save_path = osp.dirname(args.init_weights)

    # print("\nTest with Max Prob Acc: ")
    # trainer.evaluate_test()

    print("Test with Max Acc: ")
    trainer.evaluate_test()

    # print("\nTest with last epoch: ")
    # trainer.evaluate_test('last.pth')

    # trainer.final_record()
    print(args.save_path)




#!/usr/bin/python
#coding=utf-8
# ==============================================================================
#
#       Filename:  demo.py
#    Description:  excel operat
#        Created:  Tue Apr 25 17:10:33 CST 2017
#         Author:  Yur
#
# ==============================================================================

import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

# 参数对应 行, 列, 值
worksheet.write(1,0, label = 'this is test')
workbook.save('Excel_test.xls')