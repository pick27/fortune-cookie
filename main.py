#!/usr/bin/env python

import webapp2
import random

def getRandomFortune():
    # list of possible fortune_sentence
    fortunes = [
        "I see much code in your future",
        "Consider eating more fortune cookies",
        "You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
    ]
    fortunes.append

    # randomly select one of the fortunes
    index = random.randint(0,len(fortunes)-1)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = '<strong>' + getRandomFortune() + '</strong>'
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"
        lucky_number = '<strong>' + str(random.randint(1, 100)) + '</strong>'
        number_sentence = 'Your lucky number: ' + lucky_number
        number_paragraph = '<p>' + number_sentence + '</p>'

        cookie_again_button = '<a href="."><button>Another cookie plz!</button></a>'

        content = header + fortune_paragraph + number_paragraph + cookie_again_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
