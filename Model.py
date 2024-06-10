class Folder:
    path = ""
    frameSize = ""

    def FrameSizeCheck(): # 不用这个方法做, 用字典in / not in 匹配字符; 输入端也是用数字0-9去选, 然后回来选倍率
        pass


class Photo:
    model = ""
    lens_model = ""
    datetime_original = ""
    focal_length = 0
    fl_to_35mm = 0
    f_number = 0
    photographic_sensitivity = 0
    exposure_time = 0