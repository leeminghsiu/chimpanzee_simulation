### chimp_simulator by Ming Hsiu Lee
> === How To Run The Program ===
 - install python at:
  https://www.python.org/downloads/
 1. install pygame in terminal
  ```
  python3 -m pip install -U pygame --user
  ```
 2. install numpy in terminal
  ```
  pip3 install numpy
  ```
 2. cd into directory and run "chimp_simulater.py" in terminal
  ```
  python3 chimp_simulater.py
  ```
 3. adjust the parameters in "global_setting.py"
 4. see what changes after rerun "chimp_simulater.py"
 

![287245764_7534802613260010_8555577397319911161_n](https://user-images.githubusercontent.com/89007851/173249679-a4905a3e-96b2-4b43-ba25-ac2c2b2db698.gif)
![287200602_421959506469482_5813033360425710554_n](https://user-images.githubusercontent.com/89007851/173249682-c0d0f6d6-168a-4489-9153-adc2b1337b5a.gif)
> === Thesis ===
Project Goal:
* to simulate animal mating behavior
* to find out the percentage of male who has mating right under different circumstances.

Male’s (dots) behavior
* each male chimp has random combat value (CV)
* higher the CV, larger the territory
* male always wandering in the map
* if a female (square) locate in his territory the male has mating right
* when territories overlapse females could be stolen

Female’s (squares) behavior
* wandering in the map at first 
* when entering a male’s territory → follows the male
* when be in 2 territories at the same time → chooses a male to follow based on CV
* will keep distance from same sex
<img width="510" alt="image" src="https://user-images.githubusercontent.com/89007851/173249931-2ee26b78-fa87-4608-a2a7-df272b3fc8a9.png">

<img width="786" alt="image" src="https://user-images.githubusercontent.com/89007851/173249943-0a10a56e-4ea0-4ae4-8bbe-58b46b6de86a.png">
<img width="786" alt="image" src="https://user-images.githubusercontent.com/89007851/173249952-412444dd-a4ba-47a6-beb2-c0b85de79494.png">
<img width="809" alt="image" src="https://user-images.githubusercontent.com/89007851/173249969-bd95b5b4-6aef-4869-b90f-44d41b08eda7.png">
<img width="809" alt="image" src="https://user-images.githubusercontent.com/89007851/173249975-75ef64b8-aae8-4f7a-ae96-fd51b37a4709.png">
<img width="809" alt="image" src="https://user-images.githubusercontent.com/89007851/173249983-68e215a0-a312-4478-b4cc-fee66cf5a2f1.png">
<img width="809" alt="image" src="https://user-images.githubusercontent.com/89007851/173249990-a92b6dcc-5cd9-4fa3-a1a2-89d412811e4b.png">
