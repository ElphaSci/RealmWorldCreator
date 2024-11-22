from PIL import Image, ImageTk

from pic_info import PicInfo


def scale_image(pil_image: Image, y_depth: int, p56_info: PicInfo, race='default'):
    """
    Scales pil_im to the appropriate size, using the scaling parameters from pic_info, and given the y_depth

    :param pil_image: PIL Image to be scaled
    :param y_depth: new y-depth to scale pil_image to
    :param p56_info: information regarding the scaling with respect to the current background pic

    returns a scaled ImageTk, a scaling factor, and a scaled PIL Image
    """
    # Handle 3 cases of scaling; there is a back and front limit for scaling, based on the p56 background
    if p56_info.back_y < y_depth < p56_info.front_y:
        slope = p56_info.slope()
        const = p56_info.scale_constant()
        new_scale = slope * y_depth + const
        race_adjustment = {'default': 100, 'human': 100, 'giant': 110, 'elf': 90}
        scale_factor = (new_scale * race_adjustment[race]) / 100
    elif y_depth >= p56_info.front_y:
        scale_factor = p56_info.frontPercent()
    else:
        scale_factor = p56_info.backPercent()
    # Scale the image based on the calculated scale_factor
    new_shape = (int(pil_image.width * scale_factor), int(pil_image.height * scale_factor))
    scaled_pil_im = pil_image.resize(new_shape)
    tk_im = ImageTk.PhotoImage(scaled_pil_im)
    return tk_im, scale_factor, scaled_pil_im