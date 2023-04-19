import sys
from flask import Flask
from pypasser import reCaptchaV3

reCaptcha_response = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeBf0gaAAAAAOR1eq0Ypw6VKwNL3DS9zxR3P8mD&co=aHR0cHM6Ly93d3cuZGVzdGlueXJlc2N1ZS5vcmcuYXU6NDQz&hl=en&v=vkGiR-M4noX1963Xi_DB0JeI&size=invisible&cb=s6qcpjws25j9')

print("rrsp: "+ reCaptcha_response)
