from nicegui import events, ui

def draw_bbox():
    # previous_rect = None

    global draw
    draw = False
    # gt_content = None
    def mouse_handler(e: events.MouseEventArguments):
        global previous_rect, draw, gt_content
        color = 'SteelBlue'
        # ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
        if e.type =='mousedown':
            draw = True
            gt_content = ii.content
            init_xy.extend([int(e.image_x), int(e.image_y)])
        elif (e.type == 'mousemove') and draw:
            previous_rect = gt_content
            curr_x = int(e.image_x)
            curr_y = int(e.image_y)
            previous_rect += f'<rect width="{curr_x - init_xy[0]}" height="{curr_y-init_xy[1]}" x="{init_xy[0]}" y="{init_xy[1]}" fill="none" stroke="{color}"/>'
            ii.content = previous_rect
        elif e.type == 'mouseup':
            curr_x = int(e.image_x)
            curr_y = int(e.image_y)
            ii.content = gt_content + f'<rect width="{curr_x - init_xy[0]}" height="{curr_y-init_xy[1]}" x="{init_xy[0]}" y="{init_xy[1]}" fill="none" stroke="{color}"/>'
            ui.notify(f'roi drawing is finished.')
            gt_content = ii.content
            init_xy.clear()
            draw = False
    
    init_xy = []
    src = 'https://picsum.photos/id/565/640/360'
    ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup','mousemove'], cross=True)

    ui.run()

if __name__ in ("__main__","__mp_main__"):
    draw_bbox()