import requests
import tkinter
url = "https://api.kanye.rest"
def retrieve_quote():
    """
    This function retrieves a random quote from the Kanye West API.
    """
    url = "https://api.kanye.rest"
    response = requests.get(url)
    data = response.json()
    return data['quote']


display = tkinter.Tk()
display.title("Kanye West Quotes")
display.resizable(False, False)
display.minsize(500, 600)

bg = tkinter.PhotoImage(file="Practice/API/kanye-quotes/background.png")
canvas = tkinter.Canvas(display, width=500, height=500)
canvas.pack()
canvas.create_image(250, 0, anchor="n", image=bg)
quotes_text = canvas.create_text(250, 60, text="Click the kanye button for a quote!", font=("Arial", 20, "bold"), fill="black", width=280, anchor="n")


def print_quote():
    quote = retrieve_quote()
    canvas.itemconfig(quotes_text, text=quote)


kanye = tkinter.PhotoImage(file="Practice/API/kanye-quotes/kanye.png")
kanye_button = tkinter.Button(display, image=kanye, borderwidth=0, highlightthickness=0, command=print_quote)
canvas.create_window(250, 400, window=kanye_button, anchor="n")

display.mainloop()