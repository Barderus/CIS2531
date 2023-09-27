'''
Write a program that asks the user for his or her name, then asks the user to enter a sentence 
that describes himself or herself. Here is an example of the program’s screen:
    Enter your name: Julie Taylor 
    Describe yourself: I am a computer science major, a member of the 
Jazz club, and I hope to work as a mobile app developer after I graduate. 

Once the user has entered the requested input, the program should create an HTML file, 
containing the input, for a simple Web page. 

'''

import codecs
import webbrowser

def main():
    
    
    # Filename
    filename = "index.html"
    input_num = int(input("How many people would you like to have?: "))
    
    for p in range(input_num):
        user_name = input("What's your name?: ")
        user_descr = input("Enter a sentence that describe yourself: ")
        
        #Open a file
        outfile = open(filename, "a")
        html_template = """
        <html> 
        <head> </head> 
        <body>
        <center>
        <h1> """ + user_name + """</h1>
        </center>
        <hr>""" +  user_descr +	"""</hr>
        </body>
        </html>
            """
        outfile.write(html_template)
    outfile.close()
    
    file = codecs.open(filename, "r", "utf-8")
    webbrowser.open(filename)

main()