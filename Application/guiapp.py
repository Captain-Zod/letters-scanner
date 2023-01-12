import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk
from skimage import io, filters
import consoleapp, config

range = 50
extention = ".jpg"
path = "photo" + extention

class MousePositionTracker(tk.Frame):
    """ Tkinter Canvas mouse position widget. """

    def __init__(self, canvas):
        self.canvas = canvas
        self.canv_width = self.canvas.cget('width')
        self.canv_height = self.canvas.cget('height')
        self.reset()

        # Create canvas cross-hair lines.
        xhair_opts = dict(dash=(3, 2), fill='black', state=tk.HIDDEN)
        self.lines = (self.canvas.create_line(0, 0, 0, self.canv_height, **xhair_opts),
                      self.canvas.create_line(0, 0, self.canv_width,  0, **xhair_opts))

    def cur_selection(self):
        return (self.start, self.end)

    def begin(self, event):
        self.hide()
        self.start = (event.x, event.y)  # Remember position (no drawing).

    def update(self, event):
        self.end = (event.x, event.y)
        self._update(event)
        self._command(self.start, (event.x, event.y))  # User callback.

    def _update(self, event):
        # Update cross-hair lines.
        #self.canvas.coords(self.lines[0], event.x, 0, event.x, self.canv_height)
        #self.canvas.coords(self.lines[1], 0, event.y, self.canv_width, event.y)
        #self.show()
        a = 1

    def reset(self):
        self.start = self.end = None

    def hide(self):
        self.canvas.itemconfigure(self.lines[0], state=tk.HIDDEN)
        self.canvas.itemconfigure(self.lines[1], state=tk.HIDDEN)

    def show(self):
        self.canvas.itemconfigure(self.lines[0], state=tk.NORMAL)
        self.canvas.itemconfigure(self.lines[1], state=tk.NORMAL)

    def autodraw(self, command=lambda *args: None):
        """Setup automatic drawing; supports command option"""
        self.reset()
        self._command = command
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<B1-Motion>", self.update)
        self.canvas.bind("<ButtonRelease-1>", self.quit)

    def quit(self, event):
        self.hide()  # Hide cross-hairs.
        self.reset()


class SelectionObject:
    """ Widget to display a rectangular area on given canvas defined by two points
        representing its diagonal.
    """
    def __init__(self, canvas, select_opts):
        # Create attributes needed to display selection.
        self.canvas = canvas
        self.select_opts1 = select_opts
        self.width = self.canvas.cget('width')
        self.height = self.canvas.cget('height')

        # Options for areas outside rectanglar selection.
        select_opts1 = self.select_opts1.copy()  # Avoid modifying passed argument.
        select_opts1.update(state=tk.HIDDEN)  # Hide initially.
        # Separate options for area inside rectanglar selection.
        select_opts2 = dict(dash=(2, 2), fill='', outline='black', state=tk.HIDDEN)

        # Initial extrema of inner and outer rectangles.
        imin_x, imin_y,  imax_x, imax_y = 0, 0,  0, 0
        omin_x, omin_y,  omax_x, omax_y = 0, 0,  self.width, self.height

        self.rects = [
            # Area *outside* selection (inner) rectangle.
            #self.canvas.create_rectangle(omin_x, omin_y,  omax_x, imin_y, **select_opts1),
            #self.canvas.create_rectangle(omin_x, imin_y,  imin_x, imax_y, **select_opts1),
            #self.canvas.create_rectangle(imax_x, imin_y,  omax_x, imax_y, **select_opts1),
            #self.canvas.create_rectangle(omin_x, imax_y,  omax_x, omax_y, **select_opts1),
            # Inner rectangle.
            self.canvas.create_rectangle(imin_x, imin_y,  imax_x, imax_y, **select_opts2)
        ]

    def update(self, start, end):
        # Current extrema of inner and outer rectangles.
        imin_x, imin_y,  imax_x, imax_y = self._get_coords(start, end)
        omin_x, omin_y,  omax_x, omax_y = 0, 0,  self.width, self.height
        imax_x = end[0]
        imax_y = end[1]

        # Update coords of all rectangles based on these extrema.
        #self.canvas.coords(self.rects[0], omin_x, omin_y,  omax_x, imin_y),
        #self.canvas.coords(self.rects[1], omin_x, imin_y,  imin_x, imax_y),
        #self.canvas.coords(self.rects[2], imax_x, imin_y,  omax_x, imax_y),
        #self.canvas.coords(self.rects[3], omin_x, imax_y,  omax_x, omax_y),
        self.canvas.coords(self.rects[0], imax_x - range, imax_y - range,  imax_x + range, imax_y + range),

        for rect in self.rects:  # Make sure all are now visible.
            self.canvas.itemconfigure(rect, state=tk.NORMAL)

    def _get_coords(self, start, end):
        """ Determine coords of a polygon defined by the start and
            end points one of the diagonals of a rectangular area.
        """
        return (min((start[0], end[0])), min((start[1], end[1])),
                max((start[0], end[0])), max((start[1], end[1])))

    def hide(self):
        for rect in self.rects:
            self.canvas.itemconfigure(rect, state=tk.HIDDEN)


