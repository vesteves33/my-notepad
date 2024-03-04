import unittest
import app as api
import json

class TestFlaskApi(unittest.TestCase):
    
  def setUp(self):
        self.app = api.app.test_client()
    
  def test_get_method(self):
    response = self.app.get("/")
        
    self.assertEqual(
       response.get_json(),
       {
         "hello":"world"
       },)
    
  def test_post_method(self):
    # request payload
      payload = json.dumps(
        {           
        "firstname":"ruan",
        "lastname":"bekker"
        })
        
    # make request   
      response = self.app.post("/",data=payload,headers={"Content-Type":"application/json"})
        
    # assert  
      self.assertEqual(str,type(response.json['lastname']))  
      self.assertEqual(200,response.status_code)
    
  def tearDown(self):   
    # delete if anything was created
     pass

if __name__ == '__main__':  
  unittest.main()