from functools import partial

def csp_checker(v):
    print("\r\n\r\n[+] -----------CSP-------------\t")
    csp_arr=['default-src',' upgrade-insecure-requests','block-all-mixed-content','script-src','style-src','img-src','media-src','font-src','frame-src','object-src','child-src','worker-src','manifest-src']
    csp=v.replace('; ',';').replace('/http',' http')
    #print(re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(csp)))
    csp=csp.split(';')
    got_headers=[]
    for i in csp[:-1]:
        #print("\033[31m"+i.split(' ')[0]+":\033[32m"+(''.join(i.split(' ')[1:]))+"\033[0m")
        csper(str(i.split(' ')[0]),(''.join(i.split(' ')[1:])))
        got_headers.append(i.split(' ')[0])
    a=list(set(csp_arr)-set(got_headers))
    print("  | A Few CSP-Header's Not Found")
    print(*a, sep = "  |"+ "\033[31m ")  
    print("  | \033[0m")


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