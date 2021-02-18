# Autonomous Waste Segregation Robotics
# INTRODUCTION
Taking inspiration from the existing autonomous solutions in the waste management sector we have created a vision system to segregate 5 types of plastic wastes - HDPE, LDPE, PET, PVC, and Polystyrene for different recycling purposes. We have used Pybullet, a Real-Time Physics Simulator to implement a KUKA LBR iiwa robotic arm for picking and sorting plastic wastes in simulation. Simulation and real-world results show that the vision system can classify different plastic wastes. Segregation of different plastic wastes is important since each plastic type has its unique use after recycling. This project has been done under the **Robotics Research Group(RoboReg)** at the **Indian Institute of Technology(BHU) Varanasi.**
* [Approach](#APPROACH)
* [Results](#RESULTS)
* [Team](#TEAM)
* [Mentors](#MENTORS)



# APPROACH
We have created 4 groups for plastic classification using the vision model and chosen 4 plastic objects belonging to each of the respective groups. The respective groups and plastic objects are:

1)**HDPE and PVC** : Pipe

2)**LDPE and HDPE**: Plastic Toys

3)**LDPE , HDPE and PET** : Plastic Bottles

4)**POLYSTYRENE** : Thermocol Sheets

The vision model predicts results both on real-world objects and simulation objects. We aim to successfully classify pictures of these plastic objects both in real-world and simulation environment into their corresponding plastic-type categories.

**THE VISION MODEL**-The vision system classifies given plastic waste image into one of the 4 categories based on the plastic type it is likely to be made of. Transfer Learning VGG-16 model with Deep Convolution Neural Network has been used to have faster and more accurate results.

**KUKA LBR iiwa robotic arm**-The robotic arm used is a modified Kuka arm ( KUKA LBR iiwa robotic arm) where a different gripper has been chosen.
The environment consists of four platforms labeled polystyrene, LDPE or HDPE, HDPE or PVC, HDPE or PET or LDPE placed equally spaced at four corners and with the robotic arm placed at the center. The waste material(object) which is to be classified, is simulated at a certain area.
# RESULTS
**Vision Model Predictions**
<div align="center"><img src="Results/pipe.png" width="20%"/><img src="Results/pipeS.jpg" width="20%"/><br/><img src="Results/Car.jpg" width="20%"/><img src="Results/carS.jpg" width="20%"/><br/><img src="Results/bottle.jpg" width="20%"/><img src="Results/bottleS.jpg" width="20%"/><br/><img src="Results/thermocol.jpg" width="20%"/><img src="Results/thermocolS.png" width="20%"/>
</div>
**KUKA LBR iiwa robotic arm movement**
<div align="center"><img src="Results/kuka arm 3.png" width="20%"/><img src="Results/kuka arm 2.png" width="20%"/><img src="Results/kuka arm 1.png" width="20%"/></div>

# TEAM
<table>
  <tr>
    <td align="center"><a href="https://github.com/AntaraB1005"><img src="https://avatars.githubusercontent.com/u/71094731?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Antara Banerjee</b></sub></a><br /></a></td>
     <td align="center"><a href="https://github.com/AtuL-KumaR-00"><img src="https://avatars.githubusercontent.com/u/64649440?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Atul Kumar</b></sub></a><br /></a></td>
      <td align="center"><a href="https://github.com/aditiagrawal123"><img src="https://avatars.githubusercontent.com/u/64923751?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Aditi Agrawal</b></sub></a><br /></a></td>
    </tr>
</table>

# MENTORS
<table>
  <tr>
    <td align="center"><a href="https://github.com/lok-i"><img src="https://avatars.githubusercontent.com/u/54435909?s=460&u=29af076049dab351b2e43621e9a433919bf50fb1&v=4" width="100px;" alt=""/><br /><sub><b>Lokesh Krishna</b></sub></a><br /></a></td>
    <td align="center"><a href="https://github.com/NiranthS"><img src="https://avatars.githubusercontent.com/u/44475481?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Niranth Sai</b></sub></a><br /></a></td>
    </tr>
</table>
