# 🌐 Mozilla Location Service WebGL Globe
### 📡 A look at the Mozilla Location Service with WebGL Globe

The [Mozilla Location Service](https://location.services.mozilla.com) (MLS) is an open-source location service provided by the folks at Mozilla. This visualization attempts to illustrate the scale of this project and connectivity hotspots around the world and is powered by the [WebGL Globe](http://www.chromeexperiments.com/globe) framework; an open-source project created by the Google Data Arts Team.

![Demo Image](/demo-images/demo_1.png)

### 🥰 Demo [mls-globe.alexyuan.me](https://mls-globe.alexyuan.me)

[![Netlify Status](https://api.netlify.com/api/v1/badges/e4fdd5f6-067c-47a1-8029-86a40bbb2dad/deploy-status)](https://app.netlify.com/sites/mls-globe/deploys)

#### How does it work?
* Make sure that the Mozilla Location Service data is inside your directory
* Change the name of the string which ```process.py``` reads to the file name of the data
* Now run ```python3 process.py```
* A JSON file named ```compiled.json``` should now be in your directory
* The globe should now visualize the new ```compiled.json``` file

If the lines on the globe seem very large or small, change the number which ```process.py``` adds during each processing iteration. The ```percision``` varible determines the accuracy of the data points which will appear on the globe.

The code which powers the demo is a tiny bit different than what you would find in the repository. A few changes needed to be made in order for things to work out smoothly on the web server.

#### Where is the data? Why is the file not found?
The data used to power this visualization was acquired from the Mozilla Location Service and was not added to this repository as it is very large. You can get it from [here](https://location.services.mozilla.com/downloads) though. After downloading the raw data, you'll have the rename the csv file name string in ```process.py```.

All feedback is appreciated. My personal website, portfolio, blog, and contact information is found at [alexyuan.me](https://alexyuan.me).

### 😮 Gallery
![Demo Image 2](/demo-images/demo_2.png)

![Demo Image 3](/demo-images/demo_3.png)
