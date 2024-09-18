# -Simplified-implementation-of-the-P2P-update-process

## Describe
My solution to the training problem of designing a simplified P2P process
The text of the task:
In a smart home system controlled by the voice assistant Larisa, there are n devices that connect to each other via the LoRaWAN network. Device number 1 is connected to the Internet and has downloaded an update that needs to be transmitted to all devices.

The LoRaWAN network is very slow, so a peer-to-peer (P2P) protocol was invented to distribute the protocol. The update file is divided into k equal-sized parts, numbered from 1 to k.

Transmission of a part of the update occurs during timeslots. Each timeslot takes one minute. During one timeslot, each device can receive and transmit exactly one part of the update. That is, during a timeslot, a device can receive a new part of the update and transmit the part of the update it already has at the beginning of the timeslot, or perform only one of these actions, or not receive or transmit at all. After receiving a part of the update, the device can transmit this part of the update to other devices in the following timeslots.

Before each timeslot, for each part of the update, it is determined how many devices in the network have downloaded this part. Each device selects the missing part of the update that is encountered the least frequently on the network. If there are several such parts, then the missing part of the update with the lowest number is selected.

Then the device makes a request for the selected part of the update from one of the devices that has already downloaded this part of the update. If there are several such devices, the device that has downloaded the fewest parts of the update is selected. If there are several such devices, the device with the lowest number is selected.

After all the requests have been sent, each device chooses whose request to satisfy. Device A satisfies the request that came from the device that is most valuable to A. The value of device B for device A is defined as the number of parts of the update previously received by device A from device B. If device A receives several requests from equally valuable devices, then the request of the device that has downloaded the fewest parts of the update is satisfied. If there are several such requests, the device with the lowest number is selected.

A new timeslot then begins. The devices whose requests are satisfied download the requested part of the update, and the others do not download anything.

For each device, determine how many timeslots it will take to download all parts of the update.

## How to use
To execute the script, simply run the file with the .py extension.
