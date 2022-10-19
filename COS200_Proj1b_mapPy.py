import webbrowser
import folium as f
import os
import base64
from io import BytesIO
from PIL import Image
from folium import IFrame
from statistics import mean

# Kilroy Was Here - acknowledgements to Gabriel Tower for writing this class
# and implementing it

class mapper:

    # Create a map at given lat and long coords
    def createMap(self, lat, long, zoomLevel=10):
        return f.Map(location=[lat, long], zoom_start=zoomLevel)

    # Save map as an HTML file in a subfolder of the current working directory
    def saveMap(self, map, name="map.html"):
        if os.path.exists(os.getcwd() + "/maps"):
            if ".html" in name:
                map.save(os.getcwd() + "/maps/" + name)
            else:
                raise "Not .html file"
        else:
            os.mkdir(os.getcwd() + "/maps")

    # Call default web browser to open the HTML file containing the map
    def showMap(self, map):
        map.save("map.html")
        webbrowser.open("map.html")


    # Create a map marker with a thumbnail version of a specified image
    #   map: the map to add the marker to
    #   lat and long: coordinates of the marker you wish to add
    #   imgFileName: string containing full path name to image file
    #   scaleFactor: for creating an in-memory thumbnail (scaled-down) version of the image file

    def addMarkerWithImage(self, map, lat, long, imgFileName, scaleFactor=0.1, mTooltip="", mColor="blue", mIcon="info-sign"):
        # use of BytesIO as an in-memory file:
        # https://stackoverflow.com/questions/42800250/difference-between-open-and-io-bytesio-in-binary-streams

        # Use PIL.Image() to open file and find its horiz x vert size
        img = Image.open(imgFileName)

        # Make a thumbnail version of image file (default: 10% of full size)
        w = scaleFactor * img.width
        h = scaleFactor * img.height
        img.thumbnail([w, h], Image.ANTIALIAS)

        # Save to an in-memory file with handle 'tn' (thumbnail)
        tn = BytesIO()
        img.save(tn, 'JPEG')
        img.close()

        # Restore file pointer to start of file
        tn.seek(0, 0)

        # Now treat in-memory file as if it were a file on disk
        encoded = base64.b64encode(tn.read())
        html = '<img src="data:image/JPG;base64,{}">'.format
        iframe = IFrame(html(encoded.decode("UTF-8")), width=w+20, height=h+20)
        mPopup = f.Popup(iframe, max_width=2650)
        marker = f.Marker(
            location=[lat, long],
            popup=mPopup,
            icon=f.Icon(color=mColor, icon=mIcon),
            tooltip=mTooltip)
        marker.add_to(map)
        tn.close()

    # Given a list of [lat, long] coords, compute their mean
    # so map can be centered about that point
    def getCenterPoint(self, ptList):
        return mean(ptList)

