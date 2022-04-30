from _datetime import datetime
import random
import tkinter as tk
from tkinter import ttk
from tkinter import NORMAL, DISABLED
import re
import mysql.connector
from dataclasses import dataclass

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Testing#1", database="test")

mycursor = mydb.cursor()

newID = "12345"


def random_cid():
    global newID
    newID = random.randint(10000, 99999)
    return newID


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._mainCanvas = None
        # The dictionary to hold the class type to switch to
        # Each new class passed here, will only have instance or object associated with it (i.e the result of the Key)
        self._allCanvases = dict()
        # Switch (and create) the single instance of StartUpPage
        self.switch_Canvas(StartUpPage)

    def switch_Canvas(self, Canvas_class):

        # Unless the dictionary is empty, hide the current Frame (_mainCanvas is a frame)
        if self._mainCanvas:
            self._mainCanvas.pack_forget()

        # is the Class type passed one we have seen before?
        canvas = self._allCanvases.get(Canvas_class, False)

        # if Canvas_class is a new class type, canvas is False
        if not canvas:
            # Instantiate the new class
            canvas = Canvas_class(self)
            # Store it's type in the dictionary
            self._allCanvases[Canvas_class] = canvas

        # Pack the canvas or self._mainCanvas (these are all frames)
        canvas.pack(pady=60)
        # and make it the 'default' or current one.
        self._mainCanvas = canvas


