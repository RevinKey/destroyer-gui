from Tkinter import *
import subprocess
from ImageTk import *


class MenuBar(Tkinter.Menu):
    def __init__(self, parent):
        Tkinter.Menu.__init__(self, parent)

        fileMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=fileMenu)
        fileMenu.add_command(label="About", underline=1, command=self.about)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

    def about(self):
        a = Tkinter.Tk()
        a.title("About Page")

    def quit(self):
        sys.exit(0)


class App(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.grid()
        menubar = MenuBar(self)
        self.wm_title("Destroyer")
        self.config(menu=menubar, bg='#000000')
        Tkinter.Image = PhotoImage(file="des.gif")
        l2 = Tkinter.Label(image=Tkinter.Image, bg='#000000').pack(fill="x")

        quote = """
        The quiter and less obvious you become  \nthe more you will prosper...
        """

        self.label3 = Tkinter.Label(self, text=quote, justify='left', bg='#290e1e', fg='#eeffdd').pack(side="right")

        explain = """
        "What mischief would you like to do today sir?"
        "URL XXS and CSRF"
        "OSINT"
        "Macchager"
        "NMAP: Scan Network"
        "Wifi honey"
        "The backdoor factory: backdoor an image"
        "Encoded Metasploit backdoor generator"
        "Torify: run an app through tor"""
        self.label1 = Tkinter.Label(self, text=explain, justify='left', bg='#290e1e', fg='#eeffdd').pack(side="left")

        but1 = Tkinter.Button(self, text='Website analysis', command=self.xss).pack()
        but2 = Tkinter.Button(self, text='OSINT', command=self.osint).pack()
        but3 = Tkinter.Button(self, text='MAC-CHANGE', command=self.Mac).pack()
        but4 = Tkinter.Button(self, text="NMAP", command=self.nmap).pack()
        but5 = Tkinter.Button(self, text='Wifi Honey', command=self.honey).pack()
        but6 = Tkinter.Button(self, text='Backdoor Factory', command=self.bdf).pack()
        but7 = Tkinter.Button(self, text='Encoded BackDoors', command=lambda: subprocess.check_call(["python", "tryme.py"])).pack()
        but8 = Tkinter.Button(self, text='Torify', command=self.torify).pack()
        but9 = Tkinter.Button(self, text='misc', command=lambda: subprocess.check_call(["xfce4-terminal"])).pack()

    def xss(self):
        x = Tkinter.Tk()
        x.title("xssya startup")
        import xssya


    def osint(self):
        osint = Tkinter.Tk()
        osint.title("OSINT")
        osint.menubar = MenuBar(osint)

        label1 = Label(osint, text="Open Source Intelligence Gathering").pack(fill="x")
        osint.but1 = Tkinter.Button(osint, text="WhoIs", command=self.whois).pack()
        osint.but2 = Tkinter.Button(osint, text="dARK mAGIc", command=self.dark).pack()
        osint.but3 = Tkinter.Button(osint, text="TekDefender", command=self.tek).pack()
        osint.but4 = Tkinter.Button(osint, text="Harvester", command=self.harvest).pack()

    def harvest(self):
        h = Tkinter.Tk()
        h.title("Harvester")
        h.menubar = MenuBar(h)
        label2 = Label(h, text="what is the url or Company name of the target?: ").pack()
        target = Tkinter.Entry(h)
        target.pack()
        target.insert(0, "URL/Company name")
        but = Button(h, text="Run!", command=lambda: subprocess.check_call(
            ["theharvester", "-d", target.get(), "-l", "200", "-b", "all"]))

    def dark(self):
        d = Tkinter.Tk()
        d.title("DarkMagic")
        d.menubar = MenuBar(d)
        label1 = Label(d, text="what is the Target URL or IP?: ").pack()
        target = Tkinter.Entry(d)
        target.pack()
        target.insert(0, "IP/URL")
        d.Button = Button(d, text="Run!", command=lambda: subprocess.check_call(["whois", target.get()]).pack())


    def tek(self):
        tek = Tkinter.Tk()
        tek.title("TekDefender")
        tek.menubar = MenuBar(tek)

        label1 = Label(tek, text="TekDefender").pack(fill="x")
        label2 = Label(tek, text="what is the url or Company name of the target?: ").pack(side="left")
        target = Tkinter.Entry(tek)
        target.pack()
        target.insert(0, "URL/Company name")

        tek.Button = Button(tek, text="Run!", command=lambda: subprocess.check_call(["automater", target.get()])).pack()

    def whois(self):
        who = Tkinter.Tk()
        who.title("WhoIs info search")
        label1 = Label(who, text="Please enter the IP or URL: ").pack(side="right")
        target = Tkinter.Entry(who)
        target.pack()
        target.insert(0, "IP/URL")
        who.Button = Button(who, text="Run!", command=lambda: subprocess.check_call(["whois", target.get()]).pack())

    def Mac(self):
        a = Tkinter.Tk()
        a.title("Change MAC")
        a.menubar = MenuBar(a)
        apptext = Tkinter.Label(a, text="What is the interface you want to change?: ").pack()
        a.myentrybox = Tkinter.Entry(a)
        a.myentrybox.pack()
        a.myentrybox.insert(0, "some interface")
        a.but1 = Tkinter.Button(a, text="Enter",
                                command=lambda: subprocess.check_call(["macchanger", "-r", a.myentrybox.get()])).pack(
            side="right")

    def torify(self):
        a = Tkinter.Tk()
        a.title("Torify")
        a.menubar = MenuBar(a)
        apptext = Tkinter.Label(a, text="What is the application you want to run under tor: ").pack()
        a.myentrybox = Tkinter.Entry(a)
        a.myentrybox.pack()
        a.myentrybox.insert(0, "some application")
        a.but1 = Tkinter.Button(a, text="Enter",
                                command=lambda: subprocess.check_call(["torify", a.myentrybox.get()])).pack(
            side="right")


    def nmap(self):
        nmap = Tkinter.Tk()
        nmap.title("NMAP")
        nmap.menubar = MenuBar(nmap)
        apptext = Tkinter.Label(nmap, text="Welcome to my NMAP interactive menu").pack(side="top")
        apptext1 = Tkinter.Label(nmap, text="what is your target?: (ie. 192.168.0.0/24)").pack(fill="x")
        nmap.myentrybox = Tkinter.Entry(nmap)
        nmap.myentrybox.pack()
        nmap.myentrybox.insert(0, "some target")
        apptext2 = Tkinter.Label(nmap,
                                 text="what type of scan do you want to do? (ie. syn, tcp, tcpnull, xmas, udp, ping").pack(
            fill="x")
        v = StringVar()
        x = StringVar()

        nmap.myentrybox1 = Tkinter.Entry(nmap, textvariable=v)
        nmap.myentrybox1.pack()
        nmap.myentrybox1.insert(0, "scan type")

        apptext3 = Tkinter.Label(nmap, text="Paranoid Level?: (ie. t1 t2 t3 t4)").pack(fill="x")
        nmap.myentrybox2 = Tkinter.Entry(nmap, textvariable=x)
        nmap.myentrybox2.pack()
        nmap.myentrybox2.insert(0, "paranoid level")
        nmap.scan = StringVar()
        nmap.paranoid = StringVar()

        def checkbox1(nmap):
            if v.get() == ('ping'):
                nmap.scan = "-sn"
            elif v.get() == ('udp'):
                nmap.scan = "-sU"
            elif v.get() == ('xmas'):
                nmap.scan = "-sX"
            elif v.get() == ('tcpnull'):
                nmap.scan = "-sN"
            elif v.get() == ('udp'):
                nmap.scan = "-sU"
            elif v.get() == ('tcp'):
                nmap.scan = "-sT"
            elif v.get() == ('syn'):
                nmap.scan = "-sS"
            else:
                nmap.scan = "-sn"
        def checkbox2(nmap):
            if x.get() in ('t4', '4', 'T4'):
                nmap.paranoid = "-T4"
            elif x.get() in ('t3', '3', 'T3'):
                nmap.paranoid = "-T3"
            elif x.get() in ('t2', '2', 'T2'):
                nmap.paranoid = "-T2"
            elif x.get() in ('t1', '1', 'T1'):
                nmap.paranoid = "-T1"
            else:
                nmap.paranoid = "-T3"


        apptext4 = Tkinter.Label(nmap, text="Output location?:").pack(fill="x")
        nmap.myentrybox3 = Tkinter.Entry(nmap)
        nmap.myentrybox3.pack()
        nmap.myentrybox3.insert(0, "some file")

        nmap.but1 = Tkinter.Button(nmap, text="Enter", command=lambda: subprocess.check_call(["nmap", nmap.scan, nmap.paranoid, nmap.myentrybox.get(), "-oG", nmap.myentrybox3.get()])).pack(side="right")

    def honey(self):
        honey = Tkinter.Tk()
        honey.title("Wifi Honey")
        honey.menubar = MenuBar(honey)
        apptext = Tkinter.Label(honey, text="Welcome to my Wifi-Honey interactive menu").pack(side="top")
        apptext1 = Tkinter.Label(honey, text="what is the essid?:").pack(fill="x")
        honey.myentrybox = Tkinter.Entry(honey)
        honey.myentrybox.pack()
        honey.myentrybox.insert(0, "some target")

        apptext2 = Tkinter.Label(honey, text="What is the channel you want to broadcast on?").pack(fill="x")
        honey.myentrybox1 = Tkinter.Entry(honey)
        honey.myentrybox1.pack()
        honey.myentrybox1.insert(0, "11")

        apptext3 = Tkinter.Label(honey, text="what is the interface to use on your machine?:").pack(fill="x")
        honey.myentrybox2 = Tkinter.Entry(honey)
        honey.myentrybox2.pack()
        honey.myentrybox2.insert(0, "wlan0")

        honey.but1 = Tkinter.Button(honey, text="Enter", command=lambda: subprocess.check_call(
            ["wifi-honey", honey.myentrybox.get(), honey.myentrybox1.get(), honey.myentrybox2.get()])) \
            .pack(side="right")


    def bdf(self):
        bdf = Tkinter.Tk()
        bdf.title("backdoorFactory")
        bdf.menubar = MenuBar(bdf)
        apptext = Tkinter.Label(bdf, text="Welcome to my Backdoor Factory interactive menu").pack(side="top")
        apptext1 = Tkinter.Label(bdf,
                                 text="what is the Directory containing the images you want to inject the backdoor into?:").pack(
            fill="x")
        bdf.myentrybox = Tkinter.Entry(bdf)
        bdf.myentrybox.pack()
        bdf.myentrybox.insert(0, "path")

        apptext2 = Tkinter.Label(bdf, text="Do you have a predefined payload?:").pack(fill="x")
        bdf.myentrybox1 = Tkinter.Entry(bdf)
        bdf.myentrybox1.pack()
        bdf.myentrybox1.insert(0, "yes or no")
        # #if yes load payload if no ask question and make one.need to still figure out how to check the user input.

        apptext3 = Tkinter.Label(bdf, text="what is the IP you are Listening to?:").pack(fill="x")
        bdf.myentrybox2 = Tkinter.Entry(bdf)
        bdf.myentrybox2.pack()
        bdf.myentrybox2.insert(0, "IP")

        apptext4 = Tkinter.Label(bdf, text="what is the Port you are Listening on?:").pack(fill="x")
        bdf.myentrybox3 = Tkinter.Entry(bdf)
        bdf.myentrybox3.pack()
        bdf.myentrybox3.insert(0, "port")
        bdf.but1 = Tkinter.Button(bdf, text="Enter", command=lambda: subprocess.check_call(
            ["backdoor-factory", "-d", bdf.myentrybox.get(), "-s", bdf.myentrybox1.get(), "-h", bdf.myentrybox2.get(),
             "-P", bdf.myentrybox3.get()])).pack(side="right")


if __name__ == "__main__":
    app = App()
    app.mainloop()