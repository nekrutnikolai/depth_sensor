## Low-Cost Depth Sensing Module For Deep-Water Instruments

<p align="center">
  <img src="images/sensor_ai.png" width="400" style="border-radius: 8px;">
</p>

<p align="center">
  AI-generated image of a depth sensor
</p>

A low-cost, durable depth-sensing module capable of providing approximate depth readings for underwater instruments submerged up to 2000 meters. Deliverables will include a fully functional prototype, field-tested for real-world integration.

> in Partial Fulfillment of the Requirements for the Degree of Master of Engineering, Electrical and Computer Engineering at Cornell University

### Introduction

This project addresses the challenge of developing a cost-effective depth sensor for intermediate to deep depths (up to 2000 meters). Existing solutions are either prohibitively expensive or unsuitable for these depths. In collaboration with Dr. V. Hunter Adams (Cornell ECE) and Jonathan Pfeifer (WHOI), this effort focuses on creating a robust, affordable sensor module designed for integration with underwater exploration vessels. The sensor balances practical accuracy with resilience to high-pressure underwater environments, supporting WHOI’s marine research with an innovative and accessible solution.

### Updates

Designed PCB schematic found in /depth_sensor_KiCad as per image below:

<p align="center">
  <img src="images/sensor_schematic.jpg" width="600" style="border-radius: 8px;">
</p>

<p align="center">
  Image of schematic
</p>


Wrote program to output ADC data over serial and to a real-time plotter program on my computer where I was measuring the voltage from a potentiometer. This program will serve as a good way to characterize the future hall-effect sensors.


<p align="center">
  <img src="images/adc_readout.png" width="400" style="border-radius: 8px;">
</p>

<p align="center">
  Live plot of ADC plotter
</p>


<p align="center">
  <img src="images/adc_setup.jpg" width="400" style="border-radius: 8px;">
</p>

<p align="center">
  Breadboard setup of potentiometer
</p>

<!-- Components have arrived but turns out that I received the wrong ones: -->

### Specifications to Meet

| **Parameter**      | **Specification**               |
|---------------------|---------------------------------|
| **Depth**          | 2,000 m                         |
| **Pressure**       | 200 atm                         |
| **Power Input**    | 5-24V @ ≤ 100mA                 |
| **Data Protocol**  | RS-232                          |
| **Physical Size**  | Soda can - Nalgene bottle sized |
| **Connector Type** | MacArtney SubConn               |
| **Accuracy**       | ±10 m                           |
| **Mounting**       | Hose clamps, bolts, etc.        |

### Timeline  
This project spans two semesters: **FA 2024 - SP 2025** with the following timeline:  

#### Fall 2024 Semester  
- ✅ **Sep-Nov**: Conduct research and finalize physical sensing mechanism  
- ✅ **Nov**: Order components  
- ⬜ **Dec**: Design circuit PCB (in progress)  
- ⬜ **Dec**: Initial testing with ordered components (in progress)  

#### Spring 2025 Semester  
- ⬜ **Jan-Feb**: Design algorithm to translate physical system into depth readings  
- ⬜ **Jan-Feb**: Assemble prototype & test at Helen Newman Pool  
- ⬜ **Feb**: Complete interface design and implement energy-efficient adjustments  
- ⬜ **Feb-Mar**: Integrate final hardware and software, prepare for field testing  
- ⬜ **Mar-Apr**: Perform field testing with WHOI; collect data and refine design  
- ⬜ **May**: Finalize module, complete documentation, and hand over the prototype to WHOI  




