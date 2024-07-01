class PreConfig(object):
    frameSizes = {
        "0" : 0.8,
        "1" : 1.0,
        "2" : 1.5,
        "3" : 1.6,
        "4" : 2.0,
        "5" : 1.5
    }
    fs_options = "\n[0]:4433 Medium Format(0.8x) \n[1]:Full Frame(1.0x) \n[2]:APS-C(1.5x) \n[3]:APS-C(1.6x) \n[4]:M43(2.0x) \n[5]:M43(1.5x)"

    classicFLs = [14, 16, 20, 24, 28, 30, 35, 50, 65, 70, 85, 100, 105, 135]
    classicAperture = [1.2, 1.4, 1.8, 2.0, 2.8, 4, 5.6, 8.0, 11, 16, 22]


# not used
class Folder(object):
    path = ""
    frameSize = ""


class Photo(object):
    model = ""
    lens_model = ""
    datetime_original = ""
    focal_length = 0
    focal_length_in_35mm_film = 0
    f_number = 0
    photographic_sensitivity = 0
    exposure_time = 0