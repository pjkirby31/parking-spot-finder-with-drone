## Capstone
Jan 20 - April.
Meeting Thursday 5-6pm

## Project 1 → Finding parking spots with drone
- What is done:  
    - Trained yolov4-tiny model to detect parking spots  
        - Used this dataset: https://public.roboflow.com/object-detection/pklot   
        - Could get more images with drone and add them to the training dataset to improve accuracy
    - Deployed model on Raspberry Pi 4
        - Done on a VM but close enough
    - Tested the raspberry pi camera along with the physical raspberry pi
    - Built the drone (just need the new pdb in order to finish the drone)
- What to do:  
    - Learn how to use QGroundControl  
        - It is installed on the Boyer PC, but it might be easier to install it on our laptops  
    - Set up software with drone and perform all the calibrations
    - Test flight?????
        - Definitely should do this in an empty open space for safety
    - Build propeller guards for the drone
         - If we’re going to do this it should probably be done before the test flight
    - Figure out how to get accurate readings from the GPS while drone is flying
        - Since we did order a second GPS a long time ago for the raspberry pi and there is a GPS with the pixhawk, we could set up 2 GPS modules and maybe take an average or something in order to get a more accurate reading
        - If we do that we’ll also know the relative position of where the drone should be based on the last picture, so we might also be able to use that too
        - I also think the GPS for the raspberry pi has an accelerometer so maybe that info could help
        - https://docs.lib.purdue.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1131&context=open_access_theses
    - Build some sort of website or web service that we will be able to post open parking spots to

## Project 2: → Vertical Farming with LGS
- What is done:
    - Have an idea of the goals for this project 
    - Are looking into using a vehicle to drive around the facility and take pictures instead of a drone
- What needs to be done:
    - Control vehicle and get it to follow lines
    - Implement a solution to open doors
        - Look at ppt for one way to do it
    - Find and implement a solution to take pictures high up
        - Use drone on top of car
        - Selfie stick technology
        - Scissor lift
        - Lifting arm
    - Begin data gathering on a type of plant so we can get images
    - Talk to LGS about different types of data we can collect
        - Amount of water plants get
        - Nutrition that plants get
        - Temperature around plants


    

