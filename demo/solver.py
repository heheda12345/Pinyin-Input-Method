from ime import solve, init

class Solver(object):
    def __init__(self):
        self.waiting = ""
        self.buffer = ""
        self.newText = ""
        self.page = 0
        self.wl = []
        init()

    def capture(self, keyCode):
        self.newText = ""
        prePage = self.page
        self.page = 0
        
        if keyCode >= 65 and keyCode <= 90: #a-z
            self.buffer = self.buffer + chr(ord('a') + keyCode - 65)
            return True

        if self.buffer == "":
            return False

        if keyCode >= 49 and keyCode <= 57: #1-9
            wl = self.getWaitingList(prePage)
            idx = keyCode - 49
            if idx > len(wl):
                return False
            self.newText = wl[idx]
            self.buffer = ""
            return True

        elif keyCode == 16777248: #shift
            self.newText = self.buffer
            self.buffer = ""
            return True
            
        elif keyCode == 16777219: # backspace
            self.buffer = self.buffer[:-1]
            return True

        elif keyCode == 32: # space
            self.buffer = self.buffer + ' '
            return True

        elif keyCode == 61: # next page
            wl = self.wl
            if len(wl) > (prePage+1)*9:
                self.page = prePage + 1
            else:
                self.page = prePage
            return True

        elif keyCode == 45: # pre page
            if prePage > 0:
                self.page = prePage - 1
            else:
                self.page = prePage
            return True
        else:
            return False

    def updateWaitingList(self):
        self.wl = solve(self.buffer)

    def getWaitingList(self, page=-1):
        if page == -1:
            page = self.page
        return self.wl[page * 9: min(page * 9 + 9, len(self.wl))]
