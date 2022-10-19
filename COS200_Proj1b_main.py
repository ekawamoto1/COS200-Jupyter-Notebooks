# https://pypi.org/project/exif/
# https://gis.stackexchange.com/questions/357578/python-geopys-nominatim-reverse-geocoding-access-type-e-g-amenity
# https://towardsdatascience.com/reverse-geocoding-in-python-a915acf29eb6
#
#
# Exercises:
# 0. Upload to your laptop 5 or so photos you've taken with your mobile device, and put them in a folder
# 1. Assign to a variable a default scale factor to downsize megapixel images (suggested value 10%)
# 2. Assign to another variable a default zoom level for viewing a map with thumbnails of your images (suggested value 14)
# 3. Obtain and print a list containing the names of the files contained in the folder
# 4. If the image has EXIF data, obtain and print the x- and y-dimensions of each image
# 5. Write a UDF decimal_coords() that converts [deg, min, sec] to decimal degrees, multiplies that value by -1 
#    if the latitude reference is S or the longitude reference is W, and returns that value as a float
# 6. Addresses returned by the geocoder are strings with commas as separators; convert this to a list of strings
# 7. Create a Pandas dataframe whose columns are the lists of filenames, latitudes, longitudes, and addresses 
#    (use the list of strings, not the string with commas), give its columns those titles, then print the dataframe
# 8. Set the tooltip string to have the filename (not the entire path!), street address, and city/county/state/ZIP/country
#    on three separate lines (hint: HTML line breaks use the markup tag '<br>' instead of '\n')
#

import os
import mapPy                              # GT's mapping package
import pandas as pd                       # for dataframes
from geopy.geocoders import Nominatim     # geocoder service
from exif import Image                    # EXIF (exchangeable image file format): https://en.wikipedia.org/wiki/Exif

# For converting [deg, min, sec] to fractional degrees 
# longitude referenced to prime meridian (+ if E, - if W) 
# latitude referenced to equator (+ if N, - if S)
def decimal_coords(coords, ref) -> float:
    pass


# The main application
def main():
    # Scaling of thumbnail version of images to be used as markers


    # Default zoom level


    # Specify name of folder containing image files to be placed on map
    folderName = r'C:\Users\YourName\FolderContainingYourPhotos'

    # List the files found in the folder



    # Create lists for files with EXIF info - eventually turn this into a Pandas dataframe
    fileFullnameList = []
    fileList = []
    latList = []
    longList = []
    addrList = []

    for f in folderFileList:
        filename = folderName + '\\' + f

        # Create exif.Image object from handle of open file, then close file
        try:
            src = open(filename, 'rb')
            img = Image(src)
            src.close()
        except:
            print('Could not open', filename)
            continue

        print('Opening', src.name, '...')
        try:
            if img.has_exif:
                # Extract EXIF info from file

                print('GPS longitude:', img.gps_longitude, img.gps_longitude_ref)
                print('GPS latitude:', img.gps_latitude, img.gps_latitude_ref)
                lat = round(decimal_coords(img.gps_latitude, img.gps_latitude_ref), 6)
                long = round(decimal_coords(img.gps_longitude, img.gps_longitude_ref), 6)
                print('lat, long:', str(lat) + ', ' + str(long))

                # Reverse geocode lookup (lat/long -> address) using OSM (OpenStreetMap) and Nominatim service
                addr = Nominatim(user_agent="myApp").reverse([lat, long], language='en')

                print('address:', addr)

                # Only add filename, lat/long coords, and address for files with EXIF info
                fileList.append(f)
                fileFullnameList.append(filename)
                latList.append(lat)
                longList.append(long)
                addrList.append(addrL)
                print()
            else:
                print(src.name, 'has no EXIF info!')

        except:
            print('An exception occurred while trying to read EXIF data from', src.name, '\n')
            continue

    # Populate a dataframe from the lists created above



    # Generate a map and center it on the average of the latitudes and longitudes
    mapy = mapPy.mapper()
    map = mapy.createMap(mapy.getCenterPoint(latList), mapy.getCenterPoint(longList), 14)

    # Make sure that we actually generated a map
    assert map is not None

    # Add markers to map: hover gives file name, click gives thumbnail
    i = 0
    n = len(fileList)
    for i in range(n):
        ss1 = ' '.join(addrList[i][:-6])
        ss2 = ' '.join(addrList[i][-5:])
        tóoltipStr = ''
        mapy.addMarkerWithImage(map, latList[i], longList[i], fileFullnameList[i], 0.1, mColor='red', mTooltip=tooltipStr)
        i += 1

    # Save the map
    mapy.saveMap(map, "test_map.html")

    # Render the map in a web browser
    mapy.showMap(map)


if __name__ == "__main__":
    main()
