import tkinter
import random
root=tkinter.Tk()
root.title('Ash-Card Deck')
root.geometry("900x500")
root.configure(background="green")

my_frame=tkinter.Frame(root, bg="green")
my_frame.pack(pady=20)
#Creating frames for cards
main_deck=tkinter.LabelFrame(my_frame, text="Deck of cards",bd=0)
main_deck.grid(row=0,column=0,padx=20 ,ipadx=20)

#Now putting the cards in Frames
card_label=tkinter.Label(main_deck,text='')
card_label.pack(pady=20)


def shuffle():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values=range(2,15)

    global deck
    deck=[]

    for suit in suits:
        for value in values:
            deck.append(f'{value} __of__{suit}')
            #print(deck)
    #print(len(deck))

    #Grabbing a Random Card
    draw_card=random.choice(deck)
    deck.remove(draw_card)
    main_deck.append(draw_card)


#Creating buttons for shuffle etc
shuffle=tkinter.Button(root,text="Shuffle Deck",font=("Helvetica",14),command=shuffle)
shuffle.pack(pady=20)
card=tkinter.Button(root,text="Pick Card",font=("Helvetica",14))
card.pack(pady=20)
root.mainloop()
