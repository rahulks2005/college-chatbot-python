from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
from tkhtmlview import HTMLLabel

# ---------- Reset chat history file ----------
with open("chat_history.txt", "w") as f:
    f.write("CMR Chatbot Session:\n\n")

# ---------- Voice Engine ----------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening now")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            entry.delete(0, END)
            entry.insert(0, query)
            chatbot_response()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Internet error occurred.")

# ---------- Chatbot Logic ----------
chat_history_html = "<p><b>Bot:</b> Ask me something about CMR University!</p>"

def chatbot_response():
    global chat_history_html

    user_input = entry.get().strip().lower()
    entry.delete(0, END)

    # Smart keyword mapping
    if "course" in user_input or "program" in user_input:
        user_input = "course"
    elif "hi" in user_input or "hello" in user_input:
        user_input = "hi"
    elif "admission" in user_input or "apply" in user_input:
        user_input = "admission"
    elif "campus" in user_input or "tour" in user_input:
        user_input = "campus tour"
    elif "hostel" in user_input or "stay" in user_input or "accomodation" in user_input or "hostels" in user_input:
        user_input = "hostel"
    elif "sports" in user_input or "games" in user_input or "sport" in user_input or "play" in user_input:
        user_input = "sports"
    elif "placement" in user_input or "job" in user_input or "placements" in user_input or "highest package" in user_input or "average package" in user_input:
        user_input = "placements"
    elif "extracurricula" in user_input or "events" in user_input:
        user_input = "extracurricular"
    elif "foreign" in user_input or "international" in user_input:
        user_input = "international"
    elif "contact" in user_input or "phone" in user_input:
        user_input = "contact"    
    elif "location" in user_input or "map" in user_input:
        user_input = "location"    
    elif  "student erp " in user_input or "student login" in user_input or "erp portal" in user_input:
        user_input = "student erp"   
    elif "fees" in user_input or "fees structure" in user_input or "fee" in user_input or "admission fees" in user_input:
        user_input = "fees"
    else:
        print("dont understand ! sorry")    

    # Bot responses (HTML)
    if user_input in ["hi", "hello"]:
        bot_response = "<p><b>Bot:</b> Hi! Welcome to <b>CMR University</b>.</p>"
    elif user_input == "course":
        bot_response = """
        <p><b>Bot:</b> We offer 8 schools in the university:</p>
        <ul>
            <li><a href='https://www.cmr.edu.in/school/school-of-architecture/'>School of Architecture</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-design/'>School of Design</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-engineering-and-technology/'>Engineering & Technology</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-legal-studies/'>Legal Studies</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-management/'>Management</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-economics-and-commerce/'>Economics & Commerce</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-liberal-studies/'>Liberal Studies</a></li>
            <li><a href='https://www.cmr.edu.in/school/school-of-science-studies/'>Science & Computer Studies</a></li>
        </ul>
        """
    elif user_input in ["admission", "apply", "apply for 2026"]:
     bot_response = """
    <p><b>Bot:</b> Please follow the instructions below for applying to CMR University:</p>
    <ul>
        <li>The online application is for admission to programmes offered in CMR University.</li>
        <li>Application Form Fee is <b>Non-Refundable</b>.</li>
        <li>Email ID submitted at the time of registration will be used for all correspondences until enrolment is completed. Change in Email ID will <b>NOT</b> be permitted under any circumstances.</li>
        <li><b>CMR University Query Management System:</b>
            <ul>
                <li>Applicants are strongly advised to use CMR University Query Management System, rather than emailing, to get a quick response.</li>
                <li>Register and verify your email ID.</li>
                <li>Click on <b>[Any Queries? Ask US]</b> in your dashboard.</li>
                <li>Select the query category and submit your query.</li>
            </ul>
        </li>
    </ul>
    <p>👉 <a href='https://admissions.cmr.edu.in/'>Click here to apply for admission </a>.</p>
    """
     
    elif user_input == "campus tour":
        bot_response = "<p><b>Bot:</b> Explore our <a href='https://www.cmr.edu.in/lakeside-campus-tour/'>Campus Tour</a>.</p>"
    elif user_input in ["hostel","hostels","stay","accomodation"]:
        bot_response = """
        <p><b>Bot:</b> Students preferring accommodation at the hostels of CMR University can choose from the following accommodation types, as per their needs and budget:</p  
                       <ul>
                           <li> Single Occupancy : 160700 rupees,</li
                           <li> Double Occupancy : 152300 rupees,</li
                           <li> Triple Occupancy : 145300 rupees,</li
                           <li> Four sharing occupancy.</li 
                        </ul
                    </li>
                </ul>
                <p>  <a href='https://www.cmr.edu.in/hostel/#typesof_13921'>  more Hostel Details </a>.</p>


                """  
    elif user_input in ["sports","sport","games","play"]:
        bot_response = """
        <p><b>Bot: </b> At CMR we encourage talented sports students by providing various facilities for sports. The campus houses full fledged sports amenities such as:</p
                    <ul>
                        <li>Cricket Ground,</li
                        <li> Basket Ball Ground,</li
                        <li> Table Tennis,</li
                        <li> Football Ground,</li
                        <li> Indoor Sports.</li
                    </ul
                </li>
             </ul>       
              <p>   <a href='https://www.cmr.edu.in/sports/'>Sports & Activities</a>.</p>
              """
    elif user_input in ["placements","placement","job","package","highest package","average package"]:
        bot_response = """
           <p><b>Bot: </b>  Exclusive training programmes in soft skills and aptitude along with online tests are given to students to make them assess skills in broader areas. The centre provides optimal placement opportunities for all students to begin careers in their chosen field.
           </p
           <p>  <a href='https://www.cmr.edu.in/placement-cell/about-placements/'>Placement Cell</a>.</p>
           """
    elif user_input in ["extracurricular","events"]:
        bot_response = "<p><b>Bot:</b> Explore <a href='https://www.cmr.edu.in/co-curricular-extracurricular-activities/'>Co-curricular & Extracurricular Activities</a>.</p>"
    elif user_input in ["international","foreign "]:
        bot_response = "<p><b>Bot:</b> Info for <a href='https://www.cmr.edu.in/admissions/international/'>International Students</a>.</p>"
    elif user_input in ["contact","phone"]:
        bot_response = "<p><b>Bot: </b> You can contact us at (Off Hennur, Bagalur Main Road,Chagalatti, Bangalore 562149, Karnataka, India.Contact number - 70220 07672).</p> "    
    elif user_input in ["location","direction","map"]:
        bot_response = "<p><b>Bot:</b> here is a location <a href= 'https://www.google.com/maps/place/CMR+University+(Lakeside+Campus)/@13.1175674,77.6528692,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae1bd82408da43:0xeebaa35808847cd5!8m2!3d13.1175674!4d77.6554441!16s%2Fg%2F11byw4dtcl?entry=ttu&g_ep=EgoyMDI1MDYwOC4wIKXMDSoASAFQAw%3D%3D/'> Location</a>.</p>"
    elif user_input in ["student erp","erp portal","student login"]:
        bot_response = "<p><b>Bot: </b> <a href = 'https://erp.cmr.edu.in/login.htm;jsessionid=ADE8A23CD555346EFB5C315E856D3CC0/'>Student login</a>.</p>"
    elif user_input in ["fees","fees structure","admission fees","amount ","fee structure","fee"]:
        bot_response = "<p><b>Bot:</b> Please click the link given to see the fee structure - <a href = 'https://www.cmr.edu.in/admissions/fee-structure/'>Fees structure </a.</p>"
    else:
        bot_response = "<p><b>Bot:</b> Sorry, I don't understand that.</p>"

    # Update chat history
    chat_history_html += f"<p><b>You:</b> {user_input}</p>" + bot_response
    response_label.set_html(chat_history_html)

    # Save to text file
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\nBot: {bot_response.replace('<p>', '').replace('</p>', '').replace('<b>', '').replace('</b>', '')}\n\n")

    speak("Response sent")

# ---------- GUI ----------
window = Tk()
window.title("CMR Chatbot")
window.geometry("620x650")
window.configure(bg="#00B7C3")

# Logo Image
img = Image.open(r"C:\Users\Rahul k s\OneDrive\画像\Screenshots\Screenshot 2025-05-27 140604.png")
img = img.resize((300, 80))
photo = ImageTk.PhotoImage(img)

image_label = Label(window, image=photo, bg="#00B7C3")
image_label.image = photo
image_label.pack(pady=10)

# Entry Field
entry = Entry(window, width=60, bg="white", fg="black")
entry.pack(pady=5)

# Buttons
btn = Button(window, text="Send", command=chatbot_response, bg="#F6C90E", fg="black")
btn.pack(pady=2)

voice_btn = Button(window, text="🎤 Voice", command=listen, bg="#F6C90E", fg="black")
voice_btn.pack(pady=5)

# HTML Output Label (with full chat)
response_label = HTMLLabel(window, html=chat_history_html, background="white")
response_label.pack(fill="both", expand=True, padx=10, pady=10)

window.mainloop()
