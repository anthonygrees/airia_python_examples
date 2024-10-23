# output a plot/graph to pipeline output
#
import os
 
# Set the HOME or XDG_CONFIG_HOME environment variable to a valid directory
os.environ['HOME'] = '/tmp'# or any valid directory path
 
# Continue with your imports and code
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
 
# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)
 
# Create a plot
plt.plot(x, y)
 
# Add labels and title
plt.xlabel('X-axis (radians)')
plt.ylabel('Y-axis (sin(x))')
plt.title('Sine Wave')
 
# Save the plot to a BytesIO object
buffer = BytesIO()
plt.savefig(buffer, format='png')
plt.close()
 
# Convert the plot to base64
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
 
output = image_base64 + "\n\n\n" + image_base64
