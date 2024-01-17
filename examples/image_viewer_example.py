import uix

from uix.elements import container, file

from uix_components import image_viewer, basic_alert

events = [
        ["zoom-in", "Zoom in"],
        ["zoom-out", "Zoom out"],
        ["home", "Home"],
        ["fullscreen", "Full Page"],
        ["download", "Download"],
        ["save", "Save"],
    ]

def on_button_click(ctx, id, value):
    print("on_button_click",id,value)
    ctx.elements["alert1"].open("alert-success",value)
    # if value == "zoom-in":
    #     ctx.elements["iw1"].zoom_in()
    # elif value == "zoom-out":
    #     ctx.elements["iw1"].zoom_out()
    # elif value == "home":
    #     ctx.elements["iw1"].home()
    # elif value == "fullscreen":
    #     ctx.elements["iw1"].fullscreen()
    # elif value == "download":
    #     ctx.elements["iw1"].download()
    # elif value == "save":
    #     ctx.elements["iw1"].save()


def on_upload(ctx, id, event, data, status):
    print("on_upload", id, event, data, status)
    if status == "done":
        iw = ctx.session.elements["iw1"]
        if event == "select":
            iw.value = data[0].url
        
def image_viewer_example():      
    with container() as main: 
        file(id="file1",accept="image/*",multiple=False,callback=on_upload).cls("center")
        iw1 = image_viewer(id = "iw1", value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png",hasButtons=True).size(600,720)
        iw1.on("button_click",on_button_click)
        basic_alert("Image Viewer",id="alert1",type="success")
    return main
