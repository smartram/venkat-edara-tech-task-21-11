# venkat-edara-tech-task-21-11
Ukufu assignment for coding

  - Python Flask app which inspects fridge contents and gives suggestions for lunch. 

  - json files are in resource folder which are used as fridge contents.

  - tests folder consists of unittests 

# Usage!
    
  - This considers current date
  -     curl -X GET http://127.0.0.1:8080/lunch
    

  -  *enhancement* 
      consider planning for lunch for future date then. Jan 07th 2020. yyyy-mm-dd
  -     curl -X GET http:127.0.0.1:8080/lunch?date=2021-01-07

### Contact
smart.ram856@gmail.com for any Python dev projects.

### Installation
 git clone git@github.com:smartram/venkat-edara-tech-task-21-11.git
 docker build -t edara_venkata_ukufu_techtask .
 docker run -p 8080:8080 edara_venkata_ukufu_techtask

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.
