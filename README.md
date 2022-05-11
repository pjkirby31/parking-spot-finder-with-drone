## Parking Spot Finding Drone

### Raspberry Pi Setup
#### Things to install
- Python 3 (I recommend creating a python virtual enviroment)
    -  Look at requirements.txt for the packages needed for this project
- Redis server
- tmux (not necessary but highly recommended)

#### How to run

1. Install everything
2. Go through the scripts in the drone-flying folder and make sure all the code is going to do what you expect
    - Do test runs without the propellers on 
3. Run stuff and see how it goes


### How does the drone work?

![image](https://user-images.githubusercontent.com/61844179/167757377-545a5b0b-def2-4e1f-9a3a-6b4499c49571.png)
This is a basic diagram of how we talk to the drone. We connect via wifi over ssh to the raspberry pi. The pi is connected to the drone's flight controller over USB. This allows us to be able to talk directly to the flight controller from our laptop. This could be upgraded to radio or a cellular connection once the drone becomes more autonomous since our idea was that the raspberry pi would be able to handle all of the flight stuff on its own.


![image](https://user-images.githubusercontent.com/61844179/167758017-a0066bdd-1243-4891-9c15-03f205a0bfd4.png)
This is a bit more in depth view of what's going on.
1. The camera script takes pictures with the USB camera and saves them every half second
2. The dashboard script uses Rich to display a nice looking dashboard with different drone metrics on it to the terminal
    - It retrieves all of the metrics from the Redis server
3. The ping script constantly pings the home laptop to ensure that there is always a connection. If this connection is ever broken the drone will automatically land.
    - If the drone flies farther this should probably be taken out, but it is a nice safety feature
4. The flying script takes in manual input and converts it to a certain movement for the drone
    - Keys are mapped to movements as followed:
        - w  -> increase altitude by 1m
        - s -> decease altitude by 1m
        - a -> decrease yaw to face left (not mapped out yet)
        - d -> increase yaw to face right (not mapped out yet)
        - left arrow -> fly west (uses gps so not exact amount)
        - right arrow -> fly east
        - up arrow -> fly north
        - down arrow -> fly south
    - 
