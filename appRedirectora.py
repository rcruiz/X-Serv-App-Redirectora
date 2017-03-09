#!/usr/bin/python3


import webapp
import random


class redirectora(webapp.webApp):

    def process(self, parsedRequest):

        randomURL = str(random.randint(0, 1000000000))
        newURL = "http://localhost:1234/" + randomURL
        # Espera 5 segs antes de redirigir
        headHtml = '<meta http-equiv="Refresh" content="3;url=' + newURL + '">'
        codigoHTTP = "303 See Others"
        cuerpoHtml = "<p>Va a ser redirigido en 3 segundos a --> " + newURL
        cuerpoHtml += "</p>"
        return (codigoHTTP, "<HTML> <HEAD>" + headHtml + "</HEAD> <BODY>" +
                cuerpoHtml + "</BODY></HTML>")


if __name__ == "__main__":

    testWebApp = redirectora("localhost", 1234)