class Application(tk.Frame):

    # Default selection object options.
    SELECT_OPTS = dict(dash=(2, 2), stipple='gray25', fill='red',
                          outline='')

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        i = Image.open(path)
        img = ImageTk.PhotoImage(i)
        self.canvas = tk.Canvas(width=500, height=500,
                                borderwidth=0, highlightthickness=0)
        self.h = i.height
        self.w = i.width

        self.sbarV = Scrollbar(self, orient=VERTICAL)
        self.sbarH = Scrollbar(self, orient=HORIZONTAL)

        self.sbarV.config(command=self.canvas.yview)
        self.sbarH.config(command=self.canvas.xview)

        self.canvas.config(yscrollcommand=self.sbarV.set)
        self.canvas.config(xscrollcommand=self.sbarH.set)


        self.canvas.pack(fill=BOTH, side=BOTTOM, expand=True)
        self.canvas.create_image(0, 0, image=img, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.canvas.img = img  # Keep reference.
        self.sbarV.pack(side=RIGHT, fill=Y)
        self.sbarH.pack(side=BOTTOM, fill=X)

        # Create selection object to show current selection boundaries.
        self.selection_obj = SelectionObject(self.canvas, self.SELECT_OPTS)

        # Callback function to update it given two points of its diagonal.
        def on_drag(start, end, **kwarg):  # Must accept these arguments.
            self.curr = end
            self.selection_obj.update(start, end)

        # Create mouse position tracker that uses the function.
        self.posn_tracker = MousePositionTracker(self.canvas)
        self.posn_tracker.autodraw(command=on_drag)  # Enable callbacks.

        self.plus = Button(text='+', command=self.plu)
        self.plus.pack(padx=15, pady=15)
        self.min = Button(text='-', command=self.minu)
        self.min.pack(padx=15, pady=15)
        self.btn_text = tk.StringVar(value="Here!")
        self.scanner = Button(textvariable=self.btn_text, command=self.scan)
        self.scanner.pack(padx=15, pady=15)
    
    def plu(self):
        # open image to resize it
        image = Image.open(path)
        # resize the image with width and height of root
        self.h = int(self.h * 1.1)
        self.w = int(self.w * 1.1)
        resized = image.resize((self.w, self.h), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, image=image2, anchor='nw')
        self.canvas.img = image2

        self.selection_obj = SelectionObject(self.canvas, self.SELECT_OPTS)
        def on_drag(start, end, **kwarg):  # Must accept these arguments.
            self.curr = end
            self.selection_obj.update(start, end)

        # Create mouse position tracker that uses the function.
        
        self.posn_tracker = MousePositionTracker(self.canvas)
        self.posn_tracker.autodraw(command=on_drag)  # Enable callbacks.

    def minu(self):
        # open image to resize it
        image = Image.open(path)
        # resize the image with width and height of root
        self.h = int(self.h * 0.9)
        self.w = int(self.w * 0.9)
        resized = image.resize((self.w, self.h), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, image=image2, anchor='nw')
        self.canvas.img = image2

        self.selection_obj = SelectionObject(self.canvas, self.SELECT_OPTS)
        def on_drag(start, end, **kwarg):  # Must accept these arguments.
            self.curr = end
            self.selection_obj.update(start, end)

        # Create mouse position tracker that uses the function.
        self.posn_tracker = MousePositionTracker(self.canvas)
        self.posn_tracker.autodraw(command=on_drag)  # Enable callbacks.
    
    def scan(self):
        # open image to resize it
        image = Image.open(path)
        # resize the image with width and height of root
        resized = image.resize((self.w, self.h), Image.ANTIALIAS)
        left = self.curr[0] - range
        right =  self.curr[0] + range
        up =  self.curr[1] - range
        down =  self.curr[1] + range
        crop = resized.crop([ left, up, right, down])
        crop.save("tempo" + extention)

        image = io.imread("tempo" + extention)
        edges = filters.meijering(image) if config.DOFILTER else image
        res = consoleapp.find(edges)
        self.btn_text.set(res)

    def change(self):
        # open image to resize it
        image = Image.open(path)
        # resize the image with width and height of root
        y = max(image.width, self.winfo_width())
        x = max(image.height, self.winfo_height())
        resized = image.resize((y, x), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, image=image2, anchor='nw')
        self.canvas.img = image2


if __name__ == '__main__':

    WIDTH, HEIGHT = 900, 900
    BACKGROUND = 'grey'
    TITLE = 'Image Cropper'

    root = tk.Tk()
    root.title(TITLE)
    root.geometry('%sx%s' % (WIDTH, HEIGHT))
    root.configure(background=BACKGROUND)

    app = Application(root, background=BACKGROUND)
    app.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
    app.mainloop()

