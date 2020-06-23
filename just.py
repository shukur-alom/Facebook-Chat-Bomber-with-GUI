import fbchat,time
import PySimpleGUI as sg
t=False
from fbchat import Client
try:
	username='' #Enter your fb username
	client= fbchat.Client(username,'x') # x is you password enter
except: print("Chack your net connection abd try angain")
while True:

	sg.theme('DarkAmber')	# Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Text('Chat Boombing')],
					[sg.Text('Id name'), sg.InputText()],
					[sg.Text('Massage'), sg.InputText()],
					[sg.Text('How'), sg.InputText()],
					[sg.Button('Ok')] ]

	# Create the Window
	window = sg.Window('Window Title', layout)
	# Event Loop to process "events" and get the "values" of the inputs
	event, values = window.read()
	if event == sg.WIN_CLOSED :	# if user closes window or clicks cancel
		break
	name = str(values[0])
	msg = str(values[1])
	hw = int(values[2])
	window.close()
	i=1
	while i<=hw:
		ti=time.time()
		friends = client.searchForUsers(name)
		friend = friends[0]
		sent = client.send(fbchat.models.Message(msg),friend.uid)
		print(F'\n\n\t\tRun Time {time.time()-ti}')
		i=i+1