from source1 import Source1 as src1
from source2 import Source2 as src2
from source3 import Source3 as src3
from source4 import Source4 as src4
from source5 import Source5 as src5
import sys




original_stdout = sys.stdout
with open('output.txt','w') as f:
    sys.stdout=f
    print("The output is being written to the file")
    src1.getData()
    src2.getData()
    src3.getData()
    src4.getData()
    src5.getData()
    sys.stdout = original_stdout
