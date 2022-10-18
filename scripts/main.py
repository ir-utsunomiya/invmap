import argparse


#コマンドライン引数を設定
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--map_root_dir", default="/home/hiro/data/invisible-maps/", help="地図や電場強度データが入っているディレクトリを指定してください")
    parser.add_argument("-i", "--map_id", default="udai-02", help="udai-01など，地図や電場強度データの識別に使っている部分を指定してください")
    parser.add_argument("--save_model_flag", type=int, choices=[0, 1], default=0, help="計算したマップのデータサイズをcsv形式で保存するかのflagです。保存する場合は 1 を指定してください。")
    parser.add_argument("--save_mode_dir", default="/home/hiro/venv_devel/wifi_devel/csvs_dir/", help="dataframeを出力したcsvを保存するディレクトリを指定してください")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    print()