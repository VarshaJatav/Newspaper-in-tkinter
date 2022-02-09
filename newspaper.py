
from tkinter import *
from PIL import ImageTk, Image


root=Tk()
root.title("Newspaper")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root['bg']='white'
frame1=Frame(root, width = 500, bg= "black")
frame1.pack(side=TOP, fill=X)

label1=Label(frame1, text= "TODAYS NEWS ", font = "sans 35 bold", fg="white", bg="black", height=2)
label1.pack()


frame2=Frame(root, width = 1110,height=900)
frame2.pack(side="left", anchor="nw")
frame2.propagate(0)

label2=Label(frame2, text="India loses its most iconic voice, world mourns demise of Lata Mangeshkar", font= "sans 23 bold",justify="left")
label2.grid(row=0,column=0,columnspan=4)

label3=Label(frame2, text="Lata Mangeshkar was laid to rest at the Shivaji Park Ground with full state honours today, February 6. Fans have poured emotional tribute on Twitter as they mourn her demise.", font= "sans 11 italic",justify="left")
label3.grid(row=1,column=0,columnspan=4)

img1 = Image.open("lata_mangeshkar_ji.jpeg")
imgg1=img1.resize((520,320))
img1 = ImageTk.PhotoImage(imgg1)
lab1= Label(frame2,image = img1)
lab1.image = img1
lab1.grid(row=2,column=0,columnspan=2,sticky=W)


label4 = Label(frame2, text = '''
Legendary singer Lata Mangeshkar was laid to rest with full state honours on Sunday in the presence of her family at Mumbais Shivaji Park. Prime Minister Narendra Modi, actors Shah Rukh Khan, Aamir Khan, Vidya Balan and Ranbir Kapoor were among those who paid homage to the veteran singer. She died at Breach Candy hospital on Sunday of multi-organ failure at the age of 92. Daughter of Pandit Deenanath Mangeshkar and Shevanti Mangeshkar, Lata belonged to a musical family. Her father was a well-known Marathi musician and theatre artiste. She was first tutored by her father and later appeared as a child artiste in several of his plays.Legendary singer Lata Mangeshkar was laid to rest with full state honours on Sunday in the presence of her family at Mumbais Shivaji Park. Prime Minister Narendra Modi, actors Shah Rukh Khan, Aamir Khan, Vidya Balan and Ranbir Kapoor were among those who paid homage to the veteran singer. She died at Breach Candy hospital on Sunday of multi-organ failure at the age of 92. Daughter of Pandit Deenanath Mangeshkar and Shevanti Mangeshkar, Lata belonged to a musical family. Her father was a well-known Marathi musician and theatre artiste. She was first tutored by her father and later appeared as a child artiste in several of his plays.Legendary singer Lata Mangeshkar was laid to rest with full state honours on Sunday in the presence of her family at Mumbais Shivaji Park. Prime Minister Narendra Modi, actors Shah Rukh Khan, Aamir Khan, Vidya Balan and Ranbir Kapoor were among those who paid homage to the veteran singer. She died at Breach Candy hospital on Sunday of multi-organ failure at the age of 92.Legendary singer Lata Mangeshkar was laid to rest with full state honours on Sunday in the presence of her family at Mumbais Shivaji Park. Prime Minister Narendra Modi, actors Shah Rukh Khan, Aamir Khan, Vidya Balan and Ranbir Kapoor were among those who paid homage to the veteran singer. She died at Breach Candy hospital on Sunday of multi-organ failure at the age of 92. Daughter of Pandit Deenanath Mangeshkar and Shevanti Mangeshkar, Lata belonged to a musical family. Her father was a well-known Marathi musician and theatre artiste. She was first tutored by her father and later appeared as a child artiste in several of his plays.Legendary singer Lata Mangeshkar was laid to rest with full state honours on Sunday in the presence of her family at Mumbais Shivaji Park. Prime Minister Narendra Modi, actors Shah Rukh Khan, Aamir Khan, Vidya Balan and Ranbir Kapoor were among those who paid homage to the veteran singer.
''',font="sans 8 ", wraplength=650, justify="left")
label4.grid(row=2,column=2,sticky=E,columnspan=2)

frame3=Frame(root, width=500,height=700)
frame3.pack(side="left", anchor="ne")
frame3.propagate(0)

label5=Label(frame3, text="PM Modi takes Congress to the cleaners in searing  Parliament speech | Here's what he said", font= "sans 13 bold", justify="left", wraplength=450)
label5.grid(row=0,column=0)

img2 = Image.open("modii_ji.jpg")
imgg2=img2.resize((340,200))
img2 = ImageTk.PhotoImage(imgg2)
lab2= Label(frame3,image = img2)
lab2.image = img2
lab2.grid(row = 1, column = 0,sticky=W)


