#!/usr/bin/python

"""
Aplicacion redirectora
Rosa Cristina Ruiz Rivas
"""

import webapp
import random


class redirectora(webapp.webApp):
    """Address with classes"""

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """
        #recurso = parsedRequest[1]
        randomURL = str(random.randint(0, 1000000000))
        newURL = "http://localhost:1234/" + randomURL
        # Espera 5 segs antes de redirigir
        headHtml = '<meta http-equiv="Refresh" content="5;url=' + newURL + '">'
        codigoHTTP = "303 See Others"
        cuerpoHtml = "<p>Va a ser redirigido en 5 segundos a --> " + newURL
        cuerpoHtml += "</p>"
        return (codigoHTTP, "<HTML> <HEAD>" + headHtml + "</HEAD> <BODY>" +
                cuerpoHtml + "</BODY></HTML>")


if __name__ == "__main__":

    testWebApp = redirectora("localhost", 1234)
