import numpy as np
from tqdm import tqdm

map_ids = ["udai-01", "udai-02", "udai-03", "udai-04", "udai-05-06", "udai-07", "udai-08", "udai-09", "udai-10"]

def load_npz(map_file):
    return np.load(map_file, allow_pickle=True)

def extract_data(npz):
    mean = npz["Mean"]
    var = npz["Var"]
    macdict = npz["macdict"]
    gp_data = [mean, var, macdict]
    return gp_data



if __name__ == "__main__":
    error_map_list = []
    for idx, map_id in tqdm(enumerate(map_ids)):
        print("---------------------------------")
        print(f"checking now map_id = {map_id}")
        mapfile_name_1 = f"/mnt/matrix/rosbag/processed_data/nict/{map_id}/invisible-maps/{map_id}_WifiMap_res_025.npz"
        mapfile_name_2 = f"/mnt/matrix/rosbag/processed_data/nict/{map_id}/invisible-maps/{map_id}_WifiMap_res_050.npz"
        mapfile_name_3 = f"/mnt/matrix/rosbag/processed_data/nict/{map_id}/invisible-maps/{map_id}_WifiMap_res_100.npz"
        
        npz_1 = load_npz(mapfile_name_1)
        npz_2 = load_npz(mapfile_name_2)
        npz_3 = load_npz(mapfile_name_3)
        
        npz_list = [npz_1, npz_2, npz_3]

        for npz in npz_list:
            try:
                gp_data_ = extract_data(npz=npz)

            except:
                print('Error')
                error_map_list.append(map_id)
        
    print(f"Errored  map_id = {error_map_list}")

