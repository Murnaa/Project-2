import qrcode
import PySimpleGUI as sg

sg.theme('black')


qr_colors = ['black', 'white', 'purple', 'blue', 'pink', 'yellow']

# To define the layout 
layout = [[sg.Text('Enter Text:')],
          [sg.InputText()],
          [sg.Text('Select QR Code fill color:')],
          [sg.OptionMenu(qr_colors, default_value='black', key='fill_color')],
          [sg.Text('Select QR Code background color:')],
          [sg.OptionMenu(qr_colors, default_value='white', key='back_color')],
          [sg.Button('Generate QR Code'), sg.Button('Exit')]]

# Create the window
window = sg.Window('QR Code Generator', layout)

# Create event loop for the app
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Generate QR Code':

        #To get text from input box
        text = values[0]
        if text.strip():

            #To get the selected fill and background colors
            fill_color = values['fill_color']
            back_color = values['back_color']

            # To generate the QR code with the selected colors
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)

            # To save the generated QR Code image to a file
            img_file = 'qr_code.png'
            img.save(img_file)

            # Display a popup message with the generated QR code image
            sg.popup('Your QR Code!', image=img_file)

            window.close()
        else:
            # Show an error message if the input text is empty
            sg.popup_error('Please enter text')
