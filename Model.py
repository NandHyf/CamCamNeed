class Folder:
    path = ""
    frameSize = ""

    def FrameSizeCheck(): # 不用这个方法做, 用字典in / not in 匹配字符; 输入端也是用数字0-9去选, 然后回来选倍率
        pass

    frameSizes = [0, 1, 2, 3] # [0]:Medium Format \n [1]:Full Frame \n [2]:APS-C \n [3]:M43
    fs_options = "\n [0]:Medium Format \n [1]:Full Frame \n [2]:APS-C \n [3]:M43 \n"
    # Equivalent Focal Length
    efl = {} # 用numpy 2d array做吧


class Photo:
    model = ""
    lens_model = ""
    datetime_original = ""
    focal_length = 0
    fl_to_35mm = 0
    f_number = 0
    photographic_sensitivity = 0
    exposure_time = 0