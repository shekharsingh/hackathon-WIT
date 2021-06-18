# ConnectF(armers)orGood

## Contents

- [ConnectF(armers)orGood](#submission-or-project-name)
  - [Contents](#contents)
  - [Short description](#short-description)
    - [What's the problem?](#whats-the-problem)
    - [How can technology help?](#how-can-technology-help)
    - [The idea](#the-idea)
  - [Demo video](#demo-video)
  - [The architecture](#the-architecture)
  - [Long description](#long-description)
  - [Project roadmap](#project-roadmap)
  - [Getting started](#getting-started)
  - [Live demo](#live-demo)
  - [Built with](#built-with)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Short description

### What's the problem?

Agriculture is one of the major means to eradicate poverty in the world. It must feed close to 10 billion people by 2050. 65% of people in the world survive with the income from agriculture.
It is very crucial for economic growth, eradication of poverty, and global GDP improvements among the countries in the world.
Current system of food is lot more threating in nature - lot of water usage (70% of water in the earth is used for agriculture), lot of unsustainable pollution and waste. One-Third of food produced is wasted globally. Fresh produce, nutrition values of produce is always retained only when produce reaches consumer households or any form of consumer earlier than now. It takes closer to 24-48 hours for a produce to reach a market and then takes about 4-5 hours to reach a household or the place where it’s used for making dishes.
Food insecurity has led to poor diet leading to lot of diseases. Healthy diet is becoming more and more unaffordable to large section of society.
On the other hand, farmers struggle to make ends meet. If a farmer must survive, farming policies needs to change across world and needs a massive shift – policy should deliver fair prices and allow them to make a living that never put them at risk any time during their lifetime. When farmer do better, we all do better, and vice-versa. Farming is termed inelastic – with farmers and consumers not knowing the demand and supply for a given year. Parity pricing set by farmer is important to address pricing woes and that will benefit farmer and help consumer consume without additional middleman cost
In the current era, most of the agricultural products are sold by farmers to money lenders or traders. These private middlemen or traders dominate the agricultural marketing exploiting farmers due to lack of adequate marketing infrastructure or logistics to reach consumers directly.
Lot of constraints that results in poor farmers though they feed the entire world includes but not limited to:
	Too many middlemen / Traders
	Fragmented nature of market - Limited infra to handle farmers produce.
	Density regulated markets – Demand and supply varies from place to place and densely populated areas determine the cost of product mostly.
	High market fee or logistic charges 
	High intermediation cost
	Limited rural credit facility for farmers
	Insufficient storage facility
	Malpractices in market – large gains for sampling almost half of produce, black marketing, hoarding etc.
The best way to address this is to ensure that a farmer friendly infrastructure is available that can help him/his family sell the produce to the nearby consumers to a comparatively higher cost than what a middleman provides.
For E.g. if a coconut we buy at house hold is Rs.40/-, then  the farmer used to sell the same for Rs.8/ to a middleman (Fact studied recently) and almost Rs.32 is incurred by middle man for transport and logistics.  But if there is an easy means for farmer to sell his produce directly to the consumers for say Rs.15 and let consumers in the neighboring location or same community pool in logistics cost which might not cost more than Rs.22 for a coconut. This is more of improving farmers economy and profit, beneficial to consumers with the satisfaction of knowing source of the produce and freshness of product.


### How can technology help?

Identify and register farmers to the CFG app, SMS or MMS facilities are also sufficient.
Let farmers decide the cost of their produce – provide potential help in developing a profit model initially.
Value chain proposition meetings to ensure not all farmers grow same produces all time.
Provide ways for farmers to leverage best farming practices – sustainable farming practices
Alternate income recommendations – live stocks – dungs can be used as manure, etc.,
Consumers in colonies., communities group together to ensure logistics on the way with benefit of sharing cost.


### The idea

==Farmers upload video of produce in Native or known language describing cost in retail or whole-sale, Quantity availability, location, and available items using the CFG android app
==The details extracted as below:
     >> Name of the farmer or Farm , Mobile Number, Location/Address, Name of produce-Type/Sub-Type, QTY of produce, Price for min and max QTY
==Same is uploaded to the IBM Cloud Object Storage (COS) for retrieving the text, image of produce and other relevant details using the trained ML model (PixelLib).
==The extracted details are put in json format and stored in IBM COS(Cloud Object Storage) as well and displayed for consumers once the video upload complete with extraction done on the android app
==User can then place the order on the app , the details are again consolidated in Cloud storage , fair pricing on logistics arrived at for community and order is confirmed.
==Once order is confirmed, community logistics will work towards collaborating with neighboring community using Newman detection algorithm


## Demo video

https://www.youtube.com/watch?v=mOgD1ICfoKU&list=PLMA3bIh3aDJ4tTf0TnD25wZ17uvgH6QAF&index=3

## The architecture


1. The user navigates to the android CFG app and uploads a video file.
2. IBM cloud object storage has a bucket created with the name "cgf-bucket", an instance and the video is uploaded.
3. Machine learning model PixelLib extracts the image, text from the uploaded video
4. Extracted text , image and details like name, type of fruit , cost, address, QTY availability is uploaded to IBM cloud object storage as json format
5. Json is downloaded by the app to get the list of items populated or avaialbe for consumers to use.
6. App with items are available for order with logistic calculation depending on the distance and it's like community funding for the logistics to have fresh produce on time
7. Community funding is collected as corpus to ensure farmers are supported with cash to borrow to ensure farming continues always to ensure they can make livelihood.
8. Additionally plan to ensure that extra or additional produce is donated to needy by adding little corpus.
9. Nearby communities do crowd funding or community funding for ensuring that logistics is recovered using the Newman detection algorithm 

## Long description

(./doc/CFG_ConnectFarmersForGood.docx)

## Project roadmap

The project currently does the following things.

- Step 1-6 is currently complete
- Steps 7-9 to be futurisitic and planned in near future.

Extensible futuristic solution
Plans to integrate Groceries as part of the app
Leverage Environment friendly farming practices and live sessions
Share canceled orders or produce to the nearest needy.
Lend loans to needy farmers with the community sharing corpus.
orpus to be used for sponsoring education of farmers kids till they stabilize as they start with CFG app.
Advantages/ and Disadvantages 
Limited / no middleman looting farmers anymore.
Farmers will be able to determine the cost
Best farming practices for sustainable living and greater food chain ability for future generation
Right cost for right produce

## Getting started
https://github.com/shekharsingh/hackathon-WIT

User
    - acc_create.py : creates account for a user based on AI interface
        TODO - user face data to be used for unique key and id for rest of the database
    - update_product_data.py : update the database with product details and pricing what user wants to sell.py :
        TODO - Add Face data to login automatically and pull the db for particular users
            Open camera app to record and upload video
Classify
    - fruitclassify.py - model to learn and classify fruits
        TODO - not saving models
    - fruit_transfer_learning.py - model to classify fruit. Saves model
        TODO -  accuracy less than 90%
    - fruits_model.h5 - saved model
    - dataset - dataset for fruits from kaggle
ObjectExtract
    - objDetect.py - extract objects from the image
        TODO - use same for different frames of Video
    - mask_rcnn_coco.h5 - model to get objects
    - Input.jpg - example
    - Output.jpg - find and tag all objects in the picture
    segmented_object_X.jpg - extract objects and saves

## Live demo

https://github.com/shekharsingh/hackathon-WIT

## Built with

Programming languages – Python, 
Machine Learning –Model – Pixel Lib & Audio bot
IBM catalog – IBM Cloud Object Storage , IBM COS SDK for Python using IBM_boto3
OS – Android Studio 4.2.1, Android SDK( 9.0,),SDK platform tools/SDK-tools -31.0.2/26.1.1