class StartUpPage(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        tk.Frame(self)
        greeting = ttk.Label(self,
                             text="Welcome to the airport database! Please log in to perform actions, or create an account. ").grid(
            column=0, row=0)
        greeting2 = ttk.Label(self, text="You might be required to register to pursue some actions.").grid(column=0,
                                                                                                           row=1)
        loginPrompt = ttk.Label(self, text="Enter Customer ID: ").grid(column=0, row=2)
        text = tk.StringVar()
        entry1 = ttk.Entry(self, textvariable=text).grid(column=0, row=3)

        def getRandomCID():
            global newID
            newID = text.get()

        submit = ttk.Button(self, text="Submit",
                            command=lambda: [getRandomCID(), master.switch_Canvas(homescreen)]).grid(
            column=0, row=4, pady=7)

        createAccount = ttk.Button(self, text="Create Account",
                                   command=lambda: master.switch_Canvas(create_Account)).grid(
            column=0, row=5)


class create_Account(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        # first name
        firstname_label = ttk.Label(self, text="First name:")
        firstname_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
        firstname_entry = ttk.Entry(self)
        firstname_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        # last name
        lastname_label = ttk.Label(self, text="Last name:")
        lastname_label.grid(column=2, row=0, sticky=tk.NS, padx=5, pady=5)
        lastname_entry = ttk.Entry(self)
        lastname_entry.grid(column=3, row=0, sticky=tk.EW, padx=5, pady=5)

        # Date of Birth
        DOB_label = ttk.Label(self, text="DOB(YYYY-MM-DD):")
        DOB_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
        DOB_entry = ttk.Entry(self)
        DOB_entry.grid(column=1, row=1, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # phone number
        phone_label = ttk.Label(self, text="Phone(NNN-NNN-NNNN):")
        phone_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)
        phone_entry = ttk.Entry(self)
        phone_entry.grid(column=1, row=2, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # email
        email_label = ttk.Label(self, text="Email:")
        email_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)
        email_entry = ttk.Entry(self)
        email_entry.grid(column=1, row=3, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # payment
        payment_label = ttk.Label(self, text="Credit Card Number:")
        payment_label.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)
        payment_entry = ttk.Entry(self)
        payment_entry.grid(column=1, row=4, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        def submit_info():
            global newID
            newID = random_cid()
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            name = firstname + " " + lastname
            DOB = DOB_entry.get()
            DOBdate = datetime.strptime(DOB, '%Y-%m-%d').strftime('%Y-%m-%d')
            phone = phone_entry.get()
            email = email_entry.get()
            payment = payment_entry.get()
            sql = "INSERT INTO Customer (cid, Cname, DOB, Phone_num, Email, Payment_Information)" \
                  " VALUES (%s, %s, %s, %s, %s, %s)"
            vals = (newID, name, DOBdate, phone, email, payment)
            mycursor.execute(sql, vals)
            mydb.commit()

        # submit button
        submit_button = ttk.Button(self, text="Submit",
                                   command=lambda: [submit_info(), master.switch_Canvas(homescreen)])
        submit_button.grid(column=3, row=5, columnspan=2, sticky=tk.EW, padx=5, pady=5)

        # go back button
        back_button = ttk.Button(self, text="Cancel", command=lambda: master.switch_Canvas(StartUpPage)).grid(
            column=2, row=5)


class homescreen(tk.Canvas):  # Sub-lcassing tk.Frame
    def __init__(self, master, *args, **kwargs):
        # self is now an istance of tk.Frame
        tk.Canvas.__init__(self, master, *args, **kwargs)
        tk.Frame(self)

        # welcome user label
        welcome_label = ttk.Label(self, text=f"Welcome, User #{newID}")
        welcome_label.grid(column=0, row=0, columnspan=4)

        # view all flights button
        view_all_flights = ttk.Button(self, text="View All Flights",
                                      command=lambda: master.switch_Canvas(flightListFrame))
        view_all_flights.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        # view my information
        view_my_info = ttk.Button(self, text="View My Information", command=lambda: master.switch_Canvas(view_Info))
        view_my_info.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        # search for flights using flight code
        search_flights = ttk.Button(self, text="Search for Flights Using Code",
                                    command=lambda: master.switch_Canvas(flightListSearchFrame))
        search_flights.grid(column=2, row=1, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        # view my tickets
        view_my_tickets = ttk.Button(self, text="View My tickets", command=lambda: master.switch_Canvas(MyTickets))
        view_my_tickets.grid(column=3, row=1, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        # Close button
        close_button = ttk.Button(self, text="Exit").grid(column=3, row=2, pady=15)


class view_Info(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        mycursor.execute(f"Select * from Customer where Cid = {newID}")
        info = mycursor.fetchall()
        for i in info:
            cid = i[0]
            name = i[1]
            DOB = i[2]
            Phone_num = i[3]
            Email = i[4]
            Payment = i[5]

        # first name
        firstname_label = ttk.Label(self, text="CID: ")
        firstname_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
        firstname_entry = ttk.Label(self, text=cid)
        firstname_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        # last name
        lastname_label = ttk.Label(self, text="Name:")
        lastname_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
        lastname_entry = ttk.Label(self, text=name)
        lastname_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # Date of Birth
        DOB_label = ttk.Label(self, text="DOB(YYYY-MM-DD):")
        DOB_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)
        DOB_entry = ttk.Label(self, text=DOB)
        DOB_entry.grid(column=1, row=2, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # phone number
        phone_label = ttk.Label(self, text="Phone(NNN-NNN-NNNN):")
        phone_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)
        phone_entry = ttk.Label(self, text=Phone_num)
        phone_entry.grid(column=1, row=3, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # email
        email_label = ttk.Label(self, text="Email:")
        email_label.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)
        email_entry = ttk.Label(self, text=Email)
        email_entry.grid(column=1, row=4, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # payment
        payment_label = ttk.Label(self, text="Credit Card Number:")
        payment_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)
        payment_entry = ttk.Label(self, text=Payment)
        payment_entry.grid(column=1, row=5, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # go back button
        back_button = ttk.Button(self, text="Back", command=lambda: master.switch_Canvas(homescreen)).grid(
            column=2, row=6)


@dataclass
class Ticket:
    TID: str
    CID: int
    Flight_Info: int


class TicketFrame:
    ticketObj: Ticket
    root: tk.Frame
    TID_Info: ttk.Label
    CID_Info: ttk.Label
    Flight_Info: ttk.Label

    def __init__(self, root, ticketObj: Ticket):
        self.ticketObj = ticketObj
        self.root = root

        self.TID_Info = ttk.Label(self.root, text=ticketObj.TID)
        self.CID_Info = ttk.Label(self.root, text=ticketObj.CID)
        self.Flight_Info = ttk.Label(self.root, text=ticketObj.Flight_Info)

    # add this ticket frame to the grid
    def grid(self, row):
        self.row = row

        self.TID_Info.grid(column=0, row=row, sticky=tk.EW, padx=5, pady=5)
        self.CID_Info.grid(column=1, row=row, sticky=tk.EW, padx=5, pady=5)
        self.Flight_Info.grid(column=2, row=row, sticky=tk.EW, padx=5, pady=5)

    # forget this ticket frame and remove it from the grid
    def grid_forget(self):
        self.TID_Info.grid_forget()
        self.CID_Info.grid_forget()
        self.Flight_Info.grid_forget()


class MyTickets(tk.Frame):  # Sub-lcassing tk.Frame

    ticketFrames: list

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)

        # welcome label
        welcome_label = ttk.Label(self, text=f"Your Tickets")
        welcome_label.grid(column=1, row=0, columnspan=4, sticky=tk.EW)

        # table headers
        TID_label = ttk.Label(self, text="TID")
        TID_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
        CID_label = ttk.Label(self, text="CID")
        CID_label.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
        Flight_label = ttk.Label(self, text="Flight Number")
        Flight_label.grid(column=2, row=1, sticky=tk.EW, padx=5, pady=5)

        # mySQL stuff - query TB to receive tickets
        mycursor.execute(f"Select * from Ticket where Cid = {newID}")
        info = mycursor.fetchall()

        # generate all the tickets!
        self.retreiveTickets(info)

        # render all the tickets and the cancel ticket fields
        curr_row = 1
        for ticketFrame in self.ticketFrames:
            curr_row = curr_row + 1
            ticketFrame.grid(row=curr_row)

        # Cancel ticket section
        cancel_ticket_label = ttk.Label(self, text="Cancel Ticket (Tid):")
        cancel_ticket_label.grid(column=0, row=curr_row + 1, sticky=tk.EW, padx=5, pady=5)

        # field to type tid
        self.cancel_tid_entry = ttk.Entry(self)
        self.cancel_tid_entry.grid(column=1, row=curr_row + 1, columnspan=3, sticky=tk.EW, padx=5, pady=5)

        # Remove ticket based on given TID
        cancel_ticket_button = ttk.Button(self, text="Submit Cancellation", command=lambda: self.submit_cancel())
        cancel_ticket_button.grid(column=1, row=curr_row + 2, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        # Go back to home screen
        go_back_button = ttk.Button(self, text="Go Back", command=lambda: self.master.switch_Canvas(homescreen))
        go_back_button.grid(column=2, row=curr_row + 2, sticky=tk.EW, padx=5, pady=5, ipadx=2, ipady=2)

        self.grid(column=0, row=2, columnspan=3)

        # takes the tuples returned by an SQL query and converts them to valid ticketFrame objects

    def retreiveTickets(self, info):
        self.ticketFrames = []

        # create tickets and ticketFrames
        for i in info:
            newTicket = Ticket(i[0], i[1], i[2])

            newTicketFrame = TicketFrame(root=self, ticketObj=newTicket)
            self.ticketFrames.append(newTicketFrame)

    def submit_cancel(self):
        cancel_TID = int(self.cancel_tid_entry.get())

        # mySQL - delete the current ticket from the database, add the corresponding spot back to the flight!
        # TODO: add back the spot to the flight!
        mycursor.execute(f"DELETE FROM Ticket WHERE Tid = {cancel_TID}")
        mydb.commit()

        for row, i in enumerate(self.ticketFrames):
            if (i.ticketObj.TID == cancel_TID):
                self.ticketFrames[row].grid_forget()
                del self.ticketFrames[row]


@dataclass
class Flight():
    """Flight type"""
    flight_num: int
    departure_date: str
    departure_time: str
    destination: str
    spots_available: int
    gate: str


class flightFrame:
    flightObj: Flight
    root: tk.Frame
    flight_num_label: ttk.Label
    departure_date_label: ttk.Label
    departure_time_label: ttk.Label
    destination_label: ttk.Label
    spots_available_label: ttk.Label
    gate_label: ttk.Label
    buy_ticket_button: ttk.Button

    def __init__(self, flightObj: Flight, root):
        # setting up variables
        self.flightObj = flightObj
        self.root = root

        # Flight num
        self.flight_num_label = ttk.Label(root, text=f"{flightObj.flight_num}")

        # Departure Date
        self.departure_date_label = ttk.Label(root, text=f"{flightObj.departure_date}")

        # Departure Time
        self.departure_time_label = ttk.Label(root, text=f"{flightObj.departure_time}")

        # Destination
        self.destination_label = ttk.Label(root, text=f"{flightObj.destination}")

        # Spots available
        self.spots_available_label = ttk.Label(root, text=f"{flightObj.spots_available}")

        # gate
        self.gate_label = ttk.Label(root, text=f"{flightObj.gate}")

    def grid(self, row):
        self.row = row

        self.flight_num_label.grid(column=0, row=row, padx=4, pady=2, sticky=tk.EW)
        self.departure_date_label.grid(column=1, row=row, padx=4, pady=2, sticky=tk.EW)
        self.departure_time_label.grid(column=2, row=row, padx=4, pady=2, sticky=tk.EW)
        self.destination_label.grid(column=3, row=row, padx=4, pady=2, sticky=tk.EW)
        self.spots_available_label.grid(column=4, row=row, padx=4, pady=2, sticky=tk.EW)
        self.gate_label.grid(column=5, row=row, padx=4, pady=2, sticky=tk.EW)

        # TODO add buy button
        if (newID != ''):
            self.buy_a_ticket = ttk.Button(
                self.root,
                text="Buy ticket",
                command=lambda: self.buyTicket(),
                state=(DISABLED if self.flightObj.spots_available <= 0 else NORMAL)
            )
            self.buy_a_ticket.grid(column=6, row=row, padx=4, pady=2, sticky=tk.EW)

    def buyTicket(self):
        # buy a ticket code, incl SQL request!
        ticketID = random.randint(1, 10000000)

        sql = "INSERT INTO Ticket (Tid, Cid, Flight_num)" \
              " VALUES (%s, %s, %s)"
        vals = (ticketID, newID, self.flightObj.flight_num)
        mycursor.execute(sql, vals)
        mydb.commit()

        mycursor.execute(
            f"UPDATE Flight SET Spots_Available = {self.flightObj.spots_available} - 1 WHERE Flight_num = {self.flightObj.flight_num}")
        mydb.commit()

        # decrease the number of available spots
        self.flightObj.spots_available -= 1
        self.spots_available_label["text"] = f"{self.flightObj.spots_available}"

        # redraw the flight
        self.grid(row=self.row)


class flightListFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        flightList = []

        mycursor.execute(f"SELECT * FROM Flight")
        flights = mycursor.fetchall()
        for i in flights:
            flightList.append(Flight(i[0], i[1], i[2], i[3], i[4], i[6]))

        for row, flightObj in enumerate(flightList):
            prop = flightFrame(flightObj=flightObj, root=self)
            prop.grid(row=row)

        # go back button
        back_button = ttk.Button(self, text="Back", command=lambda: master.switch_Canvas(homescreen)).grid(
            column=6, row=row + 1, pady=10)


flightCode: str


class flightListSearchFrameList(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        flightList = []

        mycursor.execute(f"SELECT * FROM Flight WHERE Destination = '{flightCode}'")
        flights = mycursor.fetchall()
        for i in flights:
            flightList.append(Flight(i[0], i[1], i[2], i[3], i[4], i[6]))

        for row, flightObj in enumerate(flightList):
            prop = flightFrame(flightObj=flightObj, root=self)
            prop.grid(row=row)

        # go back button
        back_button = ttk.Button(self, text="Back", command=lambda: master.switch_Canvas(homescreen)).grid(
            column=6, row=row + 1, pady=10)


class flightListSearchFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        searchQuery = ttk.Label(self, text="Enter Flight Destination Code: ").grid(column=0, row=0)
        entry1 = ttk.Entry(self)
        entry1.grid(column=1, row=0, padx=5)

        def flight_Code():
            global flightCode
            flightCode = entry1.get()

        # submit button
        submit_button = ttk.Button(self, text="Submit",
                                   command=lambda: [flight_Code(), master.switch_Canvas(flightListSearchFrameList)])
        submit_button.grid(column=1, row=1, columnspan=2, sticky=tk.EW, pady=5)

        # go back button
        back_button = ttk.Button(self, text="Back", command=lambda: master.switch_Canvas(homescreen)).grid(
            column=0, row=1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()