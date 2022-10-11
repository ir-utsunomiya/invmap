import argparse
from ast import arg
import itertools
from logging import root
from socketserver import ThreadingUnixDatagramServer
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import GPy
from Localization.sensormodel.gp import GP
import time

from processdata import ProcessedData

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_dir", default="../datadir/", help="dataが入っているディレクトリを指定してください")
    #parser.add_argument("-m", "--multi_resolution", choices=[0, 1], help="地図の解像度(resolution)を複数用意して回すかのフラグ")
    parser.add_argument("-r", "--resolution", help="地図の解像度(resolution)を指定してください")
    #parser.add_argument("--model_save_dir",  default="/home/hiro/data/invisible-maps/", help="地図や電場強度データが入っているディレクトリを指定してください")
    parser.add_argument("-i", "--map_id", default="udai-01", help="地図のidを指定してください")
    parser.add_argument("save_model_flag", default=0, choices=[0, 1], help="modelを保存するか")
    #parser.add_argument("")
    args = parser.parse_args()
    return args 

class GPTraining:
    #def __init__(self, root_dir, map_id, resolution) -> None:
    def __init__(self, train_data, macdict) -> None:
       #self.map_path = 
        #self.wifidata_path = f"{root_dir}{map_id}/{map_id}_WiFiData.npz"
        self.train_data = train_data
        self.macdict = macdict
        #self.save_model_path = f"{}"

    def training(self):
        print("Training GP")
        time.sleep(0.2)
        
        kernel = GPy.kern.RBF(2)#+GPy.kern.RBF(2,lengthscale=5)

        start_time = time.time()
        model = GP(self.train_data.data, self.macdict) #GPモデルをインスタンス化
        model.optimize(kernel = kernel) #最適化の実行
        print(time.time - start_time) #最適化にかかった時間を計測

        print(model)

        return model

    def savemodel(self, root_dir, map_id, model):
        save_model_path = f"{root_dir}{map_id}/{map_id}_WiFiModel.npz"
        print(f"Saving Model, {save_model_path}")
        np.savez_compressed(save_model_path, param_array = model.gp.param_array)
        

def main():
    args = get_args()
    print(f"\n####################\n  map: {args.map_id} \n####################")
    time.sleep(0.2)
    data = np.load("../datadir/udai-01/udai-01_WifiData.npz")
    XY = data["XY"]
    Wifi = data["Wifi"]
    macdict = data["macdict"]
    train_data = ProcessedData(XY,Wifi,macdict)
    gptrainig = GPTraining(train_data, macdict)
    


<<<<<<< HEAD

=======
if __name__ == "__main__":
    #print(f"\n####################\n  map: {} \n####################"); time.sleep(0.2))
    main()
>>>>>>> 7b0f156ed0b434e12e2bf0507289d3df78303466
