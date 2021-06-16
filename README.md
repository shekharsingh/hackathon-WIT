# hackathon-WIT
WIT hackathon 2021

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