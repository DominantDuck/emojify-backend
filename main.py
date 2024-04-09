from flask import Flask, render_template, request, redirect, url_for
from journal import journal
import detect
from storage import storage_main

app = Flask(__name__)

emojis = []
entry = ""
button_images = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journal', methods=['POST']) #Should activate when user hits "enter"
def journal_space():
    global entry 
    global journal_emojis

    journal_entry = request.form['user-entry']
    print(journal_entry)

    entry = journal_entry #this is for storage purposes

    journal_emojis = journal.assign_emojis(journal_entry)
    # detect.process_emojis(journal_emojis) #sends emojis to video_feed

    print(journal_emojis)
    return redirect(url_for('index'))

@app.route('/snapshot', methods=['POST']) #should activate when the user clicks on the video feed of the website; a snapshot of the screen is sent
def snapshot():

    image_data_url = request.json.get('image_data_url') #David, write html code that that takes a screenshot of the video feed area
    if image_data_url:
        newest_button_dropdown = storage_main.create_summary(image_data_url, entry)
        move_images_down(newest_button_dropdown)
    #newest button needs to be sent to the html file and assinged to the newest button (1st button)


def move_images_down(newest_button_dropdown): 
    global button_images
    for i in range(len(button_images), 0, -1):
        if i == 1:
            button_images[i] = newest_button_dropdown
        else:
            button_images[i] = button_images[i - 1]
    

#for loop: 1st button = 1st img, etc.
    
if __name__ == '__main__':
    app.run(debug=True)
