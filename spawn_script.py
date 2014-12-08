"""In order for this code to work the objects and the spawner(controller) 
must be in different layers(scene) otherwise this won't work"""
import bge
sce = bge.logic.getCurrentScene()
spw = bge.logic.getCurrentController().owner #The controller is the object you have selected to write the script on
def main():
    object1 = sce.addObject("name_of_object1",spw)  #this will add an object at the location of the controller
    object2 = sce.addObject("name_of_object2",spw)
    object3 = sce.addObject("name_of_object3",spw)            
    spw.localPosition.x+=1  #This will change the location of your controller in the x axis
    spw.localPosition.y+=1  #This will change the location of your controller in the y axis
    spw.localPosition.z+=1  ##This will change the location of your controller in the z axis
    
main()