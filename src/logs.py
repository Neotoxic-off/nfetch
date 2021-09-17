class LOGS:
    data = {
        "reset" : "0",
        "black" : "30",
        "red" : "31",
        "green" : "32",
        "yellow" : "33",
        "blue" : "34",
        "purple" : "35",
        "cyan" : "36",
        "white" : "37"
    }
    back_color = {
        "reset" : "0",
        "black" : "40",
        "red" : "41",
        "green" : "42",
        "yellow" : "43",
        "blue" : "44",
        "purple" : "45",
        "cyan" : "46",
        "white" : "47"
    }

    @classmethod
    def colors(cls, color, font, back):
        if (cls.data.get(color) != None and (font >= 0 and font <= 5)):
            if (back == "reset"):
                return ("\033[{};{}m".format(font, cls.data.get(color)))
            return ("\033[{};{};{}m".format(font, cls.data.get(color), cls.back_color.get(back)))
        return (None)

    @classmethod
    def status(cls, data, status, color, font, back, before = ''):
        print("{}{}  {}  {}  {}".format(
            before,
            cls.colors(color, font, back),
            status,
            cls.colors("reset", 0, "reset"),
            data
        ))

    @classmethod
    def launch(cls, data):
        cls.status(data, " .... ", "black", 1, "blue")

    @classmethod
    def coverage(cls, data):
        if (float(data) >= 75.0):
            cls.status("coverage: {}%".format(data), "result", "black", 1, "green", '\n')
        elif (float(data) >= 50):
            cls.status("coverage: {}%".format(data), "result", "black", 1, "cyan", '\n')
        elif (float(data) >= 25):
            cls.status("coverage: {}%".format(data), "result", "black", 1, "yellow", '\n')
        else:
            cls.status("coverage: {}%".format(data), "result", "black", 1, "red", '\n')


    @classmethod
    def ok(cls, data):
        cls.status(data, "passed", "black", 1, "green")

    @classmethod
    def ko(cls, data):
        cls.status(data, "failed", "black", 1, "red")

    @classmethod
    def done(cls, data):
        cls.status(data, " done ", "black", 1, "green")

    @classmethod
    def fail(cls, data):
        cls.status(data, " fail ", "black", 1, "red")
    
    @classmethod
    def load(cls, data):
        cls.status(data, " load ", "black", 1, "yellow")

    @classmethod
    def exiting(cls, data):
        cls.status(data, " exit ", "black", 1, "green")

    @classmethod
    def name(cls, data):
        cls.status(data, " name ", "black", 1, "cyan")

    @classmethod
    def desc(cls, data):
        cls.status(data, " desc ", "black", 1, "cyan")
    
    @classmethod
    def version(cls, data):
        cls.status(data, " vers ", "black", 1, "cyan")

