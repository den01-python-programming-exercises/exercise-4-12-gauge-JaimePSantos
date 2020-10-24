class Gauge:
  value = 0

  def __init__(self,value):
    self.value = value
  
  def increase(self):
    if(self.value<5):
      self.value+=1
      return (self.value)
    else:
      return self.value
    
  def decrease(self):
    if(self.value>0):
      self.value-=1
      return (self.value)
    else:
      return self.value

  def value(self):
    return self.value
  
  def full(self):
    return (self.value == 5)