label6=Label(frame3, text='''Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP.Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP. Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP.Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP. Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP.Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP. Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP.Prime Minister Narendra Modi on Monday addressed the Lok Sabha towards the end of a discussion on the Motion of Thanks to the President. During his speech, PM Modi spoke about a number of issues, including government schemes, inflation, and the Opposition's criticism of the BJP. 
''', font = "sans 8 ",wraplength=400,justify="left")
label6.grid(row =2, column=0)


label7=Label(frame2, text="Punjab polls: Congress announces Charanjit Singh Channi as its CM face.", font= "sans 11 bold")
label7.grid(row=3,column=0,columnspan=2,sticky=SW)

label8=Label(frame2, text="Congress leader Rahul Gandhi on Sunday declared Charanjit Singh Channi as the party's chief minister face for the Punjab Assembly election.Congress leader Rahul Gandhi on Sunday declared Charanjit Singh Channi as the party's chief minister face for the Punjab Assembly election.", font= "sans 6 italic",wraplength=520)
label8.grid(row=4,column=0,columnspan=2,sticky=W)


label9=Label(frame2, text='''Putting an end to speculation, Congress leader Rahul Gandhi declared Charanjit Singh Channi as the party’s chief ministerial pick for the upcoming Punjab Assembly election during his visit to Ludhiana on Sunday.The decision was taken days after the Congress high command had sought people's opinion to decide its chief ministerial candidate in Punjab through IVR (Interactive Voice Response) calls. Announcing the Congress's CM face, Rahul Gandhi said as per the people's suggestion, the party wanted to have a chief minister from a poor background who understands the pain of the lower classes. Follow Assembly Elections LIVE Updates. "He [Channi] is from a poor family. He understands poverty and knows it deeply. And in his heart and blood there is Punjab," Rahul Gandhi said. After he was announced the CM candidate, Charanjit Singh Channi thanked Rahul Gandhi, saying a poor man became Punjab's chief minister because of him. "I thank everyone. This is a big battle which I can't fight alone. I don't have the money, courage to fight it. The people of Punjab will fight this battle,' Channi said.Punjab Congress chief Navjot Singh Sidhu, who was also in contention to be the party's CM face, hailed Rahul Gandhi, saying that only he could have made a Dalit as the chief minister of Punjab.  Charanjit Singh Channi and Navjot Singh Sidhu were the main contenders to be the CM face for the party, though both had assured Rahul Gandhi that whosoever was chosen they will stand by the decision.The Punjab Assembly Election 2022 will be held in a single phase on February 14 for 117 constituencies. The counting of votes will take place on March 10. While Charanjit Singh Channi is contesting the upcoming Punjab polls from both Bhadaur and Chamkaur Sahib constituencies, Navjot Singh Sindhu will be in the fray from Amritsar East.
''', font = "sans  5",wraplength=250,justify="left")
label9.grid(row =5, column=0,sticky=W)


img3 = Image.open("cm_punjab.webp")
imgg3=img3.resize((250,180))
img3 = ImageTk.PhotoImage(imgg3)
lab3= Label(frame2,image = img3)
lab3.image = img3
lab3.grid(row = 5, column = 1)


label10=Label(frame2, text="Coronavirus Omicron variant India live updates: India's recovery rate stands at 96.46%", font= "sans 14 bold",wraplength=640,justify="left")
label10.grid(row=3,column=2,columnspan=2)


label11=Label(frame2, text="India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. A total of 1,188 deaths were registered in 24 hours, taking the death toll to 5,04,062, said the Union health ministry on Tuesday morning. Stay with TOI for the latest updates: India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. A total of 1,188 deaths were registered in 24 hours, taking the death toll to 5,04,062, said the Union health ministry on Tuesday morning. Stay with TOI for the latest updates: India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. A total of 1,188 deaths were registered in 24 hours, taking the death toll to 5,04,062, said the Union health ministry on Tuesday morning. Stay with TOI for the latest updates:", font= "sans 8",wraplength=640,justify="left")
label11.grid(row=4,column=2,rowspan=2,sticky=N,columnspan=2)


img4 = Image.open("corona_image.webp")
imgg4=img4.resize((150,90))
img4 = ImageTk.PhotoImage(imgg4)
lab4= Label(frame2,image = img4)
lab4.image = img4
lab4.grid(row = 5, column = 3,stick=S)


label12=Label(frame2, text="India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours, a considerable decline of 19 per cent against 83,876 cases reported on the previous day. A total of 1,188 deaths were registered in 24 hours, taking the death toll to 5,04,062, said the Union health ministry on Tuesday morning. Stay with TOI for the latest updates: India on Tuesday reported 67,597 fresh Covid cases in a span of 24 hours,.", font= "sans 7",wraplength=500,justify="left")
label12.grid(row=5,column=2,sticky=S)

root.mainloop()