from functools import partial

def csper(csp,v):
    switcher = {
        'default-src': partial(default_src,v),
        'script-src': partial(script_src,v),
        'img-src': partial(img_src,v),
        'media-src': partial(media_src,v),
        'font-src': partial(font_src,v),
        'frame-src': partial(frame_src,v),
        'object-src': partial(object_src,v),
        'child-src': partial(child_src,v),
        'worker-src': partial(worker_src,v),
        'manifest-src': partial(manifest_src,v),
    }    
    func = switcher.get(csp.lower(), lambda: "")
    print(func().replace('http',' http').replace('\'\'','\' \'')+"\033[0m")


def default_src(v):
    u=v.replace('http',' http').split(' ')
    print(u)
    return '\033[34mdefautl-src:\033[32m'+v

def script_src(v):
    u=v.split(' ')
    print(u)
    return '\033[34mscript_src:\033[32m'+v

def img_src(v):
    return '\033[34mimg_src:\033[32m'+v

def media_src(v):
    return '\033[34mmedia_src:\033[32m'+v

def font_src(v):
    return '\033[34mfont_src:\033[32m'+v

def frame_src(v):
    return '\033[34mframe_src:\033[32m'+v

def object_src(v):
    return '\033[34mobject_src:\033[32m'+v

def child_src(v):
    return '\033[34mchild_src:\033[32m'+v

def worker_src(v):
    return '\033[34mworker_src:\033[32m'+v

def manifest_src(v):
    return '\033[34mmanifest_src:\033[32m'+v