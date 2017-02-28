import web
import json
import unittest
from Lighting import Lights

'''from Lighting import AmbientLight'''
"""WebServer Api For the Car with the gettere and setters  """

urls = (
    '/(getLocation)','getLocation',
    '/(getLights)','getLights',
    '/(setLights)','setLights',
    '/(getAmbientLight)','getAmbientLight',
    '/(getAmbientTemp)','getAmbientTemp',
    '/(getRideHeight)','getRideHeight',
    '/(setRideHeight)','setRideHeight',
    '/(getBodyConfiguration)','getBodyConfiguration',
    '/(setBodyConfiguration)','setBodyConfiguration',
    '/(getBatteryInfo)','getBatteryInfo',
    '/(getMotion)','getMotion',
    '/(setMotion)','setMotion',
    '/(setSpeaker)','setSpeaker'
    )

app = web.application(urls, globals())

"""Get the Location of the Car location = {'Latitude':"Double ", 'Longitude':"Double", 'Altitude':"Double"}"""
def GET(self, name):
    location = {'Latitude':"34.5234'434", 'Longitude':"23.64345'32", 'Altitude':"12342.23"}
    return json.dumps(location)


"""Get the Light of the Car LightsOn = true/false"""
def GET():
	LightsOn= True
    return json.dumps(LightsOn)

    """Set the Light of the Car LightsOn = true/false"""
def SET1(self, name):
    params = web.input()
	LightsOn = Lights(False)
	params.light = None
    LightsOn.set(params.light)

    """Get the AmbientLight settings of the Car AmbientLight = {'LightValue': 'Int','LightLevel':"String"}"""
def GET1():
    AmbientLight = {'LightValue':0,'LightLevel':"daylight"}
    return json.dumps(AmbientLight)

    """Get the AmbientTemp settings of the Car AmbientTemp = {'Fahrenheight':'Int', 'Celcius': 'Int'}"""
def GET2(self, name):
    AmbientTemp = {'Fahrenheight':75, 'Celcius': 25}
    return json.dumps(AmbientTemp)

    """Get the RideHeight settings of the Car RideHeight = {'RideHeight': 'Int'}"""
def GET3(self, name):
    RideHeight = {'RideHeight': 6}
    return json.dumps(RideHeight)


    """Set the RideHeight settings of the Car RideHeight = {'RideHeight': 'Int'}"""
def SET2(self, name):
    params = web.input()
    RideHeight.set(params.RideHeight)

    """Get the BodyConfiguration settings of the Car  BodyConfiguration = {'Configuration': "Double"}"""
def GET5(self, name):
    BodyConfiguration = {'Configuration': "Speed"}
    return json.dumps(BodyConfiguration)
    """Get the BodyConfiguration settings of the Car  BodyConfiguration = {'Configuration': "Double"}"""
def SET3(self, name):
    params = web.input()
    BodyConfiguration.set(params.Configuration)
    """Get the BatteryInfo settings of the Car BatteryInfo = {'Cell1Volt': 'Double', 'Cell2Volt': 'Double', 'PercentCharge': 'Double'}"""
def GET6(self, name):
    BatteryInfo = {'Cell1Volt': 2.2, 'Cell2Volt': 2.1, 'PercentCharge': 99.2}
    return json.dumps(BatteryInfo)

    """Get the Motion settings of the Car  Motion = {'Angle': 'Double', 'Speed': 'Double', 'Direction': 'String'}"""
def GET7(self, name):
    Motion = {'Angle': 37.5, 'Speed': 7.325, 'Direction': Forward}
    return json.dumps(Motion)

def SET4(self, name):
    params = web.input()
    Motion.set(params.Motion)

def SET5(self, name):
    params = web.input()
    Speaker.set(params.text)
class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(GET())
    def test2(self):
        self.assertRaises(GET1())
    def test3(self):
        self.assertRaises(GET2())
    def test4(self):
        self.assertRaises(GET3())
    def test5(self):
        self.assertRaises(GET4())
    def test6(self):
        self.assertRaises(GET5())
    def test7(self):
        self.assertRaises(GET6())

if __name__  == "__main__":
    """Main menthod for the webserver to be running"""
    unittest.main()
