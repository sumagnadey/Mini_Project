import new_vision_audio as nv_aud
import new_vision_utils as nv_utils

if __name__ == "__main__":
    nv_utils.initWish()
    
    while True:
        req = nv_aud.input_cmd().lower()
        
        if  'tell me' in req:
            nv_utils.hndlWiki(req)

        elif 'youtube' in req:
            nv_utils.hndlYT()
            break

        elif 'play music' in req:
            nv_utils.hndlMusic()
            break
        
        elif 'time' in req:
            nv_utils.hndlTime()
            break
        
        elif  'code' in req:
            nv_utils.hndlVsCode()
            break
        
        elif 'send Email' in req:
            nv_utils.hndlMail()
            break
        elif  'bye' in req:
            nv_utils.goodBye()
            break
