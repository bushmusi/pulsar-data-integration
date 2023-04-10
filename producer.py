import random
import pandas as pd

timestamp = ['Jan 20, 2022', 'Feb 10, 2023']
type = ['ED', 'TD']
mac = ['mac1', 'mac2', 'mac3' ]
tlm_version = [0,1,2]
adv_count=[0,2,3]
run_time=['odoh60s', '0d0h0s']

def generate_values():
  return {
        'timestamp': random.choice(timestamp),
        'type': random.choice(type),
        'mac': random.choice(mac),
        'rssi': random.randint(-100,100),
        'tlm_version': random.choice(tlm_version),
        'battery_voltage': random.randint(0,3100),
        'chip_temp': random.uniform(20,40),
        'adv_count': random.choice(adv_count),
        'run_time': random.choice(run_time)
  }

fake_data = [generate_values() for _ in range(5)]
df = pd.DataFrame(fake_data)
df.head()
print(fake_data